var dataAtual = new Date();

horas = dataAtual.getHours();

if(horas < 6 || horas > 18 ){
    greetings = "Boa Noite"
}else if(horas < 12){
    greetings = "Bom Dia"
}else{
    greetings = "Boa Tarde"
}
