function verifica(){
    let cod= parseInt(document.getElementById('idCod').value);

        if (cod > 0 && cod <=5){
            document.getElementById('idResp').value = "O codigo está entre 1 e 5"
            
        }
        else if (cod > 5 && cod <=10){
            document.getElementById('idResp').value = "O codigo está entre 6 e 10"
        }
        else if (cod > 10 && cod <=15){
            document.getElementById('idResp').value = "O codigo está entre 11 e 15"
        }
        else {
            document.getElementById('idResp').value = "Não está em intervalo"
        }


}   
