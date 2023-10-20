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
        document.getElementById('alert-main-error-img').setAttribute('src', dynamicStaticFile + 'image/app-structure/alerts/' + alertLink);
    }else if(alertLink === null || alertLink === undefined){
        document.getElementById('alert-main-error-img').style.display = 'none';
    }
    document.getElementById('alert-main-error-message').innerText = alertMessage;
    document.getElementsByClassName('alert-main')[0].style.display = 'flex';
}


document.getElementsByClassName('btn-confirm-update')[0].addEventListener('click', function() {
    var inputs_configs_application = document.getElementsByClassName('input-configs-application');
    var dict_config = {};
    for(var i = 0; i < inputs_configs_application.length; i++){
        var input = inputs_configs_application[i];
        var name = input.getAttribute('id').replaceAll('-', '_');
        var value = input.value;
        if(value !== ''){
            dict_config[name] = value;
        }else{
            var father = input.parentNode.parentNode;
            var input_title = father.getElementsByClassName('input-title')[0];
            var span_title = input_title.getElementsByTagName('span')[0];
            var name_field = span_title.innerText;
            enabledPopupAlert('O campo "' + name_field + '" não pode ser vazio.');
            return;
        }

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
        xhr.send(JSON.stringify(dict_config));
    }
});