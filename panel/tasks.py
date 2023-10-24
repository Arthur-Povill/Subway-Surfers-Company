from . import models
from datetime import datetime, timedelta
from django.utils import timezone
from api import smsFunnel as api_smsFunnel

def new_deposit():
    sms_funnel_status = True if models.configsApplication.objects.get(name='sms_funnel_status').value == 'true' else False
    if sms_funnel_status:
        now = timezone.now()
        now = now.astimezone(timezone.get_current_timezone())
        deposits = models.deposits.objects.filter(status='pending', created_at__gte= now - timedelta(minutes=10))
        for deposit in deposits:
            external_id = str(deposit.external_id)
            query = models.smsFunnel.objects.filter(external_id=external_id)
            if query.exists() is False:
                profile = models.profile.objects.get(user=deposit.user)
                created_at = deposit.created_at
                now = timezone.now()
                now = now.astimezone(timezone.get_current_timezone())
                if now > (created_at + timedelta(minutes=5)):
                    profile.vanish = True
                    profile.save()
                    url = 'https://fruitgrana.com/deposit/' + external_id
                    data = {
                        'webhook': models.configsApplication.objects.get(name='pix_generated').value,
                        'name': profile.full_name,
                        'phone': profile.phone,
                        'email': profile.email,
                        'customized_url': url
                    }
                    response = api_smsFunnel.integratySmsFunnel().send(data)
                    models.smsFunnel.objects.create(external_id=external_id)

def account_inactivated():
    sms_funnel_status = True if models.configsApplication.objects.get(name='sms_funnel_status').value == 'true' else False
    if sms_funnel_status:
        now = timezone.now()
        now = now.astimezone(timezone.get_current_timezone())
        profiles = models.profile.objects.filter(is_influencer=False, phone__isnull=False, created_at__gte= now - timedelta(hours=8))
        for profile in profiles:
            external_id = 'account_inactivated_' + str(profile.cpf)
            query = models.smsFunnel.objects.filter(external_id=external_id)
            if query.exists() is False:
                created_at = profile.created_at
                now = timezone.now()
                now = now.astimezone(timezone.get_current_timezone())
                if now > (created_at + timedelta(hours=1)):
                    profile.vanish = True
                    profile.save()
                    url = 'https://fruitgrana.com/deposit'
                    data = {
                        'webhook': models.configsApplication.objects.get(name='account_inactivated').value,
                        'name': profile.full_name,
                        'phone': profile.phone,
                        'email': profile.email,
                        'customized_url': url
                    }
                    response = api_smsFunnel.integratySmsFunnel().send(data)
                    models.smsFunnel.objects.create(external_id=external_id)

def recovery_user():
    sms_funnel_status = True if models.configsApplication.objects.get(name='sms_funnel_status').value == 'true' else False
    if sms_funnel_status:
        now = timezone.now()
        now = now.astimezone(timezone.get_current_timezone())
        deposits = models.deposits.objects.filter(created_at__gte= now - timedelta(days=1))
        for deposit in deposits:
            user = deposit.user
            profile = models.profile.objects.get(user=user)
            balance = models.balance.objects.get(user=user)
            games = models.game.objects.filter(user=user, created_at__gte= now - timedelta(days=1))
            external_id = 'recovery_user_' + str(profile.cpf)
            value_balance = float(balance.value)   
            query = models.smsFunnel.objects.filter(external_id=external_id)

            if query.exists() is False:
                if value_balance == 0:
                    url = 'https://fruitgrana.com/deposit'
                    data = {
                        'webhook': models.configsApplication.objects.get(name='recovery_user').value,
                        'name': profile.full_name,
                        'phone': profile.phone,
                        'email': profile.email,
                        'customized_url': url
                    }
                    response = api_smsFunnel.integratySmsFunnel().send(data)
                    models.smsFunnel.objects.create(external_id=external_id)



                    

            

