import(dynamicStaticFile + 'js/app-structure/default-client/funct-min-82092.js').then(module => {
    const { sleep } = module;

    document.addEventListener('DOMContentLoaded', function() {
        var welcome_message = document.getElementsByClassName('welcome-animation')[0];
        sleep(5000).then(() => {
            var card_game_free = document.getElementsByClassName('card-game-free')[0];
            card_game_free.style.display = 'flex';
            document.getElementsByClassName('accept')[0].addEventListener('click', function(){
                var card_game_free = document.getElementsByClassName('card-game-free')[0];
                card_game_free.style.display = 'none';
                window.location.href = '/games/classic?mode=free';
            });
            document.getElementsByClassName('deny')[0].addEventListener('click', function(){
                var card_game_free = document.getElementsByClassName('card-game-free')[0];
                card_game_free.style.display = 'none';
                window.location.href = '/?demo=false';
            });
        });
    });
});