from . import models
import datetime
from api import smsFunnel as api_smsFunnel

def verify_deposits_minutes(request):
    while True:
        deposits = models.deposits.objects.filter(status='pending')
        for deposit in deposits:
            external_id = str(deposit.external_id)
            query = models.smsFunnel.objects.filter(external_id=external_id)
            if query.exists() is False:
                profile = models.profile.objects.get(user=deposit.user)
                created_at = deposit.created_at
                now = datetime.datetime.now()
                url = request.build_absolute_uri('/') + 'deposit/' + external_id
                if now > (created_at + datetime.timedelta(minutes=2)):
                    data = {
                        'webhook': models.configsApplication.objects.get(name='pix_generated').value,
                        'name': profile.name,
                        'phone': profile.phone,
                        'email': profile.email,
                        'customized_url': url
                    }
                    response = api_smsFunnel.integratySmsFunnel().send(data)

def verify_one_deposit_deactivate(request):
    profiles = models.profile.objects.all()
    for profile in profiles:
        deposits = models.deposits.objects.filter(user=profile.user)
        if deposits.exists():
            games = models.game.objects.filter(user=profile.user).order_by('-created_at')
            if games.exists():
                last_game = games[0]
                now = datetime.datetime.now()
                if now > (last_game.created_at + datetime.timedelta(days=2)):
                    data = {
                        'webhook': models.configsApplication.objects.get(name='new_register').value,
                        'name': profile.name,
                        'phone': profile.phone,
                        'email': profile.email,
                        'customized_url': ''
                    }

                    

            

