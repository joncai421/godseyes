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
app.post('/value_analyse', (req, res) => {
    const symbol = req.body.symbol,
        compare_years = req.body.compare_years,
        balance_fields = req.body.balance_fields,
        income_fields = req.body.income_fields,
        cash_fields = req.body.cash_fields,
        shareBasic = req.body.shareBasic,
        basic_years = req.body.basic_years,
        connection = mysql.createConnection(dbConfig);
    let balance_query = 'SELECT report_year, ' + balance_fields.join() + ' FROM balance_table WHERE stock_symbol ="' + symbol + '" AND report_type="annual" AND report_year IN (' + compare_years.join() + '); ',
        income_query = 'SELECT report_year, ' + income_fields.join() + ' FROM income_sheet_table WHERE stock_symbol ="' + symbol + '" AND report_type="annual" AND report_year IN (' + compare_years.join() + '); ',
        cash_query = 'SELECT report_year, ' + cash_fields.join() + ' FROM cash_flow_table WHERE stock_symbol ="' + symbol + '" AND report_type="annual" AND report_year IN (' + compare_years.join() + ');';


    connection.query(balance_query + income_query + cash_query, (err, ret) => {
        if (err) {
            console.log(err);
        } else {
            const balance_table_data = ret[0],
                income_table_data = ret[1],
                cash_table_data = ret[2];

            console.log(balance_table_data);
            console.log(income_table_data);
            console.log(cash_table_data);

        }
        connection.end();
    });

    return res.send('{"code":1,"msg":"success"}');
});

app.listen(port, () => console.log(`server listening at portt:${port}`));