import requests

class integratySmsFunnel:
    def send(self, data):
        try:
            webhook = data['webhook']
            name = data['name']
            phone = str(data['phone']).replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
            email = data['email'] if 'email' in data else ''
            customized_url = data['customized_url'] if 'customized_url' in data else ''

            response = requests.post(webhook, json={
                'name': name,
                'phone': phone,
                'email': email,
                'customized_url': customized_url
            })
            print(response.text)
            return response.json()
        except Exception as e:
            print('Error SMS Funnel: ', e)