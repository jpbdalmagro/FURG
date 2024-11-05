function media(){
    var n1, n2, n3, n4, media
    
    n1 = parseInt(document.getElementById('n1').value);
    n2 = parseInt(document.getElementById('n2').value);
    n3 = parseInt(document.getElementById('n3').value);
    n4 = parseInt(document.getElementById('n4').value);

    media = (n1 + n2 + n3 + n4) / 4;

    if(media >= 7){
        alert("Aprovado");
    }else if (media >= 5){
        alert("Exame");
    }else{
        alert("Reprovado");
    }
}