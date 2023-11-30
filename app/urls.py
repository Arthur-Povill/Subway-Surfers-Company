from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('auth/register', views.register, name='register'),
    path('auth/login', views.login, name='login'),
    path('auth/recover', views.recovery, name='recovery'),
    path('auth/logout', views.logout, name='logout'),
    path('cashier/withdraw', views.withdraw, name='withdraw'),
    path('partnership/', views.partnership, name='partnership'),
    path('withdraw/lp', views.withdraw_lp, name='withdraw'),
    path('join/<str:code>', views.join, name='join'),
    path('referral/', views.referral, name='referral'),
    path('deposit/', views.deposit, name='deposit'),
    path('deposit/<str:id>', views.deposit_info, name='deposit'),
    path('terms/', views.terms, name='terms'),
    path('legal/', views.terms, name='terms'),
    path('game/', views.game, name='game'),
    path('games/classic', views.classic_game, name='classic_game'),
    path('games/classic/dev', views.classic_game_dev),
    path('games/classic/js/workers/worker.0a8b30d0071f04d38b17.js', views.classic_worker_js),
    path('first_access', views.first_access, name='first_access'),
    path('izooto.html', views.izooto_html, name='izooto'),
    path('ads.txt', views.izooto_ads_txt, name='ads_txt'),
]