from api import controller as api_controller
from django.contrib.auth.models import User
from panel import models as panel_models
from api import controller as api_controller
import locale

def profile(request):
    user = request.user
    email = user.email
    user_profile = panel_models.profile.objects.get(email=email)

    return user_profile

def first_access(request):
    api_controller.first_access(request)
    user = request.user
    email = user.email
    user_profile = panel_models.profile.objects.get(email=email)

    return user_profile

def verify_param(request, param):
    try:
        param = request.GET.get(param, None)
    except:
        param = None
    return param

def format_currency_brazilian(number):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    formatted_number = locale.currency(number, grouping=True, symbol=None)
    return formatted_number

def api_profile(request):
    response_balance = api_controller.api_my_profile(request)
    return response_balance['data']

def api_affiliate(request):
    response_affiliate = api_controller.api_info_affiliates(request)
    return response_affiliate['data']
 
def info_affiliates(request):
    response = api_controller.api_info_affiliates(request)
    return response['data']

def logout(request):
    if request.user.is_authenticated:
        api_controller.api_signout(request)

    return True

def get_info_deposit(request, id):
    response = api_controller.get_info_deposit(request, {
        'external_id': id
    }, False)

    return response

def data_application():
    data = api_controller.application_info()
    data['app_name_split_1'] = data['app_name_separated'].split(' ')[0]
    data['app_name_split_2'] = data['app_name_separated'].split(' ')[1]
    return data

def status_game(request):
    response = api_controller.api_game_status(request)
    return response

def vanishing_affiliate(request):
    user = request.user
    email = user.email
    user_profile = panel_models.profile.objects.get(email=email)
    if profile.vanish is True:
        profile.vanish = False
        profile.affiliate_user = None
        profile.save()
 