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
    path('referral/', views.referral, name='referral'),
    path('deposit/', views.deposit, name='deposit'),
    path('deposit/<str:id>', views.deposit_info, name='deposit'),
    path('terms/', views.terms, name='terms'),
    path('legal/', views.terms, name='terms'),
    path('game/', views.game, name='game'),
    path('game/v2', views.game_v2, name='game'),
    path('games/classic', views.classic_game, name='classic_game'),
    path('games/v2/classic', views.classic_game_v2, name='classic_game'),
    #path('games/classic/test', views.classic_game_dev, name='classic_game'),
]