var url = window.location.href;

function template_dashboard(dash){
    var xhr = new XMLHttpRequest();
    var element = document.getElementById('dash-' + dash);
    xhr.open('GET', 'template/dashboards?dash=' + dash, true);
    xhr.onload = function () {
        if(this.status == 200){
            element.innerHTML = this.responseText;
        }
    }
    xhr.send();

}

function dashboards(){
    var splited_url = url.split('/panel/');
    if(url.includes('panel/') && splited_url[1] == ''){
        var list_dashs = ['gains', 'registers', 'deposits', 'withdraws']
        for(var i = 0; i < list_dashs.length; i++){
            template_dashboard(list_dashs[i]);
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


dashboards();
document.getElementsByClassName('main')[0].addEventListener('click', closeMenuSuspended);
setInterval(dashboards, 30000);



