import(dynamicStaticFile + 'js/app-structure/default-client/funct-min-82092.js').then(module => {
    const { obfuscateMessage, deobfuscateMessage, getCSRFToken, enabledPopupAlert, enabledLoad, disabledLoad, encodedBase64, decodeBase64, saveDataStorage, loadDataStorage } = module;

    var btn_copy = document.getElementsByClassName('btn-copy');
    for(var i = 0; i < btn_copy.length; i++){
        btn_copy[i].addEventListener('click', function(){
            var date_type_class = this.getAttribute('data-type');
            var element = document.getElementById(date_type_class);
            const elem = document.createElement('textarea');
            elem.value = element.innerText;
            document.body.appendChild(elem);
            elem.select();
            document.execCommand('copy');
            document.body.removeChild(elem);
            enabledPopupAlert('Link copiado!', 'correct.png');
        });
    }
});