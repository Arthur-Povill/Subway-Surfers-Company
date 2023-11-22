from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from . import controller

# Create your views here.
@vary_on_headers('Cookie')
def index(request):
    data = controller.data_application()
    if request.user.is_authenticated is False:
        affiliate_code = controller.verify_param(request, 'affiliate')
        data['affiliate_code'] = affiliate_code
        return render(request, 'app-structure/original/index-not-logged.html', data)
    else:
        profile = controller.profile(request)
        if profile.first_access: 
            controller.first_access(request)
        
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
                data_profile = controller.api_profile(request)
                data['profile'] = data_profile
                return render(request, 'app-structure/original/index-welcome.html', data)

     
def register(request):
    if request.user.is_authenticated is False:
        affiliate_code = controller.verify_param(request, 'affiliate')
        data = controller.data_application()
        data['affiliate_code'] = affiliate_code
        return render(request, 'app-structure/original/index-register.html', data)
    else:
        return redirect('/')

@cache_page(60) 
def login(request):
    if request.user.is_authenticated is False:
        #affiliate_code = controller.verify_param(request, 'affiliate')
        data = controller.data_application()
        #data['affiliate_code'] = affiliate_code
        return render(request, 'app-structure/original/index-login.html', data)
    else:
        return redirect('/')

@cache_page(60)
def recovery(request):
    if request.user.is_authenticated is False:
        data = controller.data_application()
        return render(request, 'app-structure/original/index-recovery.html', data)
    else:
        return redirect('/')   

@cache_page(60)
def logout(request):
    if request.user.is_authenticated:
        controller.logout(request)
        return redirect('/')
    else:
        return redirect('/')

@vary_on_headers('Cookie')
def withdraw(request):
    if request.user.is_authenticated:
        data = controller.data_application()
        data['profile'] = controller.api_profile(request)
        data['is_admin'] = request.user.is_superuser
        return render(request, 'app-structure/original/index-withdraw.html', data)
    else:
        return redirect('/auth/register')

@vary_on_headers('Cookie')
def deposit(request):
    if request.user.is_authenticated:
        #controller.vanishing_affiliate(request)
        data = controller.data_application()
        data['profile'] = controller.api_profile(request)
        data['is_admin'] = request.user.is_superuser
        return render(request, 'app-structure/original/index-deposit.html', data)
    else:
        return redirect('/auth/register')
    
@vary_on_headers('Cookie')
def deposit_info(request, id):
    if request.user.is_authenticated:
        #controller.vanishing_affiliate(request)
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

@vary_on_headers('Cookie')
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
    
@vary_on_headers('Cookie')  
def join(request, code):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return redirect('/auth/register?affiliate=' + code)

@vary_on_headers('Cookie')
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
    
@vary_on_headers('Cookie') 
def game(request):
    if request.user.is_authenticated:
        data = controller.data_application()
        data_profile = controller.api_profile(request)
        data['profile'] = data_profile
        data['is_admin'] = request.user.is_superuser
        return render(request, 'app-structure/original/index-game.html', data)
    else:
        return redirect('/auth/register')

@vary_on_headers('Cookie')
def game_v2(request):
    if request.user.is_authenticated:
        data = controller.data_application()
        data_profile = controller.api_profile(request)
        data['profile'] = data_profile
        data['is_admin'] = request.user.is_superuser
        if data_profile['user']['influencer'] is True or request.user.is_superuser is True:
            return render(request, 'app-structure/original/index-game-easy.html', data)
        else:
            return redirect('/')
    else:
        return redirect('/auth/register')

@cache_page(60)
def terms(request):
    data = controller.data_application()
    if request.user.is_authenticated:
        data_profile = controller.api_profile(request)
        data['profile'] = data_profile
        data['is_admin'] = request.user.is_superuser
        return render(request, 'app-structure/original/index-terms-logged.html', data)
    else:
        return render(request, 'app-structure/original/index-terms-no-logged.html', data)

@vary_on_headers('Cookie')
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

@vary_on_headers('Cookie')  
def classic_game_v2(request):
    if request.user.is_authenticated:
        mode = controller.verify_param(request, 'mode')
        profile = controller.profile(request)
        if profile.is_influencer is True or request.user.is_superuser is True:
            if mode == 'demo' or mode == 'free':
                if profile.first_access is True:
                    controller.first_access(request)
                    data = controller.data_application()
                    return render(request, 'app-structure/personalized/classic-game-easy.html', data)
                else:
                    return redirect('/')
            else:
                data = controller.data_application()
                return render(request, 'app-structure/personalized/classic-game-easy.html', data)
        else:
            return redirect('/')
    else:
        return redirect('/')

@vary_on_headers('Cookie')
def classic_game_dev(request):
    data = controller.data_application()
    print(data)
    return render(request, 'app-structure/game/classic-game.html', data)

@cache_page(60)
def handler_not_found(request, exception):
    return redirect('/')

