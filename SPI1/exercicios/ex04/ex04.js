function getMinMax(){
    let maior, menor;
    for (let i = 0; i < 5; i++){
        var n = prompt("Digite um número: ");
        n = parseInt(n);
        
        if (i == 0){
            maior = n;
            menor = n;
        } else {
            if (n > maior){
                maior = n;
            } else if (n < menor){
                menor = n;
            }
        }
    }
    alert(`Maior: ${maior}\nMenor: ${menor}`);
}