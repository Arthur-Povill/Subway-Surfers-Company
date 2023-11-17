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

document.getElementsByClassName('btn-admin-home')[0].addEventListener('click', function() {
    window.location.href = '/panel';
});
document.getElementsByClassName('btn-admin-home')[1].addEventListener('click', function() {
    window.location.href = '/panel';
});

document.getElementsByClassName('btn-play')[0].addEventListener('click', function() {
    window.location.href = '/';
});

document.getElementsByClassName('btn-panel-users')[0].addEventListener('click', function() {
    window.location.href = '/panel/users';
});

document.getElementsByClassName('btn-panel-withdraw')[0].addEventListener('click', function() {
    window.location.href = '/panel/withdraws';
});

document.getElementsByClassName('btn-panel-affiliates')[0].addEventListener('click', function() {
    window.location.href = '/panel/affiliates';
});

document.getElementsByClassName('btn-easy-game')[0].addEventListener('click', function() {
    window.location.href = '/game/v2';
});

document.getElementsByClassName('btn-ggr')[0].addEventListener('click', function() {
    window.location.href = '/panel/ggr';
});

document.getElementsByClassName('btn-configuration')[0].addEventListener('click', function() {
    window.location.href = '/panel/configs';
});

if(document.getElementsByClassName('btn-signout').length > 0){
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
}
