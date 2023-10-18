import(dynamicStaticFile + 'js/app-structure/default-client/funct-min-82092.js').then(module => {
    const { obfuscateMessage, deobfuscateMessage, getCSRFToken, enabledPopupAlert, enabledLoad, disabledLoad, encodedBase64, decodeBase64, saveDataStorage, loadDataStorage } = module;

    function actionButtonSignup(){
        let email = document.getElementsByClassName('email-signup')[0].value
        let password = document.getElementsByClassName('password-signup')[0].value
        let password_confirm = document.getElementsByClassName('confirm-password')[0].value
        if(email !== ''){
            if(email.includes('@') || email.includes('.')){
                if(password !== ''){
                    if(password_confirm !== ''){
                        if(password === password_confirm){
                            let xhr = new XMLHttpRequest();
                            xhr.open('POST', '/api/v1/signup', true);
                            const csrfToken = getCSRFToken();
                            if (csrfToken) {
                                xhr.setRequestHeader("X-CSRFToken", csrfToken);
                            }
                            xhr.setRequestHeader('Content-Type', 'application/json');
                            let data = {
                                'full_name': '',
                                'cpf': '',
                                'phone': '',
                                'email': email,
                                'password': password,
                                'after_signup': true,
                                'other': true
                            }
                            let data_obfuscated = JSON.stringify({'response': obfuscateMessage(JSON.stringify(data))})
                            xhr.send(data_obfuscated);
                            xhr.onreadystatechange = function(){
                                if(xhr.readyState === 4 && xhr.status === 200){
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
                            enabledPopupAlert('As senhas não coincidem!');
                        }
                    }else{
                        enabledPopupAlert('Preencha o campo confirmar senha!');
                    }
                }else{
                    enabledPopupAlert('Preencha o campo senha!');
                }
            }else{
                enabledPopupAlert('Preencha o campo email corretamente!');
            }
        }else{
            enabledPopupAlert('Preencha o campo email!');
        }
    }

    document.getElementsByClassName('button-signup')[0].addEventListener('click', actionButtonSignup);
});