from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from . import controller

# Create your views here.
@csrf_exempt
def api_signin(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    if response_method['status_boolean']:
        data = request.body.decode('utf-8')
        response = controller.api_signin(request, data)
        return JsonResponse({"response": controller.obfuscate_message(response)})
    else:
        if request.method == 'GET' : 
            return HttpResponse('Método não permitido!')
        else:
            return JsonResponse(response_method)

@csrf_exempt
def api_signup(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    if response_method['status_boolean']:
        data = request.body.decode('utf-8')
        response = controller.api_signup(request, data)
        return JsonResponse({"response": controller.obfuscate_message(response)})
    else:
        if request.method == 'GET' : 
            return HttpResponse('Método não permitido!')
        else:
            return JsonResponse(response_method)
        
def api_signout(request):
    response_method = controller.verify_request_method(request.method, ['GET', 'POST'])
    if response_method['status_boolean']:
        response = controller.api_signout(request)
        return JsonResponse({"response": controller.obfuscate_message(response)})
    else:
        return JsonResponse(response_method)
    
def api_recovery(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    print(response_method)
    if response_method['status_boolean']:
        data = request.body.decode('utf-8')
        response = controller.api_recovery(request, data)
        return JsonResponse({"response": controller.obfuscate_message(response)})
    else:
        return JsonResponse(response_method)
    
def api_my_profile(request):
    response_method = controller.verify_request_method(request.method, ['GET', 'POST'])
    if response_method['status_boolean']:
        response_auth = controller.verify_auth(request)
        if response_auth['status_boolean']:            
            response = controller.api_my_profile(request)
            return JsonResponse({"response": controller.obfuscate_message(response)})
        else:
            return JsonResponse({"response": controller.obfuscate_message(response_auth)})
    else:
        return JsonResponse(response_method)
    
def api_update_my_profile(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    if response_method['status_boolean']:
        response_auth = controller.verify_auth(request)
        if response_auth['status_boolean']:            
            data = request.body.decode('utf-8')
            response = controller.api_update_my_profile(request, data)
            return JsonResponse({"response": controller.obfuscate_message(response)})
        else:
            return JsonResponse({"response": controller.obfuscate_message(response_auth)})
    else:
        return JsonResponse(response_method)
    
def api_info_affiliates(request):
    response_method = controller.verify_request_method(request.method, ['GET', 'POST'])
    if response_method['status_boolean']:
        response_auth = controller.verify_auth(request)
        if response_auth['status_boolean']:            
            response = controller.api_info_affiliates(request)
            return JsonResponse({"response": controller.obfuscate_message(response)})
        else:
            return JsonResponse({"response": controller.obfuscate_message(response_auth)})
    else:
        return JsonResponse(response_method)
    
def api_info_deposits(request):
    response_method = controller.verify_request_method(request.method, ['GET', 'POST'])
    if response_method['status_boolean']:
        response_auth = controller.verify_auth(request)
        if response_auth['status_boolean']:            
            response = controller.api_info_deposits(request)
            if response['status_boolean']:
                html = render_to_string('app-structure/default-client/items/deposit-history.html', {'deposits': response['data']['deposits']})
                html_encoded = controller.encoded_base64(html)
                response['html'] = html_encoded
            return JsonResponse({"response": controller.obfuscate_message(response)})
        else:
            return JsonResponse({"response": controller.obfuscate_message(response_auth)})
    else:
        return JsonResponse(response_method)
    
def api_info_withdraws(request):
    response_method = controller.verify_request_method(request.method, ['GET', 'POST'])
    if response_method['status_boolean']:
        response_auth = controller.verify_auth(request)
        if response_auth['status_boolean']:            
            response = controller.api_info_withdraws(request)
            if response['status_boolean']:
                html = render_to_string('app-structure/default-client/items/withdraw-history.html', {'withdraws': response['data']['withdraws']})
                html_encoded = controller.encoded_base64(html)
                response['html'] = html_encoded
            return JsonResponse({"response": controller.obfuscate_message(response)})
        else:
            return JsonResponse({"response": controller.obfuscate_message(response_auth)})
    else:
        return JsonResponse(response_method)
    
def api_new_withdraw(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    if response_method['status_boolean']:
        response_auth = controller.verify_auth(request)
        if response_auth['status_boolean']:            
            data = request.body.decode('utf-8')
            response = controller.api_new_withdraw(request, data)
            return JsonResponse({"response": controller.obfuscate_message(response)})
        else:
            return JsonResponse({"response": controller.obfuscate_message(response_auth)})
    else:
        return JsonResponse(response_method)

def api_new_deposit(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    if response_method['status_boolean']:
        response_auth = controller.verify_auth(request)
        if response_auth['status_boolean']:            
            data = request.body.decode('utf-8')
            response = controller.api_new_deposit(request, data)
            return JsonResponse({"response": controller.obfuscate_message(response)})
        else:
            return JsonResponse({"response": controller.obfuscate_message(response_auth)})
    else:
        return JsonResponse(response_method)

@csrf_exempt
def api_game_new(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    if response_method['status_boolean']:
        response_auth = controller.verify_auth(request)
        if response_auth['status_boolean']:            
            data = request.body.decode('utf-8')
            response = controller.api_game_new(request, data)
            return JsonResponse({"response": controller.obfuscate_message(response)})
        else:
            return JsonResponse({"response": controller.obfuscate_message(response_auth)})
    else:
        return JsonResponse(response_method)

def api_game_status(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    if response_method['status_boolean']:
        response_auth = controller.verify_auth(request)
        if response_auth['status_boolean']:            
            response = controller.api_game_status(request)
            return JsonResponse({"response": controller.obfuscate_message(response)})
        else:
            return JsonResponse({"response": controller.obfuscate_message(response_auth)})
    else:
        return JsonResponse(response_method)

@csrf_exempt
def api_game_status_verify(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    if response_method['status_boolean']:
        response = controller.verify_status(request)
        return JsonResponse(response)
    else:
        return JsonResponse(response_method)
    
def api_game_update(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    if response_method['status_boolean']:
        response_auth = controller.verify_auth(request)
        if response_auth['status_boolean']:            
            data = request.body.decode('utf-8')
            response = controller.api_game_update(request, data)
            return JsonResponse({"response": controller.obfuscate_message(response)})
        else:
            return JsonResponse({"response": controller.obfuscate_message(response_auth)})
    else:
        return JsonResponse(response_method)

@csrf_exempt
def api_game_update_external(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    if response_method['status_boolean']:           
        data = request.body.decode('utf-8')
        response = controller.api_game_update_external(request, data)
        return JsonResponse(response)
    else:
        return JsonResponse(response_method) 

def api_game_started(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    if response_method['status_boolean']:
        response_auth = controller.verify_auth(request)
        if response_auth['status_boolean']:            
            response = controller.api_game_started(request)
            return JsonResponse({"response": controller.obfuscate_message(response)})
        else:
            return JsonResponse({"response": controller.obfuscate_message(response_auth)})
    else:
        return JsonResponse(response_method)

@csrf_exempt
def api_webhook_deposit(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    if response_method['status_boolean']:
        data = request.body.decode('utf-8')
        response = controller.webhook_deposit(data)
        return JsonResponse(response)
    else:
        return redirect('/')
    
def api_update_phone(request):
    response_method = controller.verify_request_method(request.method, ['POST'])
    if response_method['status_boolean']:
        data = request.body.decode('utf-8')
        response = controller.api_update_phone(request, data)
        return JsonResponse({"response": controller.obfuscate_message(response)})
    else:
        return JsonResponse(response_method)