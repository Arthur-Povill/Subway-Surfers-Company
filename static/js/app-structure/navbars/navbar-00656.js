import(dynamicStaticFile + 'js/app-structure/default-client/auth-min-32394.js').then(module => {
    const { displayMenuAuth, openMenuSignin, openMenuSignup, closeMenuSuspended } = module;

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

    let btns_open_signin = document.querySelectorAll('.btn-open-signin')
    for (let i = 0; i < btns_open_signin.length; i++) {
        btns_open_signin[i].addEventListener('click', openMenuSignin); 
    }

    let btns_open_signup = document.querySelectorAll('.btn-open-signup')
    for (let i = 0; i < btns_open_signup.length; i++) {
        btns_open_signup[i].addEventListener('click', openMenuSignup);
    }

    document.getElementsByClassName('main')[0].addEventListener('click', closeMenuSuspended);
});