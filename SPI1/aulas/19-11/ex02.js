function validaNum(){
    const regexp = /^(\(?[1-9]{2}\)?)\s?([2-9][0-9]{3,4})-?([0-9]{4})$/;

    var num = document.getElementById("tel").value;

    if (regexp.test(num)){
        alert(`${num} é um número de telefone válido!`); 
    }else{
        alert(`${num} não é um número de telefone válido!`);
    }
}