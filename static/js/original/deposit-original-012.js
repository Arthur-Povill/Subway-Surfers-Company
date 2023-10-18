import(dynamicStaticFile + 'js/app-structure/default-client/funct-min-82092.js').then(module => {
    const { obfuscateMessage, deobfuscateMessage, getCSRFToken, enabledPopupAlert, enabledLoad, disabledLoad, encodedBase64, decodeBase64, saveDataStorage, loadDataStorage } = module;

    document.getElementsByClassName('btn-confirm-deposit')[0].addEventListener('click', function(){
        var xhr = new XMLHttpRequest();
        var name = document.getElementsByName('depositFullName')[0].value;
        var cpf = document.getElementsByName('depositDocument')[0].value
        var value = document.getElementsByName('depositAmount')[0].value
        if(name !== ''){
            if(cpf !== ''){
                if(value !== ''){
                    document.getElementById("pixgenerator").textContent = "Aguarde, estamos gerando";
                    document.getElementById("pixgenerator").style.visibility = 'hidden';
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
                                var id_ = data.data.external_id;
                                window.location.href = '/deposit/'+id_;
                                deposit_card_container.style.right = '100%';
                            }else{
                                enabledPopupAlert(data.message);
                            }
                        }
                    };
                    var data = {
                        'name': name,
                        'cpf': cpf,
                        'value': value
                    }
                    data = JSON.stringify({'response': obfuscateMessage(JSON.stringify(data))})
                    xhr.send(data);
                }else{
                    enabledPopupAlert('Preencha o campo Valor');
                }
            }else{
                enabledPopupAlert('Preencha o campo CPF');
            }
        }else{
            enabledPopupAlert('Preencha o campo Nome Completo');
        }
    });
});