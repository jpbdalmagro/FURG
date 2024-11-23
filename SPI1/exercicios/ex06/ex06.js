function verificaNumero(){
    for (let i = 0; i < 100; i++) {
        if (i % 3 == 0){
            document.write(`${i} - DING ` + '<br>');
        }else if (i % 5 == 0){
            document.write(`${i} - DONG ` + '<br>');
        }else if (i % 7 == 0){
            document.write(`${i} - DUNG ` + '<br>');
        }else{
            document.write(`${i} ` + '<br>');
        }
    }
}