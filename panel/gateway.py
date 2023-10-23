import requests
from . import models
from api import controller as api_controller
from django.conf import settings
import base64

def selected_gateway():
    gateway = models.configsApplication.objects.get(name='gateway_name')
    if gateway.value == 'paggue':
        return paggue()
    if gateway.value == 'primepag':
        return primepag()
    else:
        return None

class paggue:
    def __init__(self):
        self.base_url = 'https://ms.paggue.io/payments/api/'
        endpoint = 'auth/login'
        url = self.base_url + endpoint
        client_key = models.configsApplication.objects.get(name='gateway_key')
        client_secret = models.configsApplication.objects.get(name='gateway_secret')
        headers = {}
        payload = {
            'client_key': client_key.value,
            'client_secret': client_secret.value,
        }

        self.s = requests.Session()
        response = self.s.post(url, headers=headers, data=payload)
        self.response_login = response.json()

        self.s.headers.update({
            'Authorization': 'Bearer {}'.format(self.response_login['access_token']),
            'X-Company-ID': str(self.response_login['user']['companies'][0]['id'])
        })

    def post(self, data):
        endpoint = 'billing_order'
        url = self.base_url + endpoint
        payload = {
            "payer_name": data['full_name'],
            "amount": int(data['value'] * 100),
            "external_id": data['external_id'],
            "description": data['description']
        }
        response = self.s.post(url, json=payload)
        details_response = response.json()

        return details_response
    
    def send(self, data):
        endpoint = 'cash-out'
        url = self.base_url + endpoint
        payload = {
            'external_id': data['external_id'],
            'amount': int(data['value'] * 100),
            'type': 1,
            'pix_key': data['pix_key'],
            'description': data['description']
        }
        response = self.s.post(url, json=payload)
        details_response = response.json()

        return details_response
    
    def balance(self):
        enpoint = 'balance'
        url = self.base_url + enpoint
        response = self.s.get(url)
        details_response = response.json()

        return details_response
    
    def compare(self, value):
        response = self.balance()
        balance = int(response['available_value'])
        value = int(float(value) * 100)
        if balance >= value:
            return True
        else:
            return False
    
    def webhook(self, data):
        data =  api_controller.load_to_json(data)

        external_id = data['external_id']
        amount = data['amount']
        status = int(data['status'])
        if status == 0:
            status = 'pending'
        elif status == 1:
            status = 'approved'
        elif status == 2 or status == 5:
            status = 'canceled'
        else:
            status = 'in_progress'

        return {
            'external_id': external_id,
            'amount': amount,
            'status': status,
        }
        
class primepag:
    def __init__(self):
        self.base_url = 'https://api-stg.primepag.com.br/' #URL BASE: homologação
        self.base_url = 'https://api.primepag.com.br/' #URL BASE: homologação
        endpoint = 'auth/generate_token'
        url = self.base_url + endpoint
        client_key = models.configsApplication.objects.get(name='gateway_key')
        client_secret = models.configsApplication.objects.get(name='gateway_secret')
        string_auth = client_key.value + ':' + client_secret.value
        string_auth_encoded = base64.b64encode(string_auth.encode('ascii')).decode('ascii')
        headers = {
            'Authorization': 'BASIC {}'.format(string_auth_encoded),
        }

        data = {
            "grant_type":"client_credentials"
        }


        self.s = requests.Session()
        response = self.s.post(url, headers=headers, data=data)
        self.response_login = response.json()

        self.s.headers.update({
            'Authorization': '{} {}'.format(self.response_login['token_type'], self.response_login['access_token'])
        })

    def post(self, data):
        endpoint = 'v1/pix/qrcodes'
        url = self.base_url + endpoint
        payload = {
            "payer_name": data['full_name'],
            "value_cents": int(data['value'] * 100),
            "reference_code": data['external_id']
        }
        response = self.s.post(url, json=payload)
        details_response = response.json()
        formated_dict = {
            'payment': details_response['qrcode']['content'],
            'external_id': details_response['qrcode']['reference_code'],
        }

        return formated_dict
    
    def send(self, data):
        endpoint = 'v1/pix/payment'
        url = self.base_url + endpoint
        payload = {
            'initiation_type': 'dict',
            'idempotent_id': api_controller.generate_hash(120),
            'value_cents': int(data['value'] * 100),
            'pix_key_type': 'cpf',
            'pix_key': data['pix_key'],
            'authorized': False
        }
        response = self.s.post(url, json=payload)
        details_response = response.json()

        return details_response
    
    def balance(self):
        enpoint = 'balance'
        url = self.base_url + enpoint
        response = self.s.get(url)
        details_response = response.json()

        return details_response
    
    def compare(self, value):
        response = self.balance()
        balance = int(response['available_value'])
        value = int(float(value) * 100)
        if balance >= value:
            return True
        else:
            return False
    
    def webhook(self, data):
        data =  api_controller.load_to_json(data)
        external_id = data['message']['reference_code']
        amount = data['message']['value_cents']
        status = data['message']['status']
        if status == 'paid':
            status = 'approved'
        elif status == 'pending':
            status = 'pending'
        elif status == 'canceled':
            status = 'canceled'

        return {
            'external_id': external_id,
            'amount': amount,
            'status': status,
        }

class ezzepay:
    def __init__(self):
        if settings.DEBUG:
            environment = 'https://api.ezzebank.com' #production
        else:
            environment = '	https://api-sandbox.ezzebank.com' #sandbox

        self.base_url = environment
        endpoint = 'oauth/token'
        url = self.base_url + endpoint
        client_key = models.configsApplication.objects.get(name='gateway_key')
        client_secret = models.configsApplication.objects.get(name='gateway_secret')
        client_key = 'eyJpZCI6IjY5ZmNhYWUyLTU3YzUtMTFlZS05YWUyLTQyMDEwYTk2MDAwYiIsIm5hbWUiOiJQQVVMTyBSSUNBUkRPIERVQVJURSBGRVJSRUlSQSAwODUyMDM4ODUyMyJ9'
        client_secret = 'wydvoRHqzgX2b6YJk0CAVLucxDTBMShiaQ1EWZOr'
        string_auth = client_key.value + ':' + client_secret.value
        string_auth_encoded = string_auth.encode('ascii')
        headers = {
            'Authorization': 'Basic {}'.format(string_auth_encoded),
        }

        data = {
            'form': 'grant_type="client_credentials"'
        }


        self.s = requests.Session()
        response = self.s.post(url, headers=headers, data=data)
        self.response_login = response.json()

        self.s.headers.update({
            'Authorization': 'Bearer {}'.format(self.response_login['access_token']),
            'X-Company-ID': str(self.response_login['user']['companies'][0]['id'])
        })

    def post(self, data):
        endpoint = 'billing_order'
        url = self.base_url + endpoint
        payload = {
            "payer_name": data['full_name'],
            "amount": int(data['value'] * 100),
            "external_id": data['external_id'],
            "description": data['description']
        }
        response = self.s.post(url, json=payload)
        details_response = response.json()

        return details_response
    
    def send(self, data):
        endpoint = 'cash-out'
        url = self.base_url + endpoint
        payload = {
            'external_id': data['external_id'],
            'amount': int(data['value'] * 100),
            'type': 1,
            'pix_key': data['pix_key'],
            'description': data['description']
        }
        response = self.s.post(url, json=payload)
        details_response = response.json()

        return details_response
    
    def balance(self):
        enpoint = 'balance'
        url = self.base_url + enpoint
        response = self.s.get(url)
        details_response = response.json()

        return details_response
    
    def compare(self, value):
        response = self.balance()
        balance = int(response['available_value'])
        value = int(float(value) * 100)
        if balance >= value:
            return True
        else:
            return False
    
    def webhook(self, data):
        data =  api_controller.load_to_json(data)

        external_id = data['external_id']
        amount = data['amount']
        status = int(data['status'])
        if status == 0:
            status = 'pending'
        elif status == 1:
            status = 'approved'
        elif status == 2 or status == 5:
            status = 'canceled'
        else:
            status = 'in_progress'

        return {
            'external_id': external_id,
            'amount': amount,
            'status': status,
        }

