import(dynamicStaticFile + 'js/app-structure/default-client/funct-min-82092.js').then(module => {
    const { obfuscateMessage, deobfuscateMessage, getCSRFToken, enabledPopupAlert, enabledLoad, disabledLoad, encodedBase64, decodeBase64, saveDataStorage, loadDataStorage } = module;
    document.getElementsByClassName('btn-recovery')[0].addEventListener('click', function(){
        var email = document.getElementById('email').value;
        if(email !== ''){
            if(email.includes('@')){
                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/api/v1/recovery', true);
                const csrfToken = getCSRFToken();
                if (csrfToken) {
                    xhr.setRequestHeader("X-CSRFToken", csrfToken);
                }
                xhr.setRequestHeader('Content-Type', 'application/json');
                var data = {
                    'email': email
                }
                var data_obfuscated = JSON.stringify({'response': obfuscateMessage(JSON.stringify(data))})
                xhr.send(data_obfuscated);
                xhr.onreadystatechange = function(){
                    if(xhr.readyState === 4 && xhr.status === 200){
                        var response = JSON.parse(this.response);
                        var response_decrypted = deobfuscateMessage(response.response);
                        var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                        var data = JSON.parse(jsonStringFormated);
                        if(data.status_boolean === true){ 
                            enabledPopupAlert(data.message, 'correct.png');
                            document.getElementsByClassName('btn-close-main-card')[0].addEventListener('click', function(){
                                window.location.href = '/auth/login';
                            });
                        }else{
                            enabledPopupAlert(data.message);
                        }
                    }
                }
            }else{
                enabledPopupAlert('Preencha o campo email corretamente!');
            }
        }else{  
            enabledPopupAlert('Preencha o campo email!');
        }
    });
});