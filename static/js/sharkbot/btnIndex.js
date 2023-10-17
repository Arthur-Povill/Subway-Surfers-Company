import { obfuscateMessage, deobfuscateMessage, getCSRFToken, enabledPopupAlert, enabledLoad, disabledLoad, encodedBase64, decodeBase64, saveDataStorage, loadDataStorage } from './funct.js';

function setClickedInGame(){
    let allContainersGame = document.querySelectorAll('.container-game');
    for(let i=0; i<allContainersGame.length; i++){
        allContainersGame[i].addEventListener('click', function(){
            enabledLoad();
            let elementTarget = this;
            let iframeBetHouse = document.querySelector('#iframe-bet-house');
            let inGameNow = iframeBetHouse.getAttribute('data-game-name');
            let nameGame = this.getAttribute('data-name');
            let betName = iframeBetHouse.getAttribute('data-bet-name');
            if(inGameNow !== nameGame){
                let blockedGame = document.querySelector('#' + nameGame + '-blocked');
                let permitedGame = blockedGame.getAttribute('data-id') === 'true';
                if(permitedGame){
                    var xmlhttp = new XMLHttpRequest();
                    xmlhttp.open("POST", "api/verify/game", true);
                    const csrfToken = getCSRFToken();
                    if (csrfToken) {
                        xmlhttp.setRequestHeader("X-CSRFToken", csrfToken);
                    }
                    xmlhttp.onreadystatechange = function() {
                        if (this.readyState == 4 && this.status == 200) {
                            var response = JSON.parse(this.response);
                            var response_decrypted = deobfuscateMessage(response.response);
                            var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                            let data = JSON.parse(jsonStringFormated);
                            disabledLoad();
                            if(data.status === 200){
                                let maintenance = data['containers']['maintenance'] === 'true';
                                if(maintenance === false){
                                    let input = elementTarget.querySelector('#' + nameGame + '-link-game');
                                    let linkGame = input.value;
                                    iframeBetHouse.setAttribute('src', linkGame);
                                    iframeBetHouse.setAttribute('data-game-name', nameGame);
                                    document.querySelector('#game-clicked').value = linkGame;

                                    let menuConfiguration = document.querySelector('.menu-configuration');
                                    menuConfiguration.style.left = '0';
                                    let searchEngine = document.querySelector('.search-engine');
                                    searchEngine.style.display = 'none';
                                    let btnPower = document.querySelector('#menu-main-power');
                                    btnPower.style.display = 'flex';
                                    
                                    let base64Template = data['containers']['template'];
                                    const originalTemplate = decodeBase64(base64Template);
                                    let template = originalTemplate;
                                    let mainRight = document.getElementsByClassName('card-menu-auto')[0];
                                    mainRight.innerHTML = template;
                                    
                                    changeConfigurationMenu();

                                }else{
                                    enabledPopupAlert('Jogo em manutenção! Aguarde o término.');
                                }
                            }else{
                                enabledPopupAlert(data.message);
                            }
                        }
                    }
                    let data = JSON.stringify({'game': nameGame, 'bet': betName});
                    xmlhttp.send(JSON.stringify({'response': obfuscateMessage(data)}));
                }else{
                    let statusBlocked = blockedGame.getAttribute('data-status');
                    if(statusBlocked === 'maintenance'){
                        enabledPopupAlert('Jogo em manutenção! Aguarde o término.');
                    }else{
                        enabledPopupAlert('Você não possui acesso ao jogo! Adquira a licença em nossa loja.');
                    }
                }
            }else{
                enabledPopupAlert('Este jogo já está sendo executado!');
            }
        });
    }
}

function setFunctionsInMenu(){
    document.getElementById('menu-main-power').addEventListener('click', function(){
        let iframeBetHouse = document.querySelector('#iframe-bet-house');
        let inGameNow = iframeBetHouse.getAttribute('data-game-name');
        if(inGameNow !== ''){
            let classes = this.getAttribute('class');
            let powerDescription = this.querySelector('.menu-main-power-container');
            if(classes.includes('bot-off')){
                this.classList.remove('bot-off');
                this.classList.add('bot-on');
                this.setAttribute('data-status-bot', 'true')
                powerDescription.innerText = 'Ligado';
            }else{
                this.classList.remove('bot-on');
                this.classList.add('bot-off');
                this.setAttribute('data-status-bot', 'false')
                powerDescription.innerText = 'Desligado';
            }
        }else{
            enabledPopupAlert('Selecione um jogo para executar o bot!');
        }
    })
    document.getElementById('back-games').addEventListener('click', function(){
        let menuConfiguration = document.querySelector('.menu-configuration');
        menuConfiguration.style.left = '-100%';
        let searchEngine = document.querySelector('.search-engine');
        searchEngine.style.display = 'flex';
        let btnPower = document.querySelector('#menu-main-power');
        btnPower.style.display = 'none';
        let iframeBetHouse = document.querySelector('#iframe-bet-house');
        iframeBetHouse.setAttribute('data-game-name', '');
        let betNameDev = iframeBetHouse.getAttribute('data-bet-name-dev'); 
        iframeBetHouse.setAttribute('src', document.querySelector('#' + betNameDev + ' .input-not-show').innerText);
    })
    document.getElementById('restart-menu').addEventListener('click', function(){
        let iframeBetHouse = document.querySelector('#iframe-bet-house');
        let src = iframeBetHouse.getAttribute('src');
        iframeBetHouse.setAttribute('src', src);
    });
    document.getElementById('configuration-more-menu').addEventListener('click', function(){
        let menuConfiguration = document.querySelector('.menu-more');
        menuConfiguration.style.display = 'flex';
    })
    document.getElementsByClassName('container-close-menu')[0].addEventListener('click', function(){
        let menuConfiguration = document.querySelector('.menu-more');
        menuConfiguration.style.display = 'none';

    })
}

