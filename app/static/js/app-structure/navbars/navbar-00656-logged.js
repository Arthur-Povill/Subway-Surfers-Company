import { closeMenuSuspended } from '../default-client/after-auth-min-09982.js';
import { enabledPopupAlert, obfuscateMessage, deobfuscateMessage, formatedCpf, formatedPhone, getCSRFToken, decodeBase64 } from '/static/js/app-structure/default-client/funct.js';

const importPromise1 = import(dynamicStaticFile + 'js/app-structure/default-client/funct-min-82092.js');
const importPromise2 = import(dynamicStaticFile + 'js/app-structure/default-client/after-auth-min-09982.js');

Promise.all([importPromise1, importPromise2]).then(modules => {
    const module1 = modules[0];
    const module2 = modules[1];
    const { enabledPopupAlert, obfuscateMessage, deobfuscateMessage, formatedCpf, formatedPhone, getCSRFToken, decodeBase64 } = module1;
    const { closeMenuSuspended } = module2;

    document.getElementsByClassName('navbar-00656-logo')[0].addEventListener('click', function() {
        window.location.href = '/';
    });
    
    document.getElementsByClassName('btn-suspend-menu')[0].addEventListener('click', function() {
        let data_status = this.getAttribute('data-status');
        let menu_suspended = document.getElementsByClassName('menu-suspended')[0];
        let menu_suspendend_container = document.getElementsByClassName('menu-suspended-container')[0];
        if(data_status === 'false'){
            menu_suspended.style.display = 'flex';
            menu_suspendend_container.style.height = 'fit-content';
            this.setAttribute('data-status', 'true');
        }else{
            menu_suspended.style.display = 'none';
            menu_suspendend_container.style.height = '0';
            this.setAttribute('data-status', 'false');
            this.getElementsByClassName('line-menu')[0].style.backgroundColor = 'let(--primary-text-color)';
            this.getElementsByClassName('line-menu')[1].style.backgroundColor = 'let(--primary-text-color)';
            this.getElementsByClassName('line-menu')[2].style.backgroundColor = 'let(--primary-text-color)';
        }
    });
    
    function callTemplateProfile(){
        document.getElementsByClassName('container-profile')[0].style.display = 'flex';
    }
    
    document.getElementsByClassName('main')[0].addEventListener('click', closeMenuSuspended);
    if(document.getElementsByClassName('btn-admin').length > 0){
        document.getElementsByClassName('btn-admin')[0].addEventListener('click', function() {
            window.location.href = '/panel';
        });
    }
    document.getElementsByClassName('btn-profile')[0].addEventListener('click', callTemplateProfile);
    document.getElementsByClassName('btn-profile')[1].addEventListener('click', callTemplateProfile);
    document.getElementsByClassName('btn-play')[0].addEventListener('click', function() {
        window.location.href = '/';
    });
    document.getElementsByClassName('btn-deposit')[0].addEventListener('click', function() {
        document.getElementsByClassName('container-deposit')[0].style.display = 'flex';
    });
    document.getElementsByClassName('btn-withdraw')[0].addEventListener('click', function() {
        document.getElementsByClassName('container-withdraw')[0].style.display = 'flex';
    });
    document.getElementsByClassName('btn-affiliates')[0].addEventListener('click', function() {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', 'api/v1/my/affiliates');
        xhr.onload = function() {
            if(xhr.status === 200){
                var response = JSON.parse(this.response);
                var response_decrypted = deobfuscateMessage(response.response);
                var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                let data = JSON.parse(jsonStringFormated);
                if(data.status_boolean === true){
                    data = data.data;
                    console.log(data);
                    document.getElementById('copy-affiliates-code').value = data.link;
                    document.getElementsByClassName('total-earning')[0].innerText = data.total_earning;
                    document.getElementsByClassName('total-earning-month')[0].innerText = data.total_earning_month;
                    document.getElementsByClassName('total-earning-last-month')[0].innerText = data.total_earning_last_month;
                    
                    document.getElementsByClassName('cpa-percent')[0].innerText = data.cpa_percent;
                    document.getElementsByClassName('cpa-count')[0].innerText = data.cpa_count;
                    document.getElementsByClassName('cpa-deposits')[0].innerText = data.cpa_deposits;
                    document.getElementsByClassName('cpa-total-earnings')[0].innerText = data.cpa_total_earnings;
                    document.getElementsByClassName('cpa-total-earnings-month')[0].innerText = data.cpa_total_earnings_month;
                    
                    document.getElementsByClassName('revshare-percent')[0].innerText = data.revshare_percent;
                    document.getElementsByClassName('revshare-count')[0].innerText = data.revshare_count;
                    document.getElementsByClassName('revshare-total-earnings')[0].innerText = data.revshare_total_earnings;
                    document.getElementsByClassName('revshare-total-earnings-month')[0].innerText = data.revshare_total_earnings_month;
    
                    document.getElementsByClassName('container-affiliates')[0].style.display = 'flex';
                }else{
                    enabledPopupAlert(data.status_message);
                }
            }
        }
        xhr.send();
    });
    document.getElementsByClassName('btn-signout')[0].addEventListener('click', function() {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', 'api/v1/signout');
        xhr.onload = function() {
            if(xhr.status === 200){
                window.location.href = '/';
            }
        }
        xhr.send();
    });
    
    
    function setProfileActions(){
        var carc_fixed_title = document.getElementsByClassName("card-bottom-fixed-title");
        var cpf_profile = document.getElementById('cpf-profile');
        cpf_profile.value = formatedCpf(cpf_profile.value);
        var phone_profile = document.getElementById('phone-profile');
        phone_profile.value = formatedPhone(phone_profile.value);
    
        document.getElementsByClassName('btn-save-profile')[0].addEventListener('click', function(){
            var full_name = document.getElementById('full-name-profile').value;
            var cpf = document.getElementById('cpf-profile').value;
            var phone = document.getElementById('phone-profile').value;
            var email = document.getElementById('email-profile').value;
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'api/v1/my/profile/update');
            xhr.setRequestHeader('X-CSRFToken', getCSRFToken());
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onload = function() {
                if(xhr.status === 200){
                    var response = JSON.parse(this.response);
                    var response_decrypted = deobfuscateMessage(response.response);
                    var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                    let data = JSON.parse(jsonStringFormated);
                    if(data.status_boolean === true){
                        enabledPopupAlert(data.message, 'correct.png');
                    }else{
                        enabledPopupAlert(data.message);
                    }
                }
            }
            var data = {
                full_name: full_name,
                cpf: cpf,
                phone: phone,
                email: email
            }
            data = JSON.stringify({'response': obfuscateMessage(JSON.stringify(data))})
            xhr.send(data);
        })
        document.getElementById('phone-profile').addEventListener('keyup', function() {
            this.value = formatedPhone(this.value);
        });
    
        function internal(element, right){
            var menu_selected = document.getElementsByClassName('menu-selected')[0];
            menu_selected.classList.remove('menu-selected');
            element.classList.add('menu-selected');
            document.getElementsByClassName('card-bottom-auto-menus-container')[0].style.right = right;
        };
    
        carc_fixed_title[0].addEventListener('click', function() {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', 'api/v1/my/profile');
            xhr.onload = function() {
                if(xhr.status === 200){
                    var response = JSON.parse(this.response);
                    var response_decrypted = deobfuscateMessage(response.response);
                    var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                    let data = JSON.parse(jsonStringFormated);
                    if(data.status_boolean === true){
                        data = data.data;
                        document.getElementById('full-name-profile').value = data.user.full_name;
                        document.getElementById('email-profile').value = data.user.email;
                        document.getElementById('phone-profile').value = data.user.phone;
                    }else{
                        enabledPopupAlert(data.status_message);
                    }
                }
            }
            xhr.send();
            internal(this, '0%');
        });
        carc_fixed_title[1].addEventListener('click', function() {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', 'api/v1/my/deposits');
            xhr.onload = function() {
                if(xhr.status === 200){
                    var response = JSON.parse(this.response);
                    var response_decrypted = deobfuscateMessage(response.response);
                    var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                    let data = JSON.parse(jsonStringFormated);
                    if(data.status_boolean === true){
                        var html = decodeBase64(data.html);
                        data = data.data;
                        document.getElementsByClassName('card-container-deposit')[0].innerHTML = html;
                    }else{
                        enabledPopupAlert(data.status_message);
                    }
                }
            }
            xhr.send();
            internal(this, '100%');
        });
        carc_fixed_title[2].addEventListener('click', function() {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', 'api/v1/my/withdraws');
            xhr.onload = function() {
                if(xhr.status === 200){
                    var response = JSON.parse(this.response);
                    var response_decrypted = deobfuscateMessage(response.response);
                    var jsonStringFormated = response_decrypted.replace(/'/g, "\"");
                    let data = JSON.parse(jsonStringFormated);
                    if(data.status_boolean === true){
                        var html = decodeBase64(data.html);
                        data = data.data;
                        document.getElementsByClassName('card-container-withdraw')[0].innerHTML = html;
                    }else{
                        enabledPopupAlert(data.status_message);
                    }
                }
            }
            xhr.send();
            internal(this, '200%');
        });
    }
    function setWithdrawAction(){
        document.getElementsByClassName('btn-confirm-withdraw')[0].addEventListener('click', function() {
            var value = document.getElementById('value-withdraw').value;
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'api/v1/withdraw/new');
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
                        data = data.data;
                        document.getElementsByClassName('player-balance')[0].innerText = data.value;
                        enabledPopupAlert(message, 'correct.png');
                    }else{
                        enabledPopupAlert(data.message);
                    }
                }
            }
            var data = {
                value: value
            }
            data = JSON.stringify({'response': obfuscateMessage(JSON.stringify(data))})
            xhr.send(data);
        });
    }
    
    setProfileActions();
    setWithdrawAction();
});

