from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import controller

# Create your views here.
def index(request):
    if request.user.is_authenticated and request.user.is_superuser:
        data = controller.application_info()
        #controller.delete_db()
        #controller.change_profile_email()
        return render(request, 'admin/default-admin/index.html', data)
    else:
        return redirect('/')
    
def users(request):
    if request.user.is_authenticated and request.user.is_superuser:
        data = controller.application_info()
        return render(request, 'admin/default-admin/users.html', data)
    else:
        return redirect('/')
    
def withdraws(request):
    if request.user.is_authenticated and request.user.is_superuser:
        data = controller.application_info()
        return render(request, 'admin/default-admin/withdraws.html', data)
    else:
        return redirect('/')
    
def affiliates(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'admin/default-admin/affiliates.html')
    else:
        return redirect('/')
    
def configs(request):
    if request.user.is_authenticated and request.user.is_superuser:
        data = controller.application_info()
        return render(request, 'admin/default-admin/configs.html', data)
    else:
        return redirect('/')
    
def dashboards(request):
    if request.user.is_authenticated and request.user.is_superuser:
        dash = controller.verify_param(request, 'dash')
        response = controller.get_metrics(dash)
        return render(request, 'admin/personalized/dashboards/{}.html'.format(dash), response)
    else:
        return JsonResponse({'error': 'Not authorized'}, status=401)
    
def get_withdraws(request):
    if request.user.is_authenticated and request.user.is_superuser:
        data = request.body.decode('utf-8')
        response = controller.get_withdraws(data)
        return render(request, 'admin/personalized/withdraw/query.html', response)
    else:
        return JsonResponse({'error': 'Not authorized'}, status=401)

def get_users(request):
    if request.user.is_authenticated and request.user.is_superuser:
        data = request.body.decode('utf-8')
        response = controller.get_users(data)
        return render(request, 'admin/personalized/users/filtered.html', response)
    else:
        return JsonResponse({'error': 'Not authorized'}, status=401)
    
def get_info_user(request):
    if request.user.is_authenticated and request.user.is_superuser:
        data = request.body.decode('utf-8')
        response = controller.get_info_user(data)
        return render(request, 'admin/personalized/users/info.html', response)
    else:
        return JsonResponse({'error': 'Not authorized'}, status=401)
    
def get_affiliates(request):
    if request.user.is_authenticated and request.user.is_superuser:
        data = request.body.decode('utf-8')
        response = controller.get_affiliates(data)
        return render(request, 'admin/personalized/affiliates/filtered.html', response)
    else:
        return JsonResponse({'error': 'Not authorized'}, status=401)

def get_info_affiliates(request):
    if request.user.is_authenticated and request.user.is_superuser:
        data = request.body.decode('utf-8')
        response = controller.get_info_affiliates(request, data)
        data = response['data']
        return render(request, 'admin/personalized/affiliates/info.html', data)
    else:
        return JsonResponse({'error': 'Not authorized'}, status=401)

def update_user(request):
    if request.user.is_authenticated and request.user.is_superuser:
        data = request.body.decode('utf-8')
        response = controller.update_user(data)
        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Not authorized'}, status=401)
    
def update_withdraw(request):
    if request.user.is_authenticated and request.user.is_superuser:
        data = request.body.decode('utf-8')
        response = controller.api_update_withdraw(data)
        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Not authorized'}, status=401)
       
def update_configs(request):
    if request.user.is_authenticated and request.user.is_superuser:
        data = request.body.decode('utf-8')
        response = controller.api_update_configs(data)
        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Not authorized'}, status=401)
    
def start_configs(request):
    controller.create_fields_configs()
    return redirect('/')

@csrf_exempt
def receiver_new_user(request):
    data = request.body.decode('utf-8')
    response = controller.receiver_data_user(data)
    return JsonResponse(response)

@csrf_exempt
def receiver_new_deposit(request):
    data = request.body.decode('utf-8')
    response = controller.receiver_deposit(data)
    return JsonResponse(response)

@csrf_exempt
def set_affiliates(request):
    data = request.body.decode('utf-8')
    response = controller.receiver_set_affiliate(data)
    return JsonResponse(response)