import(dynamicStaticFile + 'js/app-structure/default-client/funct-min-82092.js').then(module => {
    const { obfuscateMessage, deobfuscateMessage, getCSRFToken, enabledPopupAlert, enabledLoad, disabledLoad, encodedBase64, decodeBase64, saveDataStorage, loadDataStorage } = module;

    document.getElementsByClassName('btn-confirm-withdraw')[0].addEventListener('click', function() {
        var value = document.getElementsByClassName('value-withdraw')[0].value;
        var name = document.getElementsByClassName('name-withdraw')[0].value;
        var cpf = document.getElementsByClassName('cpf-withdraw')[0].value;
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/api/v1/withdraw/new');
        xhr.setRequestHeader('X-CSRFToken', getCSRFToken());
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = function() {
            if(xhr.status === 200){
                var response = JSON.parse(this.response);
                var response_decrypted = deobfuscateMessage(response.response);
                var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                let data = JSON.parse(jsonStringFormated);
                if(data.status_boolean === true){
                    var message = data.message;
                    enabledPopupAlert(message, 'correct.png');
                }else{
                    enabledPopupAlert(data.message);
                }
            }
        }
        var data = {
            'value': value,
            'name': name,
            'cpf': cpf
        }
        data = JSON.stringify({'response': obfuscateMessage(JSON.stringify(data))})
        xhr.send(data);
    });
});