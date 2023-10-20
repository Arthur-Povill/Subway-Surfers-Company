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
            xhr.open('POST', 'template/user/info', true);
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

                    var cpf_profile = document.getElementById('cpf-profile');
                    cpf_profile.value = formated_cpf(cpf_profile.value);
                    cpf_profile.addEventListener('keyup', function(){
                        this.value = formated_cpf(this.value);
                    });

                    var phone_profile = document.getElementById('phone-profile');
                    phone_profile.value = formated_phone(phone_profile.value);
                    phone_profile.addEventListener('keyup', function(){
                        this.value = formated_phone(this.value);
                    });

                    document.getElementsByClassName('container-close-card-user')[0].addEventListener('click', function(){
                        document.getElementsByClassName('container-card-user')[0].style.display = 'none';
                    });

                    document.getElementsByClassName('container-btn-confirm-update')[0].addEventListener('click', updateUser);
                }
            }
            var data = {
                'id_user': id
            }
            xhr.send(JSON.stringify(data));
        })
    }
    document.getElementsByClassName('count-users')[0].innerText = item_users.length;
    document.getElementsByClassName('count-users-deposited')[0].innerText = document.getElementsByClassName('user-deposisted').length;
}

function getUsers(query){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'template/users', true);
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

function updateUser(){
    var influender = document.getElementById('influencer-profile');
    var activated = document.getElementById('activated-profile');
    var id = document.getElementById('id-profile');
    var full_name = document.getElementById('full-name-profile');
    var email = document.getElementById('email-profile');
    var cpf = document.getElementById('cpf-profile');
    var phone = document.getElementById('phone-profile');
    var code_affiliate = document.getElementById('code-affiliate');
    var cpa_percent = document.getElementById('cpa-percent');
    var revshare_percent = document.getElementById('revshare-percent');
    var permited_balance = document.getElementById('permited-balance');
    var value_balance = document.getElementById('value-balance');

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'api/user/update', true);
    const csrfToken = getCSRFToken();
    if (csrfToken) {
        xhr.setRequestHeader("X-CSRFToken", csrfToken);
    }
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if(response['status'] === 200){
                var response = JSON.parse(xhr.responseText);
                enabledPopupAlert(response['message'], 'correct.png');
            }
        }
    }

    var data = {
        'id_user': id.value,
        'influencer': influender.classList.contains('green'),
        'activated': activated.classList.contains('green'),
        'full_name': full_name.value,
        'email': email.value,
        'cpf': cpf.value,
        'phone': phone.value,
        'code_affiliate': code_affiliate.value,
        'cpa_percent': cpa_percent.value,
        'revshare_percent': revshare_percent.value,
        'permited_withdraw': permited_balance.classList.contains('green'),
        'value_balance': value_balance.value,
    }
    xhr.send(JSON.stringify(data));

}

getUsers('');
document.getElementsByClassName('search-enginee')[0].addEventListener('keyup', function(){
    var query = this.value;
    getUsers(query);
})