function changeConfigurationMenu(){
    let iframe = document.querySelector('#iframe-bet-house');
    let betName = iframe.getAttribute('data-bet-name');
    let gameName = iframe.getAttribute('data-game-name');
    let dataStorage = loadDataStorage(gameName);
    if(dataStorage.status){
        let data = dataStorage.data;
        let inputsConfiguration = document.querySelectorAll('.menu-input-funct-settings');
        for(let i=0; i<inputsConfiguration.length; i++){
            let key = inputsConfiguration[i].getAttribute('id');
            let value = data[key];
            inputsConfiguration[i].value = value;
        }
        if(data['status-bot']){
            let btnPower = document.querySelector('#menu-main-power');
            btnPower.classList.remove('bot-off');
            btnPower.classList.add('bot-on');
            btnPower.setAttribute('data-status-bot', 'true')
            let powerDescription = btnPower.querySelector('.menu-main-power-container');
            powerDescription.innerText = 'Ligado';
        }
    }

    let inputsConfiguration = document.querySelectorAll('.menu-input-funct-settings');
    for(let i=0; i<inputsConfiguration.length; i++){
        inputsConfiguration[i].addEventListener('change', configMenu)
    }

    document.getElementById('menu-main-power').addEventListener('click', configMenu)
}

function configMenu(){
    let inputsConfiguration = document.querySelectorAll('.menu-input-funct-settings');
    let iframe = document.querySelector('#iframe-bet-house');
    let betName = iframe.getAttribute('data-bet-name');
    let gameName = iframe.getAttribute('data-game-name');
    var data = {};
    for(let i=0; i<inputsConfiguration.length; i++){
        let key = inputsConfiguration[i].getAttribute('id');
        let value = inputsConfiguration[i].value;
        data[key] = value;
    }
    let btnPower = document.querySelector('#menu-main-power');
    let statusBot = btnPower.getAttribute('data-status-bot') === 'true';
    data['status-bot'] = statusBot;
    saveDataStorage(gameName, data);
}

let btnsBetHouse = document.querySelectorAll('.container-img-bet');
for(let i=0; i<btnsBetHouse.length; i++){
    let bet_name = btnsBetHouse[i].getAttribute('id');
    let blockedBet = document.querySelector('#' + bet_name + '-blocked');
    let permited = blockedBet.getAttribute('data-id') === 'true';
    if(permited){
        btnsBetHouse[i].addEventListener('click', function(){
            enabledLoad();
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.open("POST", "api/verify_bets", true);
            const csrfToken = getCSRFToken();
            if (csrfToken) {
                xmlhttp.setRequestHeader("X-CSRFToken", csrfToken);
            }

            xmlhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    var response = JSON.parse(this.response);
                    var response_decrypted = deobfuscateMessage(response.response);
                    var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                    let data = JSON.parse(jsonStringFormated);
                    disabledLoad();
                    if(data.status === 200){
                        let base64Template = data['containers']['template'];
                        const originalTemplate = decodeBase64(base64Template);
                        let template = originalTemplate;
                        let mainRight = document.getElementsByClassName('main-right')[0];
                        mainRight.innerHTML = template;
                        
                        let inputSearchGames = document.querySelector('#input-search-games');
                        inputSearchGames.addEventListener('keyup', function(){
                            let iframeBetHouse = document.querySelector('#iframe-bet-house');
                            let betName = iframeBetHouse.getAttribute('data-bet-name');
                            let game_name = this.value;
                            var xmlhttp = new XMLHttpRequest();
                            xmlhttp.open("POST", "api/search/game", true);
                            const csrfToken = getCSRFToken();
                            if (csrfToken) {
                                xmlhttp.setRequestHeader("X-CSRFToken", csrfToken);
                            }
                            xmlhttp.onreadystatechange = function() {
                                var response = JSON.parse(this.response);
                                var response_decrypted = deobfuscateMessage(response.response);
                                var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                                let data = JSON.parse(jsonStringFormated);
                                disabledLoad();
                                if(data.status === 200){
                                    let base64Template = data['containers']['template'];
                                    const originalTemplate = decodeBase64(base64Template);
                                    let template = originalTemplate;
                                    let containerGames = document.querySelector('.results-container-auto');
                                    containerGames.innerHTML = template;
                                    setClickedInGame();
                                    setFunctionsInMenu();
                                }
                            }
                            let data = JSON.stringify({'game': game_name, 'bet': betName});
                            xmlhttp.send(JSON.stringify({'response': obfuscateMessage(data)}));

                        });
                        setClickedInGame();
                        setFunctionsInMenu();
                    }else{
                        enabledPopupAlert(data.message);
                    }               
                }else{
                    enabledPopupAlert('Erro ao realizar chamada! Entre em contato com o suporte.')
                } 
            };
            let data = JSON.stringify({'bet': bet_name, 
        });
            xmlhttp.send(JSON.stringify({'response': obfuscateMessage(data)}));
        })
    }else{
        btnsBetHouse[i].addEventListener('click', function(){
            let statusBlocked = blockedBet.getAttribute('data-status');
            if(statusBlocked === 'maintenance'){
                enabledPopupAlert('Jogo em manutenção! Aguarde o término.');
            }else{
                enabledPopupAlert('Você não possui acesso a essa casa de aposta! Adquira a licença em nossa loja.');
            }
        })
    }
}