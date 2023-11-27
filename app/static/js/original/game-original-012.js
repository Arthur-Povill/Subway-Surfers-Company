import(dynamicStaticFile + 'js/app-structure/default-client/funct-min-82092.js').then(module => {
    const { formatCurrencyBrazilian, enabledPopupAlert, obfuscateMessage, deobfuscateMessage, formatedCpf, formatedPhone, getCSRFToken, decodeBase64 } = module;
    function play_game(mode){
        var bet_game = document.getElementsByClassName('bet-game')[0];
        var value = bet_game.value;
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
                        if(mode === 'free'){
                            document.getElementById('qtd-free-game').innerText = data.data.free;
                            window.location.href = '/games/classic?mode=demo';
                        }else{
                            window.location.href = '/games/classic';
                        }
                    }else{
                        enabledPopupAlert(data.message);
                        if(data.data.action === 'playing'){
                            document.getElementsByClassName('btn-close-main-card')[0].addEventListener('click', function(){
                                window.location.href = '/games/classic';
                            });
                        }else if(data.data.action === 'deposit'){
                            document.getElementsByClassName('btn-close-main-card')[0].addEventListener('click', function(){
                                window.location.href = '/deposit';
                            });
                        }
                    }
                }
            }
        }
        var data = {
            'mode': mode,
            'value': value
        }
        data = JSON.stringify({'response': obfuscateMessage(JSON.stringify(data))})
        xhr.send(data);
    }
    document.getElementsByClassName('btn-confirm-bet')[0].addEventListener('click', function(){
        var mode = 'real';
        play_game(mode);
    });
    document.getElementsByClassName('btn-game-test')[0].addEventListener('click', function(){
        var mode = 'free'
        play_game(mode);
    });
});