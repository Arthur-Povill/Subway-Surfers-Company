import(dynamicStaticFile + 'js/app-structure/default-client/funct-min-82092.js').then(module => {
    const { formatCurrencyBrazilian, enabledPopupAlert, obfuscateMessage, deobfuscateMessage, formatedCpf, formatedPhone, getCSRFToken, decodeBase64 } = module;
   document.getElementsByClassName('btn-confirm-bet')[0].addEventListener('click', function(){
        var data_mode = 'classic';
        var bet_game = document.getElementsByClassName('bet-game')[0];
        var value = bet_game.value;
    
        if(data_mode === 'lucky'){
            enabledPopupAlert('Em breve', 'correct.png');
            return false;
        }
    
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/api/v1/game/new');
        xhr.setRequestHeader('X-CSRFToken', getCSRFToken());
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = function(){
            if(xhr.status === 200){
                if(xhr.status === 200){
                    var response = JSON.parse(this.response);
                    var response_decrypted = deobfuscateMessage(response.response);
                    var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                    let data = JSON.parse(jsonStringFormated);
                    if(data.status_boolean === true){
                        window.location.href = '/games/'+ data_mode;
                    }else{
                        enabledPopupAlert(data.message);
                        if(data.data.action === 'playing'){
                            document.getElementsByClassName('btn-close-main-card')[0].addEventListener('click', function(){
                                window.location.href = '/games/'+ data_mode;
                            });
                        }else if(data.data.action === 'deposit'){
                            document.getElementsByClassName('btn-close-main-card')[0].addEventListener('click', function(){
                                document.getElementsByClassName('container-deposit')[0].style.display = 'flex';
                            });
                        }
                    }
                }
            }
        }
        var data = {
            'mode': data_mode,
            'value': value
        }
        data = JSON.stringify({'response': obfuscateMessage(JSON.stringify(data))})
        xhr.send(data);
    });
});