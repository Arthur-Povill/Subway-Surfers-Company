from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import controller

# Create your views here.
def index(request):
    data = controller.data_application()
    if request.user.is_authenticated is False:
        affiliate_code = controller.verify_param(request, 'affiliate')
        data['affiliate_code'] = affiliate_code
        return render(request, 'app-structure/original/index-not-logged.html', data)
    else:
        profile = controller.profile(request)
        data_profile = controller.api_profile(request)
        data['profile'] = data_profile
        if profile.first_access is False: 
            return redirect('/game')
        else:
            try:
                demo_param = request.GET.get('demo', None)
            except:
                demo_param = None
                
            if demo_param == 'false':
                controller.first_access(request)
                return redirect('/')
            else:
                return render(request, 'app-structure/original/index-welcome.html', data)
            
def register(request):
    if request.user.is_authenticated is False:
        affiliate_code = controller.verify_param(request, 'affiliate')
        data = controller.data_application()
        data['affiliate_code'] = affiliate_code
        return render(request, 'app-structure/original/index-register.html', data)
    else:
        return redirect('/')
    
def login(request):
    if request.user.is_authenticated is False:
        affiliate_code = controller.verify_param(request, 'affiliate')
        data = controller.data_application()
        data['affiliate_code'] = affiliate_code
        return render(request, 'app-structure/original/index-login.html', data)
    else:
        return redirect('/')
    
def logout(request):
    if request.user.is_authenticated:
        controller.logout(request)
        return redirect('/')
    else:
        return redirect('/')

def withdraw(request):
    if request.user.is_authenticated:
        data = controller.data_application()
        data['profile'] = controller.api_profile(request)
        data['is_admin'] = request.user.is_superuser
        return render(request, 'app-structure/original/index-withdraw.html', data)
    else:
        return redirect('/auth/register')
    
def deposit(request):
    if request.user.is_authenticated:
        data = controller.data_application()
        data['profile'] = controller.api_profile(request)
        data['is_admin'] = request.user.is_superuser
        return render(request, 'app-structure/original/index-deposit.html', data)
    else:
        return redirect('/auth/register')
    
def deposit_info(request, id):
    if request.user.is_authenticated:
        data = controller.data_application()
        response = controller.get_info_deposit(request, id)
        if response['status_boolean']:
            data['deposit'] = response['data']
            if data['deposit']['status'] == 'pending':
                data['is_admin'] = request.user.is_superuser
                return render(request, 'app-structure/original/index-deposit-id.html', data)
            else:
                return redirect('/deposit')
        else:
            return redirect('/')
    else:
        return redirect('/auth/register')
    
def partnership(request):
    if request.user.is_authenticated:
        data = controller.data_application()
        data_profile = controller.api_profile(request)
        data['profile'] = data_profile
        data['affiliate'] = controller.api_affiliate(request)
        data['is_admin'] = request.user.is_superuser
        return render(request, 'app-structure/original/index-partnership.html', data)
    else:
        return redirect('/auth/register')
    
def referral(request):
    if request.user.is_authenticated:
        data = controller.data_application()
        data_profile = controller.api_profile(request)
        data['profile'] = data_profile
        data['affiliate'] = controller.api_affiliate(request)
        data['is_admin'] = request.user.is_superuser
        return render(request, 'app-structure/original/index-referral.html', data)
    else:
        return redirect('/auth/register')
    
def game(request):
    if request.user.is_authenticated:
        data = controller.data_application()
        data_profile = controller.api_profile(request)
        data['profile'] = data_profile
        data['is_admin'] = request.user.is_superuser
        return render(request, 'app-structure/original/index-game.html', data)
    else:
        return redirect('/auth/register')

def terms(request):
    data = controller.data_application()
    if request.user.is_authenticated:
        data_profile = controller.api_profile(request)
        data['profile'] = data_profile
        data['is_admin'] = request.user.is_superuser
        return render(request, 'app-structure/original/index-terms-logged.html', data)
    else:
        return render(request, 'app-structure/original/index-terms-no-logged.html', data)

def classic_game(request):
    if request.user.is_authenticated:
        mode = controller.verify_param(request, 'mode')
        if mode == 'demo' or mode == 'free':
            profile = controller.profile(request)
            if profile.first_access is True:
                controller.first_access(request)
                data = controller.data_application()
                return render(request, 'app-structure/personalized/classic-game.html', data)
            else:
                return redirect('/')
        else:
            data = controller.data_application()
            return render(request, 'app-structure/personalized/classic-game.html', data)
    else:
        return redirect('/')

def classic_game_dev(request):
    return render(request, 'app-structure/personalized/classic-game-test.html')

