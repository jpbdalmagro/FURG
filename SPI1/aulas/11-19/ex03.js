function nameUpper(){
    var name = document.getElementById("nome");

    name.value = name.value.toUpperCase();

}

function validData(){
    const regexp = /^[0-9]{8}$|^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$/

    var data = document.getElementById("data").value;

    if (!regexp.test(data)){
        alert("Data Inválida")
    }
}
