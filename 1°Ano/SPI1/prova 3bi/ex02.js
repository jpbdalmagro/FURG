function validaNome(){
    regexp = /^[a-zA-Z]+$/;
    var nome = document.getElementById("nome").value;

    if (regexp.test(nome))
        document.getElementById("nome").value = nome.toUpperCase();
    else{
        alert("Nome Inválido! Apenas letras são permitidas.");
    }
}

function validaIdade(){
    regexp = /^(?:1[01][0-9]|120|[1-9]?[0-9])$/;
    var idade = document.getElementById("idade").value;

    if (!regexp.test(idade))
        alert("Idade Inválida");
}


function validaSenha(){
    var senha = document.getElementById("senha").value;

    if (senha.length < 8){
        alert("Senha deve ter no mínimo 8 caracteres.");
    }
}

function confirmaSenha(){
    var senha = document.getElementById("senha").value;
    var confirmaSenha = document.getElementById("confirma").value;

    if (senha != confirmaSenha){
        alert("Senhas não conferem.");
    }
}