import(dynamicStaticFile + 'js/app-structure/default-client/funct-min-82092.js').then(module => {
    const { obfuscateMessage, deobfuscateMessage, getCSRFToken, enabledPopupAlert, enabledLoad, disabledLoad, encodedBase64, decodeBase64, saveDataStorage, loadDataStorage } = module;

    function actionButtonSignin(){
        let data_type = this.getAttribute('data-type');
        if(data_type === 'post'){
            let email = document.getElementById('email').value
            let password = document.getElementById('password').value
            if(email !== ''){
                if(password !== ''){
                    let xhr = new XMLHttpRequest();
                    xhr.open('POST', '/api/v1/signin', true);
                    const csrfToken = getCSRFToken();
                    if (csrfToken) {
                        xhr.setRequestHeader("X-CSRFToken", csrfToken);
                    }
                    xhr.setRequestHeader('Content-Type', 'application/json');
                    let data = {
                        'email': email,
                        'password': password
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
                                window.location.href = '/';
                            }else{
                                let card_signin = document.getElementsByClassName('card-signin')[0];
                                card_signin.querySelectorAll('.status-circle')[0].style.opacity = '1';
                                card_signin.querySelectorAll('.status-circle')[1].style.opacity = '1';
                                var alert_message = data.message;
                                enabledPopupAlert(alert_message);
                            }
                        }
                    }
                }else{
                    let card_signin = document.getElementsByClassName('card-signin')[0];
                    let status_circle = card_signin.querySelectorAll('.status-circle')[1]
                    status_circle.style.opacity = '1';
                    enabledPopupAlert('Preencha o campo senha!');
                }
            }else{
                let card_signin = document.getElementsByClassName('card-signin')[0];
                let status_circle = card_signin.querySelectorAll('.status-circle')[0]
                status_circle.style.opacity = '1';
                enabledPopupAlert('Preencha o campo email!');
            }
        }else{
            openMenuSignin();
        }
    }
    
    function actionButtonSignup(){
        let data_type = this.getAttribute('data-type');
        if(data_type === 'post'){
            let full_name = document.getElementById('full-name').value
            let cpf = document.getElementById('cpf').value
            let phone = document.getElementById('phone').value
            let email = document.getElementById('email-signup').value
            let password = document.getElementById('password-signup').value
            let password_confirm = document.getElementById('confirm-password').value
            if(full_name !== ''){
                if(cpf !== ''){
                    let formatted_cpf = cpf.replace('.', '').replace('.', '').replace('-', '');
                    if(formatted_cpf.length === 11){
                        cpf = formatted_cpf;
                        if(phone !== ''){
                            let formated_phone = phone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '');
                            if(formated_phone.length === 11){
                                phone = formated_phone;
                                if(email !== ''){
                                    if(email.includes('@') || email.includes('.')){
                                        if(password !== ''){
                                            if(password_confirm !== ''){
                                                if(password === password_confirm){
                                                    let xhr = new XMLHttpRequest();
                                                    xhr.open('POST', '/api/v1/signup', true);
                                                    const csrfToken = getCSRFToken();
                                                    if (csrfToken) {
                                                        xhr.setRequestHeader("X-CSRFToken", csrfToken);
                                                    }
                                                    xhr.setRequestHeader('Content-Type', 'application/json');
                                                    let data = {
                                                        'full_name': full_name,
                                                        'cpf': cpf,
                                                        'phone': phone,
                                                        'email': email,
                                                        'password': password,
                                                        'after_signup': true
                                                    }
                                                    let data_obfuscated = JSON.stringify({'response': obfuscateMessage(JSON.stringify(data))})
                                                    xhr.send(data_obfuscated);
                                                    xhr.onreadystatechange = function(){
                                                        if(xhr.readyState === 4 && xhr.status === 200){
                                                            var response = JSON.parse(this.response);
                                                            var response_decrypted = deobfuscateMessage(response.response);
                                                            var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                                                            let data = JSON.parse(jsonStringFormated);
                                                            if(data.status_boolean === true){
                                                                window.location.href = '/';
                                                            }else{
                                                                let card_signin = document.getElementsByClassName('card-signin')[0];
                                                                card_signin.querySelectorAll('.status-circle')[0].style.opacity = '1';
                                                                card_signin.querySelectorAll('.status-circle')[1].style.opacity = '1';
                                                                var alert_message = data.message;
                                                                enabledPopupAlert(alert_message);
                                                            }
                                                        }
                                                    }
                                                }else{
                                                    let card_signup = document.getElementsByClassName('card-signup')[0];
                                                    card_signup.querySelectorAll('.status-circle')[4].style.opacity = '1';
                                                    card_signup.querySelectorAll('.status-circle')[5].style.opacity = '1';
                                                    enabledPopupAlert('As senhas não coincidem!');
                                                }
                                            }else{
                                                let card_signup = document.getElementsByClassName('card-signup')[0];
                                                card_signup.querySelectorAll('.status-circle')[5].style.opacity = '1';
                                                enabledPopupAlert('Preencha o campo confirmar senha!');
                                            }
                                        }else{
                                            let card_signup = document.getElementsByClassName('card-signup')[0];
                                            card_signup.querySelectorAll('.status-circle')[4].style.opacity = '1';
                                            enabledPopupAlert('Preencha o campo senha!');
                                        }
                                    }else{
                                        let card_signup = document.getElementsByClassName('card-signup')[0];
                                        card_signup.querySelectorAll('.status-circle')[3].style.opacity = '1';
                                        enabledPopupAlert('Preencha o campo email corretamente!');
                                    }
                                }else{
                                    let card_signup = document.getElementsByClassName('card-signup')[0];
                                        card_signup.querySelectorAll('.status-circle')[3].style.opacity = '1';
                                        enabledPopupAlert('Preencha o campo senha!');
                                }
                            }else{
                                let card_signup = document.getElementsByClassName('card-signup')[0];
                                card_signup.querySelectorAll('.status-circle')[2].style.opacity = '1';
                                enabledPopupAlert('Preencha o campo telefone corretamente!');
                            }
                        }else{
                            let card_signup = document.getElementsByClassName('card-signup')[0];
                            card_signup.querySelectorAll('.status-circle')[2].style.opacity = '1';
                            enabledPopupAlert('Preencha o campo telefone!');
                        }
                    }else{
                        let card_signup = document.getElementsByClassName('card-signup')[0];
                        card_signup.querySelectorAll('.status-circle')[1].style.opacity = '1';
                        enabledPopupAlert('Preencha o campo CPF corretamente!');
                    }
                }else{
                    let card_signup = document.getElementsByClassName('card-signup')[0];
                    card_signup.querySelectorAll('.status-circle')[1].style.opacity = '1';
                    enabledPopupAlert('Preencha o campo CPF!');
                }
            }else{
                let card_signup = document.getElementsByClassName('card-signup')[0];
                card_signup.querySelectorAll('.status-circle')[0].style.opacity = '1';
                enabledPopupAlert('Preencha o campo nome completo!');
            }
        }else{
            openMenuSignup();
        }
    }

    let btns_signin = document.getElementsByClassName('btn-signin');
    for(let i = 0; i < btns_signin.length; i++){
        btns_signin[i].addEventListener('click', actionButtonSignin);
    }

    let btns_signup = document.getElementsByClassName('btn-signup');
    for(let i = 0; i < btns_signup.length; i++){
        btns_signup[i].addEventListener('click', actionButtonSignup);
    }
});

export { displayMenuAuth, openMenuSignin, openMenuSignup, closeMenuSuspended };
function disabledScrollBody() {
    document.body.style.overflow = 'hidden';
}

function enabledScrollBody() {
    document.body.style.overflow = 'auto';
}

function displayMenuAuth(){
    let container_menu_auth = document.getElementsByClassName('containers-cards-auth')[0];
    if(container_menu_auth.style.display === 'none' || container_menu_auth.style.display === ''){
        container_menu_auth.style.display = 'flex';
        disabledScrollBody();
    }else{
        container_menu_auth.style.display = 'none';
        enabledScrollBody();
    }
}

function closeAuth(){
    let data_type = this.getAttribute('data-type');
    if(data_type === 'signin'){
        let container_signin = document.getElementsByClassName('card-signin')[0];
        displayMenuAuth();
        container_signin.style.display = 'none';
    }else{
        let container_signup = document.getElementsByClassName('card-signup')[0];
        displayMenuAuth();
        container_signup.style.display = 'none';
    }
}

function openMenuSignin(){
    closeMenuSuspended();
    let container_signin = document.getElementsByClassName('card-signin')[0];
    if(container_signin.style.display === 'none' || container_signin.style.display === ''){
        let container_signup = document.getElementsByClassName('card-signup')[0];
        container_signup.style.display = 'none';
        container_signin.style.display = 'flex';
        let container_menu_auth = document.getElementsByClassName('containers-cards-auth')[0];
        if(container_menu_auth.style.display === 'none' || container_menu_auth.style.display === ''){
            displayMenuAuth();
        }
    }
}

