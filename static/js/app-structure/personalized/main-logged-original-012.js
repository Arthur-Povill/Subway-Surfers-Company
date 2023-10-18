import(dynamicStaticFile + 'js/app-structure/default-client/funct-min-82092.js').then(module => {
    const { formatCurrencyBrazilian, enabledPopupAlert, obfuscateMessage, deobfuscateMessage, formatedCpf, formatedPhone, getCSRFToken, decodeBase64 } = module;
  
    document.addEventListener("DOMContentLoaded", function () {
        setFunctionDeposit();
        setFunctionDefault();
    });
    
    function setFunctionDeposit(){
        if (document.getElementsByClassName("btn-fast-value").length > 0) {
            var btn_values = document.getElementsByClassName("btn-fast-value");
            for (var i = 0; i < btn_values.length; i++) {
                btn_values[i].addEventListener("click", function () {
                    var input_value = document.getElementById("value-deposit");
                    var number_input = parseFloat(input_value.value.replace(",", "."));
                    var span = this.getElementsByTagName("span")[0].innerHTML
                    var number = span.replace("R$ ", "");
                    var value = parseFloat(number);
                    var result = number_input + value;
                    var formated_result = formatCurrencyBrazilian(result);
                    console.log(formated_result)
                    input_value.value = formated_result.replace('R$', '');
                });
            }
    
            document.getElementsByClassName('btn-confirm-deposit')[0].addEventListener('click', function(){
                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/api/v1/deposit/new');
                xhr.setRequestHeader('X-CSRFToken', getCSRFToken());
                xhr.setRequestHeader('Content-Type', 'application/json');
                xhr.onload = function(){
                    if(xhr.status === 200){
                        var response = JSON.parse(this.response);
                        var response_decrypted = deobfuscateMessage(response.response);
                        var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                        let data = JSON.parse(jsonStringFormated);
                        if(data.status_boolean === true){
                            document.getElementById('pix-code').src = data.data.qr_code;
                            document.getElementById('you-pay').innerText = data.data.value;
                            document.getElementById('copy-pix-code').value = data.data.pix_code;
                            var deposit_card_container = document.getElementsByClassName('deposit-card-container')[0];
                            deposit_card_container.style.right = '100%';
                        }else{
                            enabledPopupAlert(data.message);
                        }
                    }
                };
                var data = {
                    'value': document.getElementById('value-deposit').value
                }
                data = JSON.stringify({'response': obfuscateMessage(JSON.stringify(data))})
                xhr.send(data);
            });
    
            document.getElementsByClassName('btn-back-deposit')[0].addEventListener('click', function(){
                var deposit_card_container = document.getElementsByClassName('deposit-card-container')[0];
                deposit_card_container.style.right = '0';
            });
        }else{
            setTimeout(setFunctiosDeposit, 1000);
        }
    }
    
    function setFunctionDefault(){
        var btns_close = document.getElementsByClassName('btn-close-popup');
        for(var i = 0; i < btns_close.length; i++){
            btns_close[i].addEventListener('click', function(){
                var date_type_class = this.getAttribute('data-type');
                var element = document.getElementsByClassName(date_type_class)[0];
                var father = element.parentElement;
                father.style.display = 'none';
            });
        }
    
        var btn_copy = document.getElementsByClassName('btn-copy');
        for(var i = 0; i < btn_copy.length; i++){
            btn_copy[i].addEventListener('click', function(){
                var date_type_class = this.getAttribute('data-type');
                var element = document.getElementById(date_type_class);
                element.select();
                document.execCommand('copy');
                enabledPopupAlert('Dados copiado com sucesso! Você já pode colar em outro aplicativo/plataforma!', 'correct.png');
            });
        }
        var cpf = document.getElementById('cpf');
        cpf.value = formatedCpf(cpf.value);
    }
    
    var flip_button = document.getElementsByClassName('flip-button');
    for(var i = 0; i < flip_button.length; i++){
        flip_button[i].addEventListener('click', function(){
            var bet_game = document.getElementById('bet-game');
            var operation = this.getAttribute('data-operation');
            var value = parseFloat(bet_game.value.replace(',', '.'));
            if(operation === 'less'){
                var calculation = value - 1;
            }else if(operation === 'more'){
                var calculation = value + 1;
            }else{
                var calculation = value * 2;
            }
    
            if(calculation < 0){
                calculation = 0;
            }
            bet_game.value = formatCurrencyBrazilian(calculation).replace('R$', '');
        });
    }
    
    document.getElementById('bet-game').addEventListener('change', function(){
        var value = this.value;
        if(value !== ''){
            var value = value.replace(',', '.');
            var value = parseFloat(value);
            if(value < 0){
                value = 0;
            }
        }else{
            value = 0;
        }
        this.value = formatCurrencyBrazilian(value).replace('R$', '');
    
    });
    
    var game_modes = document.getElementsByClassName('games-modes');
    for(var i = 0; i < game_modes.length; i++){
        game_modes[i].addEventListener('click', function(){
            var selected_mode = document.getElementsByClassName('selected-mode')[0];
            selected_mode.classList.remove('selected-mode');
            this.classList.add('selected-mode');
        });
    }
    
    document.getElementsByClassName('btn-confirm-bet')[0].addEventListener('click', function(){
        var selected_mode = document.getElementsByClassName('selected-mode')[0];
        var data_mode = selected_mode.getAttribute('data-mode');
        var bet_game = document.getElementById('bet-game');
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
