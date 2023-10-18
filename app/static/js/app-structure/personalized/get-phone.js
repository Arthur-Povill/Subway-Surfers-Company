import(dynamicStaticFile + 'js/app-structure/default-client/funct-min-82092.js').then(module => {
    const { formatedPhone, obfuscateMessage, deobfuscateMessage, getCSRFToken, enabledPopupAlert, enabledLoad, disabledLoad, encodedBase64, decodeBase64, saveDataStorage, loadDataStorage } = module;

    document.getElementsByClassName('btn-confim-phone')[0].addEventListener('click', function() {
        var phone = document.getElementById('phone').value;
        if(phone !== ''){
            let xhr = new XMLHttpRequest();
            xhr.open('POST', '/api/v1/my/profile/update/phone', true);
            const csrfToken = getCSRFToken();
            if (csrfToken) {
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            }
            xhr.setRequestHeader('Content-Type', 'application/json');
            let data = {
                'phone': phone
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
                        var url = window.location.href;
                        if(url.includes('/deposit/')){
                            var container_popup_phone = document.getElementsByClassName('container-popup-phone')[0];
                            container_popup_phone.style.display = 'none';
                            document.body.style.height = 'fit-content';
                            document.body.style.overflow = 'auto';
                        }else{
                            window.location.href = '/deposit/';
                        }
                    }else{var alert_message = data.message;
                        enabledPopupAlert(alert_message);
                    }
                }
            }
        }else{
            enabledPopupAlert('Preencha o campo de telefone');
        }
    });

    document.getElementById('phone').addEventListener('keypress', function(e) {
        var value = this.value;
        var value_formated = formatedPhone(value);
        this.value = value_formated;
    });

    //block scroll in body
    document.body.style.height = '100vh';
    document.body.style.position = 'relative';
    document.body.style.overflow = 'hidden';
});
