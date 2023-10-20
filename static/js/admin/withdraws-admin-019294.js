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

function changeStatus(id, status){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/panel/api/withdraw/update', true);
    const csrfToken = getCSRFToken();
    if (csrfToken) {
        xhr.setRequestHeader("X-CSRFToken", csrfToken);
    }
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if(response['status'] === 200){
                enabledPopupAlert(response['message'], 'correct.png');
                var query = document.getElementsByClassName('search-enginee')[0].value;
                getWithdraws(query);
                if(response['data']['status'] === 'approved'){
                    enabledPopupAlert('Saque aprovado com sucesso!', 'correct.png');
                    var element_father = this.parentElement.parentElement;
                    var father = element_father.parentElement.parentElement;
                    var element_status_value = father.getElementsByClassName('status-value')[0];
                    element_status_value.classList.remove('pendent');
                    element_status_value.classList.add('approved');
                    element_status_value.innerText = 'Aprovado';
                    element_father.innerHTML = '-';
                }else{
                    enabledPopupAlert(response.message, 'correct.png');
                }
            }
        }
    }
    var data = {
        'id': id,
        'status': status
    }
    xhr.send(JSON.stringify(data));
}

function setClickedBtnStatus(){
    var btn_approved = document.getElementsByClassName('btn-approved-yes');
    var btn_denied = document.getElementsByClassName('btn-approved-no');

    for(var i = 0; i < btn_approved.length; i++){
        btn_approved[i].addEventListener('click', function(){
            var id = this.getAttribute('data-id');
            changeStatus(id, 'approved');
        });
    }

    for(var i = 0; i < btn_denied.length; i++){
        btn_denied[i].addEventListener('click', function(){
            var id = this.getAttribute('data-id');
            changeStatus(id, 'canceled');
            var element_father = this.parentElement.parentElement;
            var father = element_father.parentElement;
            var element_status_value = father.getElementsByClassName('status-value')[0];
            element_status_value.classList.remove('pendent');
            element_status_value.classList.add('canceled');
            element_status_value.innerText = 'Negado';
            element_father.innerHTML = '-';
        });
    }
}

function getWithdraws(query){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'template/withdraws', true);
    const csrfToken = getCSRFToken();
    if (csrfToken) {
        xhr.setRequestHeader("X-CSRFToken", csrfToken);
    }
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
            document.getElementsByClassName('bottom-side-content-container')[0].innerHTML = xhr.responseText;
            setClickedBtnStatus();
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

var btn_filtered = document.getElementsByClassName('btn-filtered');
for(var i = 0; i < btn_filtered.length; i++){
    btn_filtered[i].addEventListener('click', function(){
        var element_selected = document.getElementsByClassName('btn-filtered-selected')[0];
        element_selected.classList.remove('btn-filtered-selected');
        this.classList.add('btn-filtered-selected');

        //get all item-users
        var text_lower = this.innerText.toLowerCase();
        var item_users = document.getElementsByClassName('item-users');
        for(var i = 0; i < item_users.length; i++){
            if(text_lower === 'todos'){
                item_users[i].style.display = 'flex';
            }else{
                var element_status = item_users[i].querySelector('.border-status span');
                var status = element_status.innerText.toLowerCase();
                if(text_lower === status){
                    item_users[i].style.display = 'flex';
                }else{
                    item_users[i].style.display = 'none';
                }
            }

        }

    })
}

getWithdraws('');
document.getElementsByClassName('search-enginee')[0].addEventListener('keyup', function(){
    var query = this.value;
    getWithdraws(query);
})
