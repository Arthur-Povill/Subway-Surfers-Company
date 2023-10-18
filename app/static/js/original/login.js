import(dynamicStaticFile + 'js/app-structure/default-client/funct-min-82092.js').then(module => {
    const { obfuscateMessage, deobfuscateMessage, getCSRFToken, enabledPopupAlert, enabledLoad, disabledLoad, encodedBase64, decodeBase64, saveDataStorage, loadDataStorage } = module;
    function actionButtonSignin(){
        let email = document.getElementsByClassName('email-login')[0].value
        let password = document.getElementsByClassName('password-login')[0].value
        if(email !== ''){
            if(password !== ''){
                let xhr = new XMLHttpRequest();
                xhr.open('POST', '/api/v1/signin', true);
                const csrfToken = getCSRFToken();
                if (csrfToken) {
                    xhr.setRequestHeader("X-CSRFToken", csrfToken);
                }
                xhr.setRequestHeader('Content-Type', 'application/json');
                let data = {
                    'email': email,
                    'password': password
                }
                let data_obfuscated = JSON.stringify({'response': obfuscateMessage(JSON.stringify(data))})
                xhr.send(data_obfuscated);
                xhr.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        var response = JSON.parse(this.response);
                        var response_decrypted = deobfuscateMessage(response.response);
                        var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                        let data = JSON.parse(jsonStringFormated);
                        if(data.status_boolean === true){
                            window.location.href = '/';
                        }else{
                            var alert_message = data.message;
                            enabledPopupAlert(alert_message);
                        }
                    }
                }
            }else{
                enabledPopupAlert('Preencha o campo senha!');
            }
        }else{
            enabledPopupAlert('Preencha o campo email!');
        }
    }
    
    document.getElementsByClassName('button-signin')[0].addEventListener('click', actionButtonSignin);
});