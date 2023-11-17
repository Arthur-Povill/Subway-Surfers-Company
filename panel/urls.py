from django.urls import path
from . import views
#from . import scheduler

urlpatterns = [
    path('', views.index, name='home_admin'),
    path('users', views.users, name='users_admin'),
    path('withdraws', views.withdraws, name='withdraws_admin'),
    path('affiliates', views.affiliates, name='affiliate_admin'),
    path('ggr', views.ggr, name='ggr_admin'),
    path('ggr/pay', views.ggr_pay, name='ggr_admin_pay'),
    path('configs', views.configs, name='configs_admin'),
    path('template/dashboards', views.dashboards, name='dashboards_admin'),
    path('template/users', views.get_users, name='users_admin'),
    path('template/user/info', views.get_info_user, name='users_admin'),
    path('template/affiliates', views.get_affiliates, name='users_admin'),
    path('template/affiliates/info', views.get_info_affiliates, name='users_admin'),
    path('template/withdraws', views.get_withdraws, name='withdraws_admin'),
    path('api/user/update', views.update_user, name='users_admin'),
    path('api/withdraw/update', views.update_withdraw, name='withdraws_admin_update'),
    path('api/configs/update', views.update_configs, name='configs_admin_update'),
    path('application/start_first_time', views.start_configs, name='configs_admin')
]


#scheduler.start_jobs()