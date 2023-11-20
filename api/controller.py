from django.contrib.auth import authenticate, login as loginProcess, logout as logoutProcess
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from . import smsFunnel, emailController
from panel import gateway
import json
import base64
from django.conf import settings
from panel import models as admin_models
import string
import random
import datetime
import hashlib
import secrets
import qrcode
import io
import requests
from urllib.parse import urlparse
import os

'''
    ----------- Defaults Vars, lists and Dict  ------------
'''
SUB_MAP = {
    " ": "Z", "Z": " ", ",": "a", "a": ",", "Y": "<", "<": "Y", "*": "/", "/": "*", 
    "\u000b": "F", "F": "\u000b", "N": "5", "5": "N", "D": "l", "l": "D", "+": "m", 
    "m": "+", "S": "W", "W": "S", "|": ";", ";": "|", ">": "_", "_": ">", "e": "j", 
    "j": "e", "%": "p", "p": "%", "6": "L", "L": "6", "7": "H", "H": "7", "~": "U", "U": 
    "~", "h": "k", "k": "h", "1": ")", ")": "1", "w": "T", "T": "w", "O": "A", "A": "O", 
    "[": "y", "y": "[", "v": "q", "q": "v", "c": "$", "$": "c", 
    "g": "}", "}": "g", "E": "M", "M": "E", "G": "u", "u": "G", 
    "!": "R", "R": "!", "-": "Q", "Q": "-", "]": "^", "^": "]", "n": ".", ".": "n", 
    "J": "`", "`": "J", "o": "?", "?": "o", "x": "0", "0": "x", "d": "s", "s": "d", 
    "r": "t", "t": "r", "K": "8", "8": "K", "b": "V", "V": "b", "\\": "@", "@": "\\", 
    "I": ":", ":": "I", "9": "C", "C": "9", "f": "#", "#": "f", "P": "=", "=": "P", 
    "{": "z", "z": "{", "i": "&", "&": "i", "3": "4", "4": "3", "(": "2", "2": "(", 
    "B": "X", "X": "B", 
}

'''
    ----------- Function to treat variables, dictionary, strings  ------------
'''
def delete_session(username):
    sessions = Session.objects.all(username=username)
    for s in sessions:
        session_decode = s.get_decoded()
        query = User.objects.get(username=username)
        id = query.id
        if int(session_decode['_auth_user_id']) == int(id):
            s.delete()


    return {
        'status': True,
        'message': 'Sessões removidas com sucesso!',
        'containers': {}
    }

def generate_hash(size=16):
    random_bytes = secrets.token_bytes(size)
    sha256 = hashlib.sha256()
    sha256.update(random_bytes)
    hash_result = sha256.hexdigest()

    return hash_result

def obfuscate_message(message):
    message = str(message)
    text = ''
    for char in message:
        if char in SUB_MAP:
            text += SUB_MAP[char]
        else:
            text += char
    
    return text

def deobfuscate_message(message):
    message = str(message)
    text = ''
    for char in message:
        if char in SUB_MAP:
            text += SUB_MAP[char]
        else:
            text += char
    return text

def encoded_base64(message):
    encoded_text = base64.b64encode(message.encode('utf-8')).decode('utf-8')
    return encoded_text

def decode_base64(message):
    decoded_text = base64.b64decode(message).decode('utf-8')
    return decoded_text

def load_to_json(data):
    try:
        data = json.loads(data)
    except:
        try:
            data = json.load(data)
        except:
            pass
    return data

def verify_request_method(method, authorized_method):
    if method in authorized_method:
        status = 200
        status_boolean = True
        message = 'Método autorizado!'
        data = {}
    else:
        status = 405
        status_boolean = False
        message = 'Método não autorizado!'
        data = {}

    return {
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def verify_auth(request):
    if request.user.is_authenticated:
        status = 200
        status_boolean = True
        message = 'Usuário autenticado!'
        data = {}
    else:
        status = 401
        status_boolean = False
        message = 'Usuário não autenticado!'
        data = {}

    return {
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def verify_admin(request):
    if request.user.is_superuser:
        status = 200
        status_boolean = True
        message = 'Usuário autorizado!'
        data = {}
    else:
        status = 401
        status_boolean = False
        message = 'Usuário não autorizado!'
        data = {}

    return {
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def verify_infos(target, value):
    if value is not None and value != '':
        verify_created = False
        if target == 'email':
            if '@' in value:
                prefix = '@' + value.split('@')[1]
                permited_emails = [
                    '@hotmail.com', 
                    '@hotmail.com.br', 
                    '@gmail.com', 
                    '@outlook.com', 
                    '@yahoo.com',
                    '@icloud.com',
                    '@aol.com'
                ]
                if prefix in permited_emails:
                    verify_created = True
                else:
                    status = 400
                    status_boolean = False
                    message = 'E-mail não está dentro das normas do site!'
                    data = {}
            else:
                status = 400
                status_boolean = False
                message = 'E-mail não está dentro das normas do site!'
                data = {}
        elif target == 'password':
            if len(value) >= 8:
                if any(char.isupper() for char in value):
                    if any(char.islower() for char in value):
                        if any(char.isdigit() for char in value):
                            if any(not char.isalnum() for char in value):
                                status = 200
                                status_boolean = True
                                message = 'Senha dentro da normas do site!'
                                data = {}
                            else:
                                status = 400
                                status_boolean = False
                                message = 'Senha não possui caracteres especiais!'
                                data = {}
                        else:
                            status = 400
                            status_boolean = False
                            message = 'Senha não possui números!'
                            data = {}
                    else:
                        status = 400
                        status_boolean = False
                        message = 'Senha não possui letras minúsculas!'
                        data = {}
                else:
                    status = 400
                    status_boolean = False
                    message = 'Senha não possui letras maiúsculas!'
                    data = {}
            else:
                status = 400
                status_boolean = False
                message = 'Senha não possui 8 caracteres!'
                data = {}
        elif target == 'full_name':
            if len(value.split(' ')) >= 2:
                status = 200
                status_boolean = True
                message = 'Nome completo dentro da normas do site!'
                data = {}
            else:
                status = 400
                status_boolean = False
                message = 'Nome incompleto não possui nome e sobrenome!'
                data = {}
        elif target == 'phone':
            desformated_value = str(value).replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
            if len(desformated_value) >= 10 and len(desformated_value) <= 12:
                verify_created = True
            else:
                status = 400
                status_boolean = False
                message = 'Insira um telefone válido!'
                data = {}
        elif target == 'cpf':
            if len(value) >= 11:
                verify_created = True
            else:
                status = 400
                status_boolean = False
                message = 'CPF não possui 11 caracteres!'
                data = {}
    else:
        status = 400
        status_boolean = False
        message = 'Campo {} não foi informado!'.format(target)
        data = {}

    if verify_created:
        response = verify_infos_exists(target, value)
        status = response['status']
        status_boolean = response['status_boolean']
        message = response['message']
        data = response['data']

    return {
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def verify_users(key, value, qtd=None):
    users = User.objects.filter(email=value)
    if users.exists():
        status = 200
        status_boolean = True
        message = 'Usuário encontrado!'
        data = {
            'user': users.first() if qtd is None else users[:qtd]
        }
    else:
        status = 404
        status_boolean = False
        message = 'Usuário não encontrado!'
        data = {} 

    return {
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def verify_infos_exists(target, value):
    if value is not None and value != '':
        query_users = admin_models.profile.objects.filter(**{target: value})
        if query_users.exists() is False:
            status = 200
            status_boolean = True
            message = 'Campo {} não está cadastrado!'.format(target)
            data = {
                'permited_register': True
            }
        else:
            status = 200
            status_boolean = True
            message = 'Campo {} já está cadastrado!'.format(target)
            data = {
                'permited_register': False
            }
    else:
        status = 400
        status_boolean = False
        message = 'Campo {} não foi informado!'.format(target)
        data = {}

    return {
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def format_currency_brazilian(number):
    try:
        number = float(number)
    except:
        pass

    a = '{:,.2f}'.format(number)
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')

def desformat_currency_brazilian(number):
    number = number.replace('R$', '')
    number = number.replace('.', '')
    number = number.replace(',', '.')
    return float(number)

'''
    ----------- Main Functions API client  ------------
'''

def set_force_password(email):
    profiles = admin_models.profile.objects.filter(email=email)
    for profile in profiles:
        user = profile.user
        user.set_password(profile.password)
        user.save()

def api_signin(request, data, encrypted=True):  
    if encrypted:
        data = load_to_json(data)
        data = deobfuscate_message(data['response'])
        data = load_to_json(data)
    else:
        data = load_to_json(data)

    email = data['email'].lower()
    password = data['password']
    if email is not None and email != '': 
        if password is not None and password != '':
            query_users = verify_users('email', email)
            if query_users['status_boolean']:
                user = authenticate(username=email, password=password)
                if user is not None:
                    loginProcess(request, user)
                    status = 200
                    status_boolean = True
                    message = 'Usuário autenticado com sucesso!'
                    data = {
                        'username': user.username
                    }
                else:
                    status = 401
                    status_boolean = False
                    message = 'Usuários ou senha inválidos'
                    data = {}
            else:
                status = query_users['status']
                status_boolean = query_users['status_boolean']
                message = 'Usuários ou senha inválidos'
                data = query_users['data']
        else:
            status = 400
            status_boolean = False
            message = 'Senha não informada!'
            data = {}            
    else:
        status = 400
        status_boolean = False
        message = 'Email não informado!'
        data = {}
        
    return {
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }        

def api_signup(request, data, encrypted=True):  
    if encrypted:
        data = load_to_json(data)
        data = deobfuscate_message(data['response'])
        data = load_to_json(data)
    else:
        data = load_to_json(data)

    ip = request.META.get('REMOTE_ADDR')
    email = data['email'].lower()
    password = data['password']
    if 'full_name' in data:
        full_name = data['full_name']
    else:
        full_name = ''
    if 'phone' in data: 
        phone = data['phone']
    else:
        phone = ''
    if 'cpf' in data:
        cpf = data['cpf']
    else:
        cpf = ''
    if 'afilliated_code' in data:
        afilliated_code = data['afilliated_code']
    else:
        afilliated_code = ''
    print(afilliated_code)

    if 'other' in data:
        other = data['other']
    else:
        other = False

    if 'after_signup' in data:
        after_signup = data['after_signup']
    else:
        after_signup = False

    if other == False:
        verify_email = verify_infos('email', email)
        if verify_email['status_boolean']:
            if verify_email['data']['permited_register']:
                verify_password = verify_infos('password', password)
                if verify_password['status_boolean']:
                    verify_full_name = verify_infos('full_name', full_name)
                    if verify_full_name['status_boolean']:
                        verify_phone = verify_infos('phone', phone)
                        if verify_phone['status_boolean']:
                            if verify_phone['data']['permited_register']:
                                verify_cpf = verify_infos('cpf', cpf)
                                if verify_cpf['status_boolean']:
                                    if verify_cpf['data']['permited_register']:
                                        user_exists = User.objects.filter(username=email).exists()
                                        if user_exists:
                                            status = 400
                                            status_boolean = False
                                            message = 'E-mail já cadastrado!'
                                            data = {}
                                        else:
                                            user = User.objects.create_user(email, email, password)
                                            first_name = full_name.split(' ')[0]
                                            last_name = full_name.split(' ')[1] if len(full_name.split(' ')) > 1 else ''
                                            user.first_name = first_name
                                            user.last_name = last_name
                                            user.save()

                                            user_profile = admin_models.profile.objects.filter(email=email).first()
                                            user_profile.phone = phone
                                            user_profile.email = email
                                            user_profile.password = password
                                            user_profile.cpf = cpf
                                            user_profile.save()

                                            if afilliated_code != '' or afilliated_code != None:
                                                user_affiliate = admin_models.affiliate.objects.filter(email=email).first()
                                                user_affiliate.code = generate_afilliate_code()
                                                user_affiliate.save()

                                            status = 200
                                            status_boolean = True
                                            message = 'Usuário cadastrado com sucesso!'
                                            data = {
                                                'user': user.username
                                            }

                                            if after_signup:
                                                api_signin(request, {'email': email, 'password': password}, encrypted=False)
                                    else:
                                        status = verify_cpf['status']
                                        status_boolean = verify_cpf['status_boolean']
                                        message = verify_cpf['message']
                                        data = verify_cpf['data']
                                else:
                                    status = False
                                    status_boolean = 401
                                    message = verify_cpf['message']
                                    data = verify_cpf['data']
                            else:
                                status = False
                                status_boolean = 401
                                message = verify_phone['message']
                                data = verify_phone['data']
                        else:
                            status = verify_phone['status']
                            status_boolean = verify_phone['status_boolean']
                            message = verify_phone['message']
                            data = verify_phone['data']
                    else:
                        status = verify_full_name['status']
                        status_boolean = verify_full_name['status_boolean']
                        message = verify_full_name['message']
                        data = verify_full_name['data']
                else:
                    status = verify_password['status']
                    status_boolean = verify_password['status_boolean']
                    message = verify_password['message']
                    data = verify_password['data']
            else:
                status = verify_email['status']
                status_boolean = verify_email['status_boolean']
                message = verify_email['message']
                data = verify_email['data']
        else:
            status = verify_email['status']
            status_boolean = verify_email['status_boolean']
            message = verify_email['message']
            data = verify_email['data']
    else:
        verify_email = verify_infos('email', email)
        if verify_email['status_boolean']:
            if verify_email['data']['permited_register']:
                verify_password = verify_infos('password', password)
                if verify_password['status_boolean'] or password != '':
                    user_exists = User.objects.filter(email=email).exists()
                    if user_exists:
                        status = 400
                        status_boolean = False
                        message = 'E-mail já cadastrado!'
                        data = {}
                    else:
                        user = User.objects.create_user(email, email, password)
                        user.save()

                        user_profile = admin_models.profile.objects.filter(email=email).first()
                        user_profile.phone = ''
                        user_profile.email = email
                        user_profile.password = password
                        user_profile.cpf = ''
                        user_profile.full_name = ''
                        if afilliated_code != '' or afilliated_code != None:
                            afilliated = admin_models.affiliate.objects.filter(code=afilliated_code)
                            if afilliated.exists():
                                afilliated = afilliated.first()
                                user_profile.affiliate_email = afilliated.email
                        user_profile.save()

                        user_affiliate = admin_models.affiliate.objects.filter(email=email).first()
                        user_affiliate.code = generate_afilliate_code()
                        user_affiliate.save()

                        status = 200
                        status_boolean = True
                        message = 'Usuário cadastrado com sucesso!'
                        data = {
                            'user': user.username
                        }

                        if after_signup:
                            api_signin(request, {'email': email, 'password': password}, encrypted=False)

                else:
                    status = 400
                    status_boolean = False
                    message = verify_password['message']
                    data = verify_password['data']
            else:
                status = 400
                status_boolean = False
                message = verify_email['message']
                data = verify_email['data']
        else:
            status = 400
            status_boolean = False
            message = verify_email['message']
            data = verify_email['data']

    return {
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def api_signout(request):
    api_verify_session(request.user, close=True)
    logoutProcess(request)
    status = 200
    status_boolean = True
    message = 'Usuário deslogado com sucesso!'
    data = {}

    return {
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def api_recovery(request, data, encrypted=True):
    if encrypted:
        data = load_to_json(data)
        data = deobfuscate_message(data['response'])
        data = load_to_json(data)
    else:
        data = load_to_json(data)

    email = data['email'].lower()
    query = admin_models.profile.objects.filter(email=email)
    
    if query.exists():
        profile = query.first()
        name = profile.full_name
        if name is None or name == '':
            name = 'Usuário'
        password = profile.password
        app_name = admin_models.configsApplication.objects.get(name='app_name').value
        msg = '''
        Olá {nome}!

        A senha cadastrada é {senha} 

        Não compartilhe sua senha com estranhos. Ela garante a segurança de sua conta.

        Esta é uma mensagem automática, não responda a este e-mail.

        Att,
        Equipe {app_name}
        '''.format(nome=name, senha=password, app_name=app_name)

        email_controller = emailController.email()
        email_controller.send(email, 'Recuperação de senha', msg)
        
        status = 200
        status_boolean = True
        message = 'Sua senha foi enviado para o seu e-mail! Verifique sua caixa de spam.'
        data = {}
    else:
        status = 404
        status_boolean = False
        message = 'E-mail não encontrado!'
        data = {}

    return {
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def api_verify_session(username, close=False):
    status = 404
    status_boolean = False
    message = 'Nenhuma sessão foi encontrada!'
    data = {}

    sessions = Session.objects.all()
    for session in sessions:
        session_data = session.get_decoded()
        if session_data.get('_auth_user_id') == str(username.id):
            status = 200
            status_boolean = True
            data = {}
            if close:
                session.delete()
                message = 'Sessão encontrada e fechada com sucesso!'
            else:
                message = 'Sessão encontrada!'
            break

    return {
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def api_my_profile(request):
    user = request.user
    email = user.email
    user_profile = admin_models.profile.objects.filter(email=email).first()
    user_balance = admin_models.balance.objects.filter(email=email).first()
    
    data = {
        'user': {
            'full_name': user_profile.full_name if user_profile.full_name != None else '',
            'influencer': user_profile.is_influencer,
            'cpf': user_profile.cpf if user_profile.cpf != None else '',
            'phone': user_profile.phone if user_profile.phone != None else '',
            'email': user_profile.email,
        },
        'balance':{
            'value': format_currency_brazilian(user_balance.value),
            'value_float': user_balance.value,
            'value_affiliate': format_currency_brazilian(user_balance.value_affiliate),
        }
    }

    status = 200
    status_boolean = True
    message = 'Usuário encontrado com sucesso!'
    data = data

    return{
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def api_info_affiliates(request):
    url = request.build_absolute_uri()
    user = request.user
    email = user.email
    affiliate = admin_models.affiliate.objects.get(email=email)  
    balance = admin_models.balance.objects.get(email=email)       
    data = {
        'code': affiliate.code,
        'link': url.replace('partnership/', '') + 'join/' + affiliate.code,
        'total_earning': format_currency_brazilian(affiliate.total_earnings),
        'total_eaning_day': format_currency_brazilian(affiliate.total_earnings_day),
        'total_earning_month': format_currency_brazilian(affiliate.total_earnings_month),
        'total_earning_last_month': format_currency_brazilian(affiliate.total_earnings_last_month),
        'cpa_count': affiliate.cpa_count,
        'cpa_percent': int(affiliate.cpa_percent),
        'cpa_total': format_currency_brazilian(affiliate.cpa_total),
        'cpa_day': format_currency_brazilian(affiliate.cpa_day),
        'cpa_month': format_currency_brazilian(affiliate.cpa_month),
        'cpa_last_month': format_currency_brazilian(affiliate.cpa_last_month),
        'revshare_percent': int(affiliate.revshare_percent),
        'revshare_total': format_currency_brazilian(affiliate.revshare_total),
        'revshare_day': format_currency_brazilian(affiliate.revshare_day),
        'revshare_month': format_currency_brazilian(affiliate.revshare_month),
        'revshare_last_month': format_currency_brazilian(affiliate.revshare_last_month),
        'indication_percent': int(affiliate.indication_percent),
        'indication_count': format_currency_brazilian(affiliate.indication_total),
        'indication_total': format_currency_brazilian(affiliate.indication_total),
        'value': format_currency_brazilian(balance.value),
        'value_affiliate': format_currency_brazilian(balance.value_affiliate),
    }

    status = 200
    status_boolean = True
    message = 'Usuário encontrado com sucesso!'
    data = data
    
    return{
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def api_update_my_profile(request, data, encrypted=True):
    if encrypted:
        data = load_to_json(data)
        data = deobfuscate_message(data['response'])
        data = load_to_json(data)
    else:
        data = load_to_json(data)

    changed = False
    status = None
    user = request.user
    profile = admin_models.profile.objects.filter(email=email).first()

    full_name = data['full_name']
    email = data['email'].lower()
    phone = data['phone']

    if full_name != profile.full_name:
        verify_full_name = verify_infos('full_name', full_name)
        if verify_full_name['status_boolean']:
            profile.full_name = full_name
            splited_name = full_name.split(' ')
            user.first_name = splited_name[0]
            user.last_name = splited_name[len(splited_name) - 1]
            changed = True
        else:
            status = verify_full_name['status']
            status_boolean = verify_full_name['status_boolean']
            message = verify_full_name['message']
            r_data = verify_full_name['data']
    
    if email != profile.email:
        verify_email = verify_infos('email', email)
        if verify_email['status_boolean']:
            profile.email = email
            user.email = email
            changed = True
        else:
            status = verify_email['status']
            status_boolean = verify_email['status_boolean']
            message = verify_email['message']
            r_data = verify_email['data']

    if phone != profile.phone:
        verify_phone = verify_infos('phone', phone)
        if verify_phone['status_boolean']:
            profile.phone = phone
            changed = True
        else:
            status = verify_phone['status']
            status_boolean = verify_phone['status_boolean']
            message = verify_phone['message']
            r_data = verify_phone['data']

    if changed:
        profile.save()
        user.save()
        status = 200
        status_boolean = True
        message = 'Usuário atualizado com sucesso!'
        r_data = {}
    else:
        if status is None:
            status = 400
            status_boolean = True
            message = 'Nenhum campo foi alterado!'
            r_data = {}

    return{
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': r_data
    }

def api_info_deposits(request):
    user = request.user
    email = user.email
    deposits = admin_models.deposits.objects.filter(email=email)

    data = {
        'deposits': []
    }
    for deposit in deposits:
        data['deposits'].append({
            'ID': deposit.id,
            'value': format_currency_brazilian(deposit.value),
            'status': deposit.status,
            'created_at': deposit.created_at.strftime('%d/%m/%Y %H:%M:%S')
        })

    status = 200
    status_boolean = True
    message = 'Usuário encontrado com sucesso!'
    data = data

    return{
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def get_info_deposit(request, data, encrypted=True):
    if encrypted:
        data = load_to_json(data)
        data = deobfuscate_message(data['response'])
        data = load_to_json(data)
    else:
        data = load_to_json(data)

    external_id = data['external_id']
    deposit = admin_models.deposits.objects.filter(external_id=external_id).first()
    if deposit is not None:
        status = 200
        status_boolean = True
        message = 'Deposito encontrado com sucesso!'
        data = {
            'qr_code': deposit.qr_code,
            'value': format_currency_brazilian(deposit.value),
            'pix_code': deposit.pix_code,
            'status': deposit.status,
        }
    else:
        status = 404
        status_boolean = False
        message = 'Deposito não encontrado!'
        data = {}

    return{
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def api_info_withdraws(request):
    user = request.user
    email = user.email
    withdraws = admin_models.withdraw.objects.filter(email=email)

    data = {
        'withdraws': []
    }
    for withdraw in withdraws:
        data['withdraws'].append({
            'value': format_currency_brazilian(withdraw.value),
            'status': withdraw.status,
            'created_at': withdraw.created_at.strftime('%d/%m/%Y %H:%M:%S'),
            'details': withdraw.details if withdraw.details is not None else '-'
        })

    status = 200
    status_boolean = True
    message = 'Usuário encontrado com sucesso!'
    data = data

    return{
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def api_new_deposit(request, data, encrypted=True):
    if encrypted:
        data = load_to_json(data)
        data = deobfuscate_message(data['response'] )
        data = load_to_json(data)
    else:
        data = load_to_json(data)

    user = request.user
    email = user.email
    profile = admin_models.profile.objects.filter(email=email).first()
    
    try:
        value = float(data['value'].replace('R$ ', '').replace('.', '').replace(',', '.'))
    except:
        return {
            'status': 400,
            'status_boolean': False,
            'message': 'Valor não informado!',
            'data': {}
        }
    
    name = data['name']
    cpf = data['cpf']
    if profile.full_name == '' and profile.cpf == '':
        profile.full_name = name
        profile.cpf = cpf
        profile.save()
    permited_deposit = admin_models.configsApplication.objects.filter(name='permited_deposit').first()
    value_permited_deposit = float(desformat_currency_brazilian(permited_deposit.value))
    if value >= value_permited_deposit:
        external_id = generate_hash()
        player_name = data['name']
        description = 'Deposito do jogo da frutinha!'
        parsed_uri = urlparse(request.build_absolute_uri())
        scheme = parsed_uri.scheme
        scheme = parsed_uri.scheme
        scheme = 'https' if scheme == 'http' else scheme
        domain = parsed_uri.netloc
        domain_url = f"{scheme}://{domain}/"
        gateway_selected = gateway.selected_gateway()
        response = gateway_selected.post({
            'full_name': 'Jogo da Frutinha - {}'.format(player_name),
            'cpf': cpf,
            'value': value,
            'external_id': external_id,
            'description': description,
            'email': email,
            'domain_url': domain_url
        }) 
        external_id = response['external_id']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(response['payment'])
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        image_buffer = io.BytesIO()
        img.save(image_buffer, format='PNG')
        base64_image = base64.b64encode(image_buffer.getvalue()).decode('utf-8')

        new_deposit = admin_models.deposits.objects.create(
            external_id=external_id,
            email=email,
            value=value,
            pix_code=response['payment'],
            qr_code=base64_image
        )

        send_sms = True if admin_models.configsApplication.objects.filter(name='sms_funnel_status').first().value == 'true' else False
        if send_sms is True:
            parsed_uri = urlparse(request.build_absolute_uri())
            scheme = parsed_uri.scheme
            domain = parsed_uri.netloc
            domain_url = f"{scheme}://{domain}/"

            data_sms = {
                'webhook': admin_models.configsApplication.objects.filter(name='pix_generated').first().value,
                'name': profile.full_name,
                'phone': profile.phone,
                'email': profile.email,
                'customized_url': domain_url + 'deposit/{}'.format(external_id),
            }
            smsFunnel.integratySmsFunnel().send(data_sms)
            #admin_models.smsFunnel.objects.create(external_id=external_id)


        status = 200
        status_boolean = True
        message = 'Deposito criado com sucesso!'
        data = {
            'qr_code': new_deposit.qr_code,
            'value': format_currency_brazilian(value),
            'pix_code': new_deposit.pix_code,
            'external_id': new_deposit.external_id,
        }
    else:
        status = 400
        status_boolean = False
        message = 'Valor mínimo para deposito é de R$ {}'.format(format_currency_brazilian(value_permited_deposit))
        data = {}

    return{
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def api_new_withdraw(request, data, encrypted=True):    
    user = request.user
    email = user.email
    withdraws = admin_models.withdraw.objects.filter(email=email)
    today = datetime.datetime.now()
    permited = True
    if withdraws.exists():
        for withdraw in withdraws:
            if withdraw.created_at.day == today.day and withdraw.created_at.month == today.month and withdraw.created_at.year == today.year:
                permited = False
                if withdraw.status == 'pending':
                    status = 400
                    status_boolean = False
                    message = 'Você já possui um saque pendente!'
                    data = {}
                    break
                elif withdraw.status == 'approved':
                    status = 400
                    status_boolean = False
                    message = 'Você já realizou um saque hoje!'
                    data = {}
                    break
                else:
                    status = 400
                    status_boolean = False
                    message = 'Você já solicitou saque hoje, tente novamente amanhã!'
                    data = {}
                    break

    if permited:
        if encrypted:
            data = load_to_json(data)
            data = deobfuscate_message(data['response'])
            data = load_to_json(data)
        else:
            data = load_to_json(data)

        deposits = admin_models.deposits.objects.filter(email=email, status='approved')
        profile = admin_models.profile.objects.filter(email=email).first()
        if deposits.exists():
            value_deposit = 0
            counted = 0
            for deposit in deposits:
                value_deposit += float(deposit.value)
                if counted == 3:
                    break
            meta_value = value_deposit * 4
        else:
            if profile.is_influencer is True:
                meta_value = 0
            else:
                return {
                    'status': 400,
                    'status_boolean': False,
                    'message': 'Você precisa ao menos realizar um depósito para solicitar saque!',
                    'data': {}
                }

        try:
            value = float(data['value'].format('R$ ', '').replace('.', '').replace(',', '.'))
        except:
            return {
                'status': 400,
                'status_boolean': False,
                'message': 'Valor não informado!',
                'data': {}
            }
        
        permited_withdraw = admin_models.configsApplication.objects.filter(name='permited_withdraw').first()
        value_permited_withdraw = float(desformat_currency_brazilian(permited_withdraw.value))
        if value >= value_permited_withdraw:
            balance = admin_models.balance.objects.filter(email=email).first()
            balance_value = float(balance.value) if profile.is_influencer is False else float(balance.value_affiliate)
            if balance_value >= value:
                if balance_value >= meta_value:
                    if balance.permited_withdraw:
                        if profile.is_influencer is False:
                            value_withdraw = value - (value * 0.1)
                        else:
                            value_withdraw = value - (value * 0.1)
                        new_withdraw = admin_models.withdraw.objects.create(
                            email=email, 
                            value=value_withdraw
                        )

                        if profile.cpf == '' or profile.cpf is None:
                            profile.cpf = data['cpf']
                            profile.save()
                        
                        if profile.is_influencer is False:
                            balance.value = balance_value - value
                        else:
                            balance.value_affiliate = balance_value - value
                        balance.save()

                        status = 200
                        status_boolean = True
                        message = 'Saque realizado com sucesso!'
                        data = {
                            'value': format_currency_brazilian(balance.value)
                        }
                    else:
                        status = 400
                        status_boolean = False
                        message = 'Você não está autorizado para realizar saque!'
                        data = {}
                else:
                    status = 400
                    status_boolean = False
                    message = 'Você não atingiu a meta de R${}! Falta muito pouco R${}'.format(format_currency_brazilian(meta_value), format_currency_brazilian(meta_value - value))
                    data = {}
            else:
                status = 400
                status_boolean = False
                message = 'Você não possui saldo suficiente para realizar o saque!'
                data = {}
        else:
            status = 400
            status_boolean = False
            message = 'Valor mínimo para saque é de R$ {}'.format(format_currency_brazilian(value_permited_withdraw))
            data = {}
        
    return {
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def api_game_new(request, data, encrypted=True):
    if encrypted:
        data = load_to_json(data)
        data = deobfuscate_message(data['response'])
        data = load_to_json(data)
    else:
        data = load_to_json(data)

    try:
        value = float(data['value'].format('R$ ', '').replace('.', '').replace(',', '.'))
    except:
        return {
            'status': 400,
            'status_boolean': False,
            'message': 'Valor não informado!',
            'data': {}
        }
    
    user = request.user
    email = user.email
    mode_game = data['mode']
    balance = admin_models.balance.objects.filter(email=email).first()
    balance_value = float(balance.value)
    if value >= 1:
        if balance_value >= value:
            games = admin_models.game.objects.filter(email=email, is_finished=False)
            profile = admin_models.profile.objects.filter(email=email).first()
            if profile.is_influencer is False and balance_value < 1:
                external_id = 'recovery_user_' + str(profile.cpf)
                parsed_uri = urlparse(request.build_absolute_uri())
                scheme = parsed_uri.scheme
                domain = parsed_uri.netloc
                domain_url = f"{scheme}://{domain}/"
                data_sms = {
                    'webhook': admin_models.configsApplication.objects.filter(name='recovery_user').first().value,
                    'name': profile.full_name,
                    'phone': profile.phone,
                    'email': profile.email,
                    'customized_url': domain_url + 'deposit',
                }
                smsFunnel.integratySmsFunnel().send(data_sms)
                
            game_count = games.count()
            if profile.in_game is False and game_count == 0:
                new_game = admin_models.game.objects.create(
                    email=email, 
                    bet=value,
                    hash_game=generate_hash(),
                )

                profile.in_game = True
                profile.save()

                balance.value = balance_value - value
                balance.save()

                status = 200
                status_boolean = True
                message = 'Jogo criado com sucesso!'
                data = {
                    'hash_game': new_game.hash_game,
                    'value': format_currency_brazilian(balance.value)
                }

            else:
                profile.in_game = True
                profile.save()
                status = 400
                status_boolean = False
                message = 'Você já possui um jogo ativo!'
                data = {
                    'action': 'playing'
                }
        else:
            status = 400
            status_boolean = False
            message = 'Você não possui saldo suficiente para realizar o jogo!'
            data = {
                'action': 'deposit'
            }
    else:
        status = 400
        status_boolean = False
        message = 'Valor mínimo para jogar é de R$ 1,00'
        data = {
            'action': 'deposit'
        }

    return {
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def api_game_status(request):
    user = request.user
    email = user.email
    profile = admin_models.profile.objects.filter(email=email).first()
    if profile.in_game:
        games = admin_models.game.objects.filter(email=email, is_finished=False)
        if games.exists():
            game = games.first()
            if game.is_started is False:
                status = 200
                status_boolean = True
                message = 'Usuário está com o jogo ativo!'
                data = {
                    'in_game': profile.in_game,
                    'game': {
                        'hash_game': game.hash_game,
                        'value': float(game.bet), 
                    }
                }
            else:
                game.is_finished = True
                profile.in_game = False
                game.save()
                profile.save()

                status = 400
                status_boolean = False
                message = 'Usuário está com o jogo inativo!'
                data = {
                    'in_game': profile.in_game,
                    'game': {
                        'hash_game': game.hash_game,
                        'value': float(game.bet), 
                    }
                }
        else:
            profile.in_game = False
            profile.save()
            status = 400
            status_boolean = False
            message = 'Usuário está com o jogo ativo, mas não existe jogo!'
            data = {
                'in_game': profile.in_game,
            }
    else:
        status = 400
        status_boolean = False
        message = 'Usuário está com o jogo inativo!'
        data = {
            'in_game': profile.in_game,
        }

    return{
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def api_game_update(request, data, encrypted=True):
    user = request.user
    email = user.email
    profile = admin_models.profile.objects.filter(email=email).first()
    game = admin_models.game.objects.filter(email=email, is_finished=False).first()

    if encrypted:
        data = load_to_json(data)
        data = deobfuscate_message(data['response'])
        data = load_to_json(data)
    else:
        data = load_to_json(data)
        
    if profile.in_game:
        if data['hash_game'] == game.hash_game:
            status_game = data['status']
            if status_game == 'started':
                game.is_started = True
                game.save()

                status = 200
                status_boolean = True
                message = 'Jogo iniciado com sucesso!'
                data = {
                    'in_game': profile.in_game,
                    'game': {
                        'hash_game': game.hash_game,
                        'value': game.bet, 
                    }
                }
            elif status_game == 'finished' and game.is_started:
                win = True if data['win'] == 'true' else False
                game.win = win
                if win:
                    bet_value = float(game.bet)
                    gain = bet_value * 1.5
                    game.payout = gain - bet_value
                    balance = admin_models.balance.objects.filter(email=email).first()
                    balance.value = float(balance.value) + gain
                    balance.save()

                game.is_finished = True
                game.save()

                profile.in_game = False
                profile.save()


                status = 200
                status_boolean = True
                message = 'Jogo encerrado com sucesso!'
                data = {
                    'in_game': profile.in_game,
                    'game': {
                        'hash_game': game.hash_game,
                        'value': game.bet, 
                    }
                }
        else:
            status = 400
            status_boolean = False
            message = 'O jogo não confere com o game atual!'
            data = {}
    else:
        status = 400
        status_boolean = False
        message = 'Usuário está com o jogo inativo!'
        data = {}

    return{
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def api_game_started(request, data, encrypted=True):
    user = request.user
    email = user.email
    profile = admin_models.profile.objects.filter(email=email).first()
    game = admin_models.game.objects.filter(email=email, is_finished=False).first()

    if encrypted:
        data = load_to_json(data)
        data = deobfuscate_message(data['response'])
        data = load_to_json(data)
    else:
        data = load_to_json(data)

    if profile.in_game:
        if data['hash_game'] == game.hash_game:
            game.is_started = True
            game.save()

            status = 200
            status_boolean = True
            message = 'Usuário está com o jogo ativo!'
            data = {
                'in_game': profile.in_game,
                'game': {
                    'hash_game': game.hash_game,
                    'value': game.bet, 
                }
            }
        else:
            status = 400
            status_boolean = False
            message = 'O jogo não confere com o game atual!'
            data = {}
    else:
        status = 400
        status_boolean = False
        message = 'Usuário está com o jogo inativo!'
        data = {}

    return{
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

def webhook_deposit(data):
    gateway_selected = gateway.selected_gateway()
    data = gateway_selected.webhook(data)
    external_id = data['external_id']
    status = data['status']
    try:
        amount = data['amount']
    except:
        amount = 0

    deposit_query = admin_models.deposits.objects.filter(external_id=external_id)
    if deposit_query.exists():
        deposit = deposit_query.first()
        deposit.status = status
        if status == 'approved':
            email = deposit.email
            balance = admin_models.balance.objects.get(email=email)
            profile = admin_models.profile.objects.get(email=email)
            
            value = deposit.value
            if value >= 20 and value < 50:
                value += 20
            elif value  >= 50 and value < 100:
                value += 60
            elif value >= 100:
                value + 125
                
            balance.value = balance.value + value
            send_sms = True if admin_models.configsApplication.objects.filter(name='sms_funnel_status').first().value == 'true' else False
            if send_sms is True:
                data_sms = {
                    'webhook': admin_models.configsApplication.objects.filter(name='pix_approved').first().value,
                    'name': profile.full_name,
                    'phone': profile.phone,
                    'email': profile.email
                }
                smsFunnel.integratySmsFunnel().send(data_sms)
                    
            if profile.affiliate_email != None and profile.affiliate_email != '':
                email_affiliated = profile.affiliate_email
                profile_affiliated_main = admin_models.profile.objects.get(email=email_affiliated)
                affiliated_main = admin_models.affiliate.objects.get(email=email_affiliated)
                balance_affiliated_main = admin_models.balance.objects.get(email=email_affiliated)

                if int(profile.qt_deposit) == 0:
                    profile.first_deposit = True
                    if deposit.value >= 20:
                        cpa_value = 18 if profile.is_influencer is True else 16
                        calculation = (deposit.value * (affiliated_main.cpa_percent / 100))
                        if calculation > cpa_value:
                            calculation = cpa_value

                        #Add gains in affiliates
                        if profile_father.is_influencer is True:
                            balance_affiliated_father.value_affiliate += calculation
                        else:
                            balance_affiliated_father.value += calculation
                        affiliated_main.total_earnings += calculation
                        affiliated_main.cpa_total += calculation
                        affiliated_main.cpa_count += 1
                        
                        today = datetime.datetime.now()
                        if affiliated_main.last_update != today:
                            affiliated_main.total_earning_day = calculation
                            affiliated_main.cpa_day = calculation
                        else:
                            affiliated_main.total_earning_day += calculation
                            affiliated_main.cpa_day += calculation

                        if today.month == affiliated_main.last_update.month:
                            affiliated_main.total_earning_month += calculation
                            affiliated_main.cpa_month += calculation
                        else:
                            affiliated_main.total_earnings_last_month = affiliated_main.total_earning_month
                            affiliated_main.cpa_last_month = affiliated_main.cpa_month
                            affiliated_main.total_earning_month = calculation
                            affiliated_main.cpa_month = calculation

                        #Add gains by indication
                        if profile_affiliated_main.affiliate_email != None and profile_affiliated_main.affiliate_email != '':
                            email_father = profile_affiliated_main.affiliate_email
                            balance_affiliated_father= admin_models.balance.objects.get(email=email_father)
                            affiliated_father = admin_models.affiliate.objects.get(email=email_father)
                            profile_father = admin_models.profile.objects.get(email=email_father)

                            calculation = (deposit.value * (affiliated_father.indication_percent / 100))
                            balance_affiliated_father.value_affiliate = balance_affiliated_father.value_affiliate + calculation

                            if profile_father.is_influencer is True:
                                balance_affiliated_father.value_affiliate += calculation
                            else:
                                balance_affiliated_father.value += calculation
                            affiliated_father.total_earnings += calculation
                            affiliated_father.indication_total += calculation
                            affiliated_father.indication_count += 1
                            
                            today = datetime.datetime.now()
                            if affiliated_main.last_update != today:
                                affiliated_main.total_earning_day = calculation
                            else:
                                affiliated_main.total_earning_day += calculation

                            if today.month == affiliated_main.last_update.month:
                                affiliated_main.total_earning_month += calculation
                            else:
                                affiliated_main.total_earnings_last_month = affiliated_main.total_earning_month
                                affiliated_main.total_earning_month = calculation
                            
                            balance_affiliated_father.save()
                            affiliated_father.save()

                profile.qt_deposit += 1
                profile.save()
                affiliated_main.save()
                balance_affiliated_main.save()
            balance.save()
            
        deposit.save()

        status = 200
        status_boolean = True
        message = 'Deposito atualizado com sucesso!'
        data = {
            'external_id': external_id,
            'status': status,
            'amount': amount
        }
    else:
        status = 400
        status_boolean = False
        message = 'Deposito não encontrado!'
        data = {}

    return{
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }    

def api_update_phone(request, data, encrypted=True):
    if encrypted:
        data = load_to_json(data)
        data = deobfuscate_message(data['response'])
        data = load_to_json(data)
    else:
        data = load_to_json(data)

    phone = data['phone']
    name = data['name']
    user = request.user
    email = user.email
    profile = admin_models.profile.objects.filter(email=email).first()
    if profile.phone == None or profile.phone == '':
        verify_phone = verify_infos('phone', phone)
        if verify_phone['status_boolean']:
            profile.full_name = name
            profile.phone = phone.replace(' ', '')
            profile.save()
            send_sms = True if admin_models.configsApplication.objects.filter(name='sms_funnel_status').first().value == 'true' else False
            if send_sms is True:
                parsed_uri = urlparse(request.build_absolute_uri())
                scheme = parsed_uri.scheme
                domain = parsed_uri.netloc
                domain_url = f"{scheme}://{domain}/"
                data_sms = {
                    'webhook': admin_models.configsApplication.objects.filter(name='account_inactivated').first().value,
                    'name': profile.full_name,
                    'phone': profile.phone,
                    'email': profile.email,
                    'customized_url': domain_url + 'deposit',
                }
                response = smsFunnel.integratySmsFunnel().send(data_sms)

            status = 200
            status_boolean = True
            message = 'Telefone atualizado com sucesso!'
            data = {}
        else:
            status = verify_phone['status']
            status_boolean = verify_phone['status_boolean']
            message = verify_phone['message']
            data = verify_phone['data']
    else:
        status = 400
        status_boolean = False
        message = 'Telefone já cadastrado!'
        data = {}

    return{
        'status': status,
        'status_boolean': status_boolean,
        'message': message,
        'data': data
    }

'''
    ----------- Controller User ------------
'''
def first_access(request):
    user = request.user
    email = user.email
    user_profile = admin_models.profile.objects.filter(email=email).first()
    user_profile.first_access = False
    user_profile.save()
    return {
        'status': 200,
        'status_boolean': True,
        'message': 'Usuário atualizado com sucesso!',
        'data': {}
    }

def generate_afilliate_code(length=6):
    list_codes = all_afilliate_codes()
    caracteres = string.ascii_letters + string.digits
    while True:
        codigo = ''.join(random.choice(caracteres) for _ in range(length))
        if codigo not in list_codes:
            return codigo
    
def all_afilliate_codes():
    affiliates = admin_models.affiliate.objects.all()
    list_codes = []
    for affiliate in affiliates:
        list_codes.append(affiliate.code)
    
    return list_codes

def application_info():
    data = {
        'app_email': admin_models.configsApplication.objects.get(name='app_email').value,
        'app_name':  admin_models.configsApplication.objects.get(name='app_name').value,
        'app_name_separated':  admin_models.configsApplication.objects.get(name='app_name_separated').value,
        'gateway_secret': admin_models.configsApplication.objects.get(name='gateway_secret').value,
        'gateway_token': admin_models.configsApplication.objects.get(name='gateway_key').value,
        'gateway_name': admin_models.configsApplication.objects.get(name='gateway_name').value,
        'permited_deposit': admin_models.configsApplication.objects.get(name='permited_deposit').value,
        'permited_withdraw': admin_models.configsApplication.objects.get(name='permited_withdraw').value,
        'support_link': admin_models.configsApplication.objects.get(name='support_link').value,
        'support_link_affiliates': admin_models.configsApplication.objects.get(name='support_link_affiliates').value,
        'link_group': admin_models.configsApplication.objects.get(name='link_group').value,
        'copy_get_phone': admin_models.configsApplication.objects.get(name='copy_get_phone').value,
        'sms_funnel_status': True if admin_models.configsApplication.objects.get(name='sms_funnel_status').value == 'true' else False,
        'smtp_host_recovery': admin_models.configsApplication.objects.get(name='smtp_host_recovery').value,
        'smtp_port_recovery': admin_models.configsApplication.objects.get(name='smtp_port_recovery').value,
        'smtp_email_recovery': admin_models.configsApplication.objects.get(name='smtp_email_recovery').value,
        'smtp_password_recovery': admin_models.configsApplication.objects.get(name='smtp_password_recovery').value,
        'static_url': settings.STATIC_URL,
    }
    return data

def config_application():
   '''data = {
        'app_email': admin_models.configsApplication.objects.get(name='app_email').value,
        'app_name':  admin_models.configsApplication.objects.get(name='app_name').value,
        'app_name_separated':  admin_models.configsApplication.objects.get(name='app_name_separated').value,
        'gateway_secret': admin_models.configsApplication.objects.get(name='gateway_secret').value,
        'gateway_token': admin_models.configsApplication.objects.get(name='gateway_key').value,
        'gateway_name': admin_models.configsApplication.objects.get(name='gateway_name').value,
        'permited_deposit': admin_models.configsApplication.objects.get(name='permited_deposit').value,
        'permited_withdraw': admin_models.configsApplication.objects.get(name='permited_withdraw').value,
        'support_link': admin_models.configsApplication.objects.get(name='support_link').value,
        'support_link_affiliates': admin_models.configsApplication.objects.get(name='support_link_affiliates').value,
        'link_group': admin_models.configsApplication.objects.get(name='link_group').value,
        'copy_get_phone': admin_models.configsApplication.objects.get(name='copy_get_phone').value,
        'sms_funnel_status': True if admin_models.configsApplication.objects.get(name='sms_funnel_status').value == 'true' else False,
        'smtp_host_recovery': admin_models.configsApplication.objects.get(name='smtp_host_recovery').value,
        'smtp_port_recovery': admin_models.configsApplication.objects.get(name='smtp_port_recovery').value,
        'smtp_email_recovery': admin_models.configsApplication.objects.get(name='smtp_email_recovery').value,
        'smtp_password_recovery': admin_models.configsApplication.objects.get(name='smtp_password_recovery').value,
        'static_url': settings.STATIC_URL,
    }

    if data['sms_funnel_status']:
        data['pix_generated'] = admin_models.configsApplication.objects.get(name='pix_generated').value
        data['account_inactivated'] = admin_models.configsApplication.objects.get(name='account_inactivated').value
        data['recovery_user'] = admin_models.configsApplication.objects.get(name='recovery_user').value'''
   pass

def application_info_user():
    data = {
        'app_email': admin_models.configsApplication.objects.get(name='app_email').value,
        'app_name':  admin_models.configsApplication.objects.get(name='app_name').value,
        'app_name_separated':  admin_models.configsApplication.objects.get(name='app_name_separated').value,
        'permited_deposit': admin_models.configsApplication.objects.get(name='permited_deposit').value,
        'permited_withdraw': admin_models.configsApplication.objects.get(name='permited_withdraw').value,
        'support_link': admin_models.configsApplication.objects.get(name='support_link').value,
        'support_link_affiliates': admin_models.configsApplication.objects.get(name='support_link_affiliates').value,
        'link_group': admin_models.configsApplication.objects.get(name='link_group').value,
        'copy_get_phone': admin_models.configsApplication.objects.get(name='copy_get_phone').value,
        'static_url': settings.STATIC_URL,
    }

    return data

