function formated_cpf(v){
    if(v != ''){
        v=v.replace(/\D/g,"");
        v=v.replace(/(\d{3})(\d)/,"$1.$2");
        v=v.replace(/(\d{3})(\d)/,"$1.$2");
        v=v.replace(/(\d{3})(\d{1,2})$/,"$1-$2");
    }
    return v; 
}

function formated_phone(v){
    if(v != ''){
        v=v.replace(/\D/g,"");
        v=v.replace(/(\d{2})(\d)/,"($1) $2");
        v=v.replace(/(\d{5})(\d)/,"$1-$2");
    }
    return v; 
}

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

function setClickedInUsers(){
    var item_users = document.getElementsByClassName('item-users');
    for (var i = 0; i < item_users.length; i++) {
        item_users[i].addEventListener('click', function(){
            var id = this.getElementsByClassName('id-user')[0].innerText;
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'template/affiliates/info', true);
            const csrfToken = getCSRFToken();
            if (csrfToken) {
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            }
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onload = function() {
                if (xhr.status === 200) {
                    var container_card_user = document.getElementsByClassName('container-card-user')[0];
                    container_card_user.innerHTML = xhr.responseText;
                    container_card_user.style.display = 'flex';

                    var input_container_status = document.getElementsByClassName('input-container-status');
                    for (var i = 0; i < input_container_status.length; i++) {
                        input_container_status[i].addEventListener('click', function(){
                            var div = this.getElementsByClassName('borded')[0];
                            var span = this.getElementsByTagName('span')[0];
                            if(div.classList.contains('green')){
                                div.classList.remove('green');
                                div.classList.add('red');
                                span.innerText = 'Desativado';
                            }else{
                                div.classList.remove('red');
                                div.classList.add('green');
                                span.innerText = 'Ativado';
                            }
                        })
                    }

                    document.getElementsByClassName('btn-close-affiliates')[0].addEventListener('click', function(){
                        document.getElementsByClassName('container-card-user')[0].style.display = 'none';
                    });
                }
            }
            var data = {
                'id_user': id
            }
            xhr.send(JSON.stringify(data));
        })
    }
    document.getElementsByClassName('count-users')[0].innerText = item_users.length;
}

function getUsers(query){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'template/affiliates', true);
    const csrfToken = getCSRFToken();
    if (csrfToken) {
        xhr.setRequestHeader("X-CSRFToken", csrfToken);
    }
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
            document.getElementsByClassName('bottom-side-content-container')[0].innerHTML = xhr.responseText;
            setClickedInUsers();
        }
    }
    var data = {
        'query': query
    }
    xhr.send(JSON.stringify(data));
}

getUsers('');
document.getElementsByClassName('search-enginee')[0].addEventListener('keyup', function(){
    var query = this.value;
    getUsers(query);
})
