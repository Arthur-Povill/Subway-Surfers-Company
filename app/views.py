from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.http import HttpResponse
from django.http import FileResponse
import requests
from django.conf import settings
import os
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
        '''if profile.first_access: 
            controller.first_access(request)'''
        return redirect('/game')
        
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
def withdraw_lp(request):
    if request.user.is_authenticated is False:
        data = controller.data_application()
        return render(request, 'app-structure/original/withdraw-free.html', data)
    else:
        return redirect('/')

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
        domain = request.META['HTTP_HOST']
        data = controller.data_application()
        mode = controller.verify_param(request, 'mode')
        status_game = controller.status_game(request)
        data['is_admin'] = request.user.is_superuser
        data['status_game'] = status_game['data'] if mode != 'demo' or mode != 'free' else {'in_game': True, 'game': {'hash_game': 'null', 'value': '5.0'}}
        data['status_game']['domain'] = domain
        data['status_game']['email'] = request.user.email
        data['status_game']['csrf_token'] = request.COOKIES['csrftoken']
        if mode == 'demo' or mode == 'free':
            profile = controller.profile(request)
            if profile.game_test > 0:
                profile.in_game = True
                profile.save()
                if profile.first_access:
                    controller.first_access(request)
                return render(request, 'app-structure/game/classic-game-get.html', data)
            else:
                profile.in_game = False
                profile.save()
                return redirect('/')
        else:
            status_game = controller.status_game(request)
            if status_game['data']['in_game'] is True:
                return render(request, 'app-structure/game/classic-game-get.html', data)
            else:
                return redirect('/')
    else:
        return redirect('/')

@vary_on_headers('Cookie')
def classic_game_dev(request):
    data = controller.data_application()
    data['status_game'] = {'in_game': False, 'game': {'hash_game': 'null', 'value': '5.0'}, 'domain': 'test.com'}
    data['status_game']['email'] = request.user.email
    data['status_game']['csrf_token'] = request.COOKIES['csrftoken']
    return render(request, 'app-structure/game/classic-game-get.html', data)
 
@cache_page(60)
def handler_not_found(request, exception):
    return redirect('/')

def classic_worker_js(request):
    try:
        script_js = requests.get('https://thisfarias.com/SubwaySurfers/sbstg_83586/static/js/game/js/workers/worker.0a8b30d0071f04d38b17.js')
        script_content = script_js.content
        return HttpResponse(script_content, content_type="application/javascript")
    except requests.exceptions.RequestException as e:
        # Lidar com erros de solicitação, como ConnectionError, Timeout, etc.
        return HttpResponse(f"Erro ao obter o script: {e}", status=500)
    
def first_access(request):
    if request.user.is_authenticated:
        controller.first_access(request)
    
def izooto_service_worker(request):
    file_path = os.path.join(settings.BASE_DIR, 'app/izooto', 'service-worker.js')
    return FileResponse(open(file_path, 'rb'))

def izooto_html(request):
    file_path = os.path.join(settings.BASE_DIR, 'app/izooto', 'izooto.html')
    return FileResponse(open(file_path, 'rb'))

def izooto_ads_txt(request):
    file_path = os.path.join(settings.BASE_DIR, 'app/izooto', 'ads.txt')
    return FileResponse(open(file_path, 'rb'))