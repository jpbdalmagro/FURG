function teste() {
    const regexp = /^[+-]?[0-9]+(\.[0-9]+)?$/;

    let num = document.getElementById("input").value;

    if (regexp.test(num))
        alert("Você digitou um número real")
    else{
        alert("Você não digitou um número")
    }
}
