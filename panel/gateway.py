import requests
from . import models
from api import controller as api_controller

def selected_gateway():
    gateway = models.configsApplication.objects.get(name='gateway_name')
    if gateway.value == 'paggue':
        return paggue()
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
        