function openMenuSignup(){
    closeMenuSuspended();
    let container_signup = document.getElementsByClassName('card-signup')[0];
    if(container_signup.style.display === 'none' || container_signup.style.display === ''){
        let container_signin = document.getElementsByClassName('card-signin')[0];
        container_signin.style.display = 'none';
        container_signup.style.display = 'flex';
        let container_menu_auth = document.getElementsByClassName('containers-cards-auth')[0];
        if(container_menu_auth.style.display === 'none' || container_menu_auth.style.display === ''){
            displayMenuAuth();
        }
    }
}

function closeMenuSuspended(){
    let btn_suspend_menu = document.getElementsByClassName('btn-suspend-menu')[0];
    let menu_suspended = document.getElementsByClassName('menu-suspended')[0];
    let menu_suspendend_container = document.getElementsByClassName('menu-suspended-container')[0];
    if(btn_suspend_menu.getAttribute('data-status') === 'true'){
        menu_suspended.style.display = 'none';
        menu_suspendend_container.style.height = '0';
        btn_suspend_menu.setAttribute('data-status', 'false');
        btn_suspend_menu.getElementsByClassName('line-menu')[0].style.backgroundColor = 'let(--primary-text-color)';
        btn_suspend_menu.getElementsByClassName('line-menu')[1].style.backgroundColor = 'let(--primary-text-color)';
        btn_suspend_menu.getElementsByClassName('line-menu')[2].style.backgroundColor = 'let(--primary-text-color)';
    }
}


document.getElementsByClassName('close-auth')[0].addEventListener('click', closeAuth);
document.getElementsByClassName('close-auth')[1].addEventListener('click', closeAuth);

let auth_inputs = document.querySelectorAll('.card-auth-inputs input');
for(let i = 0; i < auth_inputs.length; i++){
    auth_inputs[i].addEventListener('focus', function(){
        let status_circle = this.parentElement.querySelectorAll('.status-circle')[0]
        status_circle.style.opacity = '0';
    });
}

document.getElementById('confirm-password').addEventListener('keyup', function(){
    let password = document.getElementById('password-signup').value;
    let confirm_password = document.getElementById('confirm-password').value;
    if(password !== confirm_password){
        let card_signup = document.getElementsByClassName('card-signup')[0];
        card_signup.querySelectorAll('.status-circle')[4].style.opacity = '1';
        card_signup.querySelectorAll('.status-circle')[5].style.opacity = '1';
    }else{
        let card_signup = document.getElementsByClassName('card-signup')[0];
        card_signup.querySelectorAll('.status-circle')[4].style.opacity = '0';
        card_signup.querySelectorAll('.status-circle')[5].style.opacity = '0';
    }
});

document.getElementById('password-signup').addEventListener('keyup', function(){
    let password = this.value;
    let confirm_password = document.getElementById('confirm-password').value;
    if(confirm_password !== ''){
        if(password !== confirm_password){
            let card_signup = document.getElementsByClassName('card-signup')[0];
            card_signup.querySelectorAll('.status-circle')[4].style.opacity = '1';
            card_signup.querySelectorAll('.status-circle')[5].style.opacity = '1';
        }else{
            let card_signup = document.getElementsByClassName('card-signup')[0];
            card_signup.querySelectorAll('.status-circle')[4].style.opacity = '0';
            card_signup.querySelectorAll('.status-circle')[5].style.opacity = '0';
        }
    }
});