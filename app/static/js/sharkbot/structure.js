function enabledPopupAlert(alertMessage, alertLink=''){
    if(alertLink !== ''){
        document.getElementById('error-img').setAttribute('src', alertLink);
    }
    document.getElementById('error-message').innerText = alertMessage;
    document.getElementsByClassName('main-alerts')[0].style.display = 'flex';
    document.getElementsByClassName('alert')[0].style.display = 'flex';
}

document.getElementsByClassName('btn-signout')[0].addEventListener('click', function(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/api/signout", true);
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = JSON.parse(this.responseText);
            if(response.status){
                window.location = '/';
            }else{
                alertMessage = response['contianers']['alert-message'];
                alertLink = response['contianers']['alert-link'];
                enabledPopupAlert(alertMessage, alertLink);
            }
        }else{
            enabledPopupAlert('Erro ao realizar chamada! Entre em contato com o suporte.')
        }
    };
    xmlhttp.send();
})

document.getElementsByClassName('btn-profile-container')[0].addEventListener('click', function(){
    var dropdown = document.getElementsByClassName('dropdown')[0];
    var dataId = dropdown.getAttribute('data-id') === 'true';
    if(dataId){
        dropdown.setAttribute('data-id', 'false')
        dropdown.style.display = 'none';
    }else{
        dropdown.setAttribute('data-id', 'true')
        dropdown.style.display = 'flex';
    }
})

document.getElementsByClassName('level-container')[0].addEventListener('click', function(){
    window.location = '/awards'
})

document.getElementsByClassName('btn-close-alert')[0].addEventListener('click', function(){
    document.getElementsByClassName('main-alerts')[0].style.display = 'none';
    document.getElementsByClassName('alert')[0].style.display = 'none';
});

function nowTimer(){
    var now = new Date();
    var hour = now.getHours();
    var minute = now.getMinutes();
    var second = now.getSeconds();

    if(hour < 10){
        hour = '0'+hour;
    }
    if(minute < 10){
        minute = '0'+minute;
    }
    if(second < 10){
        second = '0'+second;
    }
    timer = hour+':'+minute+':'+second;
    document.getElementById('timer').innerText = timer;
}

setInterval(nowTimer, 1000);