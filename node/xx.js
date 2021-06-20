for (let i in r.data.items){
    if(r.data.items[i].quote.pe_ttm<=30){
        a.push(r.data.items[i].quote.symbol)
    }
}