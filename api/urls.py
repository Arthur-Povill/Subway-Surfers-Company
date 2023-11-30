from django.urls import path
from . import views

urlpatterns = [
    path('v1/signin', views.api_signin, name='v1_api_signin'),
    path('v1/signup', views.api_signup, name='v1_api_signup'),
    path('v1/signout', views.api_signout, name='v1_api_signout'),
    path('v1/recovery', views.api_recovery, name='v1_api_recovery'),
    path('v1/my/profile', views.api_my_profile, name='v1_api_my_profile'),
    path('v1/my/profile/update', views.api_update_my_profile, name='v1_api_update_my_profile'),
    path('v1/my/profile/update/phone', views.api_update_phone, name='v1_api_update_my_profile_phone'),
    path('v1/my/affiliates', views.api_info_affiliates, name='v1_api_info_affiliates'),
    path('v1/my/deposits', views.api_info_deposits, name='v1_api_info_deposits'),
    path('v1/my/withdraws', views.api_info_withdraws, name='v1_api_info_withdraws'),
    path('v1/withdraw/new', views.api_new_withdraw, name='v1_api_new_withdraw'),
    #path('v1/withdraw/free', views.api_new_withdraw_free, name='v1_api_new_withdraw'),
    path('v1/deposit/new', views.api_new_deposit, name='v1_api_new_deposit'),
    path('v1/game/new', views.api_game_new, name='v1_api_game_new'),
    path('v1/game/status', views.api_game_status, name='v1_api_game_status'),
    path('v1/game/status/verify', views.api_game_status_verify),
    path('v1/game/update', views.api_game_update, name='v1_api_game_update'),
    path('v1/game/update/external', views.api_game_update_external, name='v1_api_game_update'),
    path('v1/webhook/deposit/confirm', views.api_webhook_deposit, name='v1_api_webhook_deposit_confirm'),
]