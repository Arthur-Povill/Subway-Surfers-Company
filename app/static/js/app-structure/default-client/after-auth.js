export { closeMenuSuspended };

function disabledScrollBody() {
    document.body.style.overflow = 'hidden';
}

function enabledScrollBody() {
    document.body.style.overflow = 'auto';
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