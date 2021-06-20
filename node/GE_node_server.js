/**
 * Created by jonc on 8/1/2021.
 */
const express = require('express'),
    app = express(),
    mysql = require('mysql'),
    port = 8001,
    dbConfig = {
        host: 'localhost',
        database: 'wallstreet',
        user: 'root',
        password: '123QWEasd',
        port: 3306,
        multipleStatements: true
    },
    hkDBConfig = {
        host: 'localhost',
        database: 'hk',
        user: 'root',
        password: '123QWEasd',
        port: 3306,
        multipleStatements: true
    };

const bodyParser = require('body-parser');
app.set('port', process.env.PORT || port);
app.use(bodyParser.json());
app.use((req, res, next) => {
    res.set({
        'Access-Control-Allow-Credentials': true, // 允许后端发送cookie
        'Access-Control-Allow-Origin': req.headers.origin || '*', //任意域名都可以访问,或者基于我请求头里面的域
        'Access-Control-Allow-Headers': 'X-Requested-With,Content-Type',//设置请求头格式和类型
        'Content-Type': 'application/json; charset=utf-8'//默认与允许的文本格式json和编码格式
    });
    req.method === 'OPTIONS' ? res.status(204).end() : next();
});

function compareData(data, baseYear, fields, res_map, shareBasic){
    let index;
    for (let i = 0;i<data.length;i++){
        if(data[i].report_year == baseYear){
            index = i;
            break;
        }
    }
    for (let i = 0;i<data.length;i++){
        if(index!=i){
            res_map[data[i].report_year] = Object.assign({},data[i]);
            let ratio = [];
            for (let f of fields){
                let r;
                if(f!='report_year'){
                    if (f=='DilutedAverageShares'){
                        if(shareBasic && shareBasic!=null){
                            r = parseFloat(shareBasic/parseFloat(data[i][f]));
                        }else {
                            r = parseFloat(data[index][f])/parseFloat(data[i][f]);
                        }
                    }else{
                        r = parseFloat(data[index][f])/parseFloat(data[i][f]);
                        ratio.push(r);
                    }
                    res_map[data[i].report_year][f+'_ratio'] = r;
                }
            }
            if(fields.length){
                res_map[data[i].report_year].growRatio = ratio.reduce((a, b) => a + b) / ratio.length;
            }else{
                res_map[data[i].report_year].growRatio = 1;
            }
        }
    }
}

function fixSharesBias(res_map, compare_years){
    // console.log(res_map);
    const final_result = {};
    for(let y of compare_years){
        let total_grow = [];
        for (let i in res_map){
            let r = res_map[i][y]['growRatio'] / res_map['income'][y]['DilutedAverageShares_ratio'];
            res_map[i][y]['after_fixshares_ratio'] = r;
            total_grow.push(r);
        }
        final_result[y] = {ratio: total_grow.reduce((a, b) => a + b) / total_grow.length};
    }
    return Object.assign({},final_result);
}
app.post('/value_analyse', (req, res) => {
    let symbol = req.body.symbol,
        compare_years = req.body.compare_years,
        balance_fields = req.body.balance_fields,
        income_fields = req.body.income_fields,
        cash_fields = req.body.cash_fields,
        shareBasic = req.body.shareBasic,
        basic_years = req.body.basic_years,
        connection = symbol.includes('.HK')?mysql.createConnection(hkDBConfig):mysql.createConnection(dbConfig);
    if(symbol.includes('.HK')){
        symbol = symbol.replace('.HK', '');
    }
    let balance_query = 'SELECT report_year' + (balance_fields.length?', '+balance_fields.join():'') + ' FROM balance_table WHERE stock_symbol ="' + symbol + '" AND report_type="annual" AND report_year IN (' + compare_years.concat([basic_years]).join() + '); ',
        income_query = 'SELECT report_year, DilutedAverageShares' + (income_fields.length?', '+income_fields.join():'') + ' FROM income_sheet_table WHERE stock_symbol ="' + symbol + '" AND report_type="annual" AND report_year IN (' + compare_years.concat([basic_years]).join() + '); ',
        cash_query = 'SELECT report_year' + (cash_fields.length?', '+cash_fields.join():'') + ' FROM cash_flow_table WHERE stock_symbol ="' + symbol + '" AND report_type="annual" AND report_year IN (' + compare_years.concat([basic_years]).join() + ');';

    connection.query(balance_query + income_query + cash_query, (err, ret) => {
        if (err) {
            console.log(err);
        } else {
            const balance_table_data = ret[0],
                income_table_data = ret[1],
                cash_table_data = ret[2],
                res_map = {balance:{},cash:{},income:{}};

            // console.log(balance_table_data);
            // console.log(income_table_data);
            // console.log(cash_table_data);

            compareData(balance_table_data, basic_years, balance_fields, res_map.balance);
            compareData(income_table_data, basic_years, income_fields.concat(['DilutedAverageShares']), res_map.income, shareBasic);
            compareData(cash_table_data, basic_years, cash_fields, res_map.cash);
            res_map.final = fixSharesBias(res_map, compare_years);

            // console.log(res_map);

            let avg_price_query = [];
            for (let i of compare_years){
                avg_price_query.push('SELECT AVG(Pri_close) as avg_'+i +' FROM daily_price_'+i+' WHERE stock_symbol="'+ symbol +'"');
            }
            connection.query(avg_price_query.join('; '), (err, ret) => {
                if (err) {
                    console.log(err);
                } else {
                    // console.log(ret.length);
                    const ePrice = [];
                    for (let i =0; i<ret.length; i++){
                        const year = Object.keys(ret[i][0])[0].split('_')[1],
                            avg_price = ret[i][0]['avg_'+year];
                        res_map.final[year].avg_price = avg_price;
                        res_map.final[year].est_price = parseFloat(avg_price * res_map.final[year].ratio);
                        ePrice.push(res_map.final[year].est_price);
                    }

                    res_map.final_est_fair = ePrice.reduce((a, b) => a + b) / ePrice.length;
                    res_map.final_est_trade = res_map.final_est_fair * 0.7;
                    console.log(res_map);
                    return res.send(JSON.stringify({"code":1,"msg":res_map}));
                }
                connection.end();
            });
        }
    });


});

app.listen(port, () => console.log(`server listening at portt:${port}`));