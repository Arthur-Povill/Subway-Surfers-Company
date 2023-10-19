function getCSRFToken() {
    const name = 'csrftoken=';
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(';');

    for (let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i].trim();
        if (cookie.indexOf(name) === 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }
    return null;
}

function enabledPopupAlert(alertMessage, alertLink=''){
    if(alertLink !== '' && alertLink !== null && alertLink !== undefined){
        document.getElementById('alert-main-error-img').setAttribute('src', '/static/image/app-structure/alerts/' + alertLink);
    }else if(alertLink === null || alertLink === undefined){
        document.getElementById('alert-main-error-img').style.display = 'none';
    }
    document.getElementById('alert-main-error-message').innerText = alertMessage;
    document.getElementsByClassName('alert-main')[0].style.display = 'flex';
}


document.getElementsByClassName('btn-confirm-update')[0].addEventListener('click', function() {
    var app_name = document.getElementById('app-name').value;
    var app_name_separated = document.getElementById('app-name-separated').value;
    var app_email = document.getElementById('app-email').value;
    var support_link = document.getElementById('support-link').value;
    var copy_get_phone = document.getElementById('copy-get-phone').value;
    var permited_deposit = document.getElementById('permited-deposit').value;
    var permited_withdraw = document.getElementById('permited-withdraw').value;
    var link_support_affiliates = document.getElementById('link-support-affiliates').value;
    var link_group = document.getElementById('link-group').value;
    if(app_name !== ''){
        if(app_name_separated !== ''){
            if(app_email !== ''){
                if(support_link !== ''){
                    if(link_support_affiliates !== ''){
                        if(link_group !== ''){
                            if(copy_get_phone !== ''){
                                if(permited_deposit !== ''){
                                    if(permited_withdraw !== ''){
                                        var xhr = new XMLHttpRequest();
                                        xhr.open('POST', '/panel/api/configs/update', true);
                                        const csrfToken = getCSRFToken();
                                        if (csrfToken) {
                                            xhr.setRequestHeader("X-CSRFToken", csrfToken);
                                        }
                                        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                                        xhr.onload = function() {
                                            if (xhr.status === 200) {
                                                var response = JSON.parse(xhr.responseText);
                                                if(response['status'] === 200){
                                                    enabledPopupAlert(response.message, 'correct.png');
                                                }else{
                                                    enabledPopupAlert(response.message);
                                                }
                                            }else{
                                                enabledPopupAlert('Erro ao atualizar as configurações.');
                                            }
                                        };
                                        var data = {
                                            'app_name': app_name,
                                            'app_name_separated': app_name_separated,
                                            'app_email': app_email,
                                            'support_link': support_link,
                                            'link_support_affiliates': link_support_affiliates,
                                            'link_group': link_group,
                                            'copy_get_phone': copy_get_phone,
                                            'permited_deposit': permited_deposit,
                                            'permited_withdraw': permited_withdraw
                                        }
                                        xhr.send(JSON.stringify(data));
                                    }else{
                                        enabledPopupAlert('O campo "Permitir saque" não pode ser vazio.');
                                    }
                                }else{
                                    enabledPopupAlert('O campo "Permitir depósito" não pode ser vazio.');
                                }
                            }else{
                                enabledPopupAlert('O campo "Copiar telefone" não pode ser vazio.');
                            }
                        }else{
                            enabledPopupAlert('O campo "Link do grupo" não pode ser vazio.');
                        }
                    }else{
                        enabledPopupAlert('O campo "Link de suporte afiliados" não pode ser vazio.');
                    }
                }else{
                    enabledPopupAlert('O campo "Link de suporte" não pode ser vazio.');
                }
            }else{
                enabledPopupAlert('O campo "E-mail" não pode ser vazio.');
            }
        }else{
            enabledPopupAlert('O campo "Nome separado" não pode ser vazio.');
        }
    }else{
        enabledPopupAlert('O campo "Nome do aplicativo" não pode ser vazio.');
    }

});