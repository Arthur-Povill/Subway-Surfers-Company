from . import models
from . import gateway
from api import controller as api_controller
import datetime

def verify_param(request, param):
    try:
        param = request.GET.get(param, None)
    except:
        param = None
    return param

def get_metrics(dash):
    balances = models.balance.objects.all()
    deposits = models.deposits.objects.all()
    games = models.game.objects.all()
    profiles = models.profile.objects.all()
    withdraws = models.withdraw.objects.all()

    if dash == 'gains':
        dict_gains = {
            'users': 0,
            'home': 0,
            'game_today': 0,
            'count_game_today': 0, 
            'game_week': 0,
            'count_game_week': 0,
            'game_month': 0,
            'count_game_month': 0,
            'game_total': 0,
            'count_game_total': 0,
        }

        for balance in balances:
            profile = models.profile.objects.get(user=balance.user)
            if balance.permited_withdraw and profile.is_influencer is False:
                dict_gains['users'] += balance.value

        for deposit in deposits:
            if deposit.status == 'approved':
                dict_gains['home'] += deposit.value

        for game in games:
            profile = models.profile.objects.get(user=game.user)
            if profile.is_influencer is False:
                dict_gains['game_total'] += game.bet
                dict_gains['count_game_total'] += 1

                if game.created_at.date() == datetime.date.today():
                    dict_gains['game_today'] += game.bet
                    dict_gains['count_game_today'] += 1

                if game.created_at.date() >= datetime.date.today() - datetime.timedelta(days=7):
                    dict_gains['game_week'] += game.bet
                    dict_gains['count_game_week'] += 1

                if game.created_at.date() >= datetime.date.today() - datetime.timedelta(days=30):
                    dict_gains['game_month'] += game.bet
                    dict_gains['count_game_month'] += 1

        dict_gains['users'] = api_controller.format_currency_brazilian(dict_gains['users'])
        dict_gains['home'] = api_controller.format_currency_brazilian(dict_gains['home'])
        dict_gains['game_today'] = api_controller.format_currency_brazilian(dict_gains['game_today'])
        dict_gains['game_week'] = api_controller.format_currency_brazilian(dict_gains['game_week'])
        dict_gains['game_month'] = api_controller.format_currency_brazilian(dict_gains['game_month'])
        dict_gains['game_total'] = api_controller.format_currency_brazilian(dict_gains['game_total'])

        metrics = dict_gains
    elif dash == 'registers':
        dict_new_users = {
            'today': 0,
            'week': 0,
            'month': 0,
            'last_month': 0,
            'total': 0,
        }

        for profile in profiles:
            if profile.created_at.date() == datetime.date.today():
                dict_new_users['today'] += 1

            if profile.created_at.date() >= datetime.date.today() - datetime.timedelta(days=7):
                dict_new_users['week'] += 1

            if profile.created_at.date() >= datetime.date.today() - datetime.timedelta(days=30):
                dict_new_users['month'] += 1

            if profile.created_at.date() >= datetime.date.today() - datetime.timedelta(days=60):
                dict_new_users['last_month'] += 1

            dict_new_users['total'] += 1

        metrics = dict_new_users
    elif dash == 'deposits':
        dict_deposits = {
            'first_deposit': 0,
            'count_first_deposit': 0, 
            'today': 0,
            'count_today': 0, 
            'week': 0,
            'count_week': 0,
            'month': 0,
            'count_month': 0,
            'total': 0,
            'count_total': 0,
        }
        filtered_users = []
        for deposit in deposits:
            if deposit.status == 'approved':
                if deposit.user not in filtered_users:
                    filtered_users.append(deposit.user)
                    dict_deposits['first_deposit'] += deposit.value
                    dict_deposits['count_first_deposit'] += 1
                    
                if deposit.created_at.date() == datetime.date.today():
                    dict_deposits['today'] += deposit.value
                    dict_deposits['count_today'] += 1
                
                if deposit.created_at.date() >= datetime.date.today() - datetime.timedelta(days=7):
                    dict_deposits['week'] += deposit.value
                    dict_deposits['count_week'] += 1

                if deposit.created_at.date() >= datetime.date.today() - datetime.timedelta(days=30):
                    dict_deposits['month'] += deposit.value
                    dict_deposits['count_month'] += 1

                dict_deposits['total'] += deposit.value
                dict_deposits['count_total'] += 1

        dict_deposits['first_deposit'] = api_controller.format_currency_brazilian(dict_deposits['first_deposit'])
        dict_deposits['today'] = api_controller.format_currency_brazilian(dict_deposits['today'])
        dict_deposits['week'] = api_controller.format_currency_brazilian(dict_deposits['week'])
        dict_deposits['month'] = api_controller.format_currency_brazilian(dict_deposits['month'])
        dict_deposits['total'] = api_controller.format_currency_brazilian(dict_deposits['total'])
        metrics = dict_deposits
    elif dash == 'withdraws':
        dict_withdraws = {
            'approved': 0,
            'count_approved': 0,
            'recused': 0,
            'count_recused': 0,
            'pending': 0,
            'count_pending': 0,
        }

        for withdraw in withdraws:
            if withdraw.status == 'approved':
                dict_withdraws['approved'] += withdraw.value
                dict_withdraws['count_approved'] += 1
            elif withdraw.status == 'canceled':
                dict_withdraws['recused'] += withdraw.value
                dict_withdraws['count_recused'] += 1
            else:
                dict_withdraws['pending'] += withdraw.value
                dict_withdraws['count_pending'] += 1
                    
        dict_withdraws['approved'] = api_controller.format_currency_brazilian(dict_withdraws['approved'])
        dict_withdraws['recused'] = api_controller.format_currency_brazilian(dict_withdraws['recused'])

        metrics = dict_withdraws
        
    return{
        'metrics': metrics
    }

def get_withdraws(data=None):
    if data != None and data != '':
        data = api_controller.load_to_json(data)
        query = data['query'].lower()
        if query == '':
            withdraws = models.withdraw.objects.all()
        else:
            withdraws = models.withdraw.objects.filter(user__username__icontains=query)
    else:
        withdraws = models.withdraw.objects.all()

    dict_withdraws = []
    for withdraw in withdraws:
        item = {}
        profile = models.profile.objects.get(user=withdraw.user)
        item['id'] = withdraw.id
        item['full_name'] = profile.full_name
        item['email'] = profile.email
        item['influencer'] = profile.is_influencer
        item['value'] = api_controller.format_currency_brazilian(withdraw.value)
        item['status'] = withdraw.status
        
        withdraw_user = models.withdraw.objects.filter(user=withdraw.user, status='approved')
        all_withdraw = 0
        for w in withdraw_user:
            all_withdraw += w.value
        item['all_withdraw'] = api_controller.format_currency_brazilian(all_withdraw)
        dict_withdraws.append(item)

    dict_withdraws = sorted(dict_withdraws, key=lambda k: (k['status'] == 'pending', k['influencer']), reverse=True)
    return {
        'withdraws': dict_withdraws
    }

def get_users(data=None):
    if data != None and data != '':
        data = api_controller.load_to_json(data)
        query = data['query'].lower()
        print(query)
        if query == '':
            profiles = models.profile.objects.all()
        else:
            profiles = models.profile.objects.filter(user__username__icontains=query)
    else:
        profiles = models.profile.objects.all()

    dict_users = []
    '''ranged = 50
    for i in range(ranged):
        try:
            profile = profiles[i]
            balance = models.balance.objects.get(user=profile.user)
            item = {}
            item['id'] = profile.user.id
            item['full_name'] = profile.full_name
            item['email'] = profile.user.email
            item['activated'] = profile.user.is_active
            item['influencer'] = profile.is_influencer
            item['balance'] = api_controller.format_currency_brazilian(balance.value)
            item['permited_withdraw'] = balance.permited_withdraw
            item['created_at'] = profile.created_at.strftime('%d/%m/%Y %H:%M:%S')
            deposits = models.deposits.objects.filter(user=profile.user, status='approved')
            item['deposited'] = True if len(deposits) > 0 else False
            dict_users.append(item)
        except:
            break'''
    
    #get last 50 users
    ranged = 50
    for i in range(len(profiles) - ranged, len(profiles)):
        profile = profiles[i]
        balance = models.balance.objects.get(user=profile.user)
        item = {}
        item['id'] = profile.user.id
        item['full_name'] = profile.full_name
        item['email'] = profile.user.email
        item['activated'] = profile.user.is_active
        item['influencer'] = profile.is_influencer
        item['balance'] = api_controller.format_currency_brazilian(balance.value)
        item['permited_withdraw'] = balance.permited_withdraw
        item['created_at'] = profile.created_at.strftime('%d/%m/%Y %H:%M:%S')
        deposits = models.deposits.objects.filter(user=profile.user, status='approved')
        item['deposited'] = True if len(deposits) > 0 else False
        dict_users.append(item)


    dict_users = sorted(dict_users, key=lambda k: k['created_at'], reverse=True)
    
    return {
        'users': dict_users
    }

def get_info_user(data):
    data = api_controller.load_to_json(data)
    id_user = data['id_user']
    user = models.profile.objects.get(user__id=id_user)
    balance = models.balance.objects.get(user__id=id_user)
    affiliate = models.affiliate.objects.get(user__id=id_user)

    dict_user = {
        'profile': {
            'id': user.user.id,
            'full_name': user.full_name,
            'email': user.user.email,
            'cpf': user.cpf,
            'phone': user.phone,
            'activated': user.user.is_active,
            'influencer': user.is_influencer,

        },
        'balance': {
            'value': api_controller.format_currency_brazilian(balance.value),
            'permited_withdraw': balance.permited_withdraw,
        },
        'affiliate': {
            'code': affiliate.code,
            'cpa_percent': int(affiliate.cpa_percent) if affiliate.cpa_percent % 2 == 0 else str(affiliate.cpa_percent).replace('.', ','),
            'revshare_percent': int(affiliate.revshare_percent) if affiliate.revshare_percent % 2 == 0 else str(affiliate.revshare_percent).replace('.', ','),
        }
    }

    return{
        'metrics': dict_user
    }

def update_user(data):
    try:
        data = api_controller.load_to_json(data)
        id_user = data['id_user']
        influencer = data['influencer']
        activated = data['activated']
        full_name = data['full_name']
        email = data['email']
        cpf = data['cpf']
        phone = data['phone']
        code_affiliate = data['code_affiliate']
        permited_withdraw = data['permited_withdraw']
        cpa_percent = float(data['cpa_percent'].replace(',', '.'))
        revshare_percent = float(data['revshare_percent'].replace(',', '.'))
        value = float(api_controller.desformat_currency_brazilian(data['value_balance']))

        user = models.profile.objects.get(user__id=id_user)
        user.user.is_active = activated
        user.user.save()
        user.full_name = full_name
        user.user.email = email
        user.cpf = cpf
        user.phone = phone
        user.is_influencer = influencer
        user.save()

        balance = models.balance.objects.get(user__id=id_user)  
        balance.permited_withdraw = permited_withdraw
        balance.value = value
        balance.save()

        affiliate = models.affiliate.objects.get(user__id=id_user)
        affiliate.code = code_affiliate
        affiliate.cpa_percent = cpa_percent
        affiliate.revshare_percent = revshare_percent
        affiliate.save()

        return {
            'status': 200,
            'message': 'Usuário atualizado com sucesso!',
            'data': {}
        }
    except Exception as e:
        return {
            'status': 500,
            'message': 'Erro ao atualizar o usuário!',
            'data': {
                'error': str(e)
            }
        }

def get_affiliates(data=None):
    if data != None and data != '':
        data = api_controller.load_to_json(data)
        query = data['query'].lower()
        if query == '':
            profiles = models.profile.objects.filter(is_influencer=True)
        else:
            profiles = models.profile.objects.filter(is_influencer=True, user__username__icontains=query)
    else:
        profiles = models.profile.objects.all()

    dict_users = []
    for profile in profiles:
        balance = models.balance.objects.get(user=profile.user)
        item = {}
        item['id'] = profile.user.id
        item['full_name'] = profile.full_name
        item['email'] = profile.user.email
        item['balance'] = api_controller.format_currency_brazilian(balance.value)
        item['balance_affiliate'] = api_controller.format_currency_brazilian(balance.value_affiliate)
        dict_users.append(item)
    
    return {
        'users': dict_users
    }

def get_info_affiliates_1(data):
    data = api_controller.load_to_json(data)
    id_user = data['id_user']
    user = models.profile.objects.get(user__id=id_user)
    balance = models.balance.objects.get(user__id=id_user)
    affiliate = models.affiliate.objects.get(user__id=id_user)

    dict_user = {
        'profile': {
            'id': user.user.id,
            'full_name': user.full_name,
            'email': user.user.email,
            'cpf': user.cpf,
            'phone': user.phone,
            'activated': user.user.is_active,
            'influencer': user.is_influencer,

        },
        'balance': {
            'value': api_controller.format_currency_brazilian(balance.value),
            'permited_withdraw': balance.permited_withdraw,
        },
        'affiliate': {
            'code': affiliate.code,
            'cpa_percent': int(affiliate.cpa_percent) if affiliate.cpa_percent % 2 == 0 else str(affiliate.cpa_percent).replace('.', ','),
            'revshare_percent': int(affiliate.revshare_percent) if affiliate.revshare_percent % 2 == 0 else str(affiliate.revshare_percent).replace('.', ','),
        }
    }

    return{
        'metrics': dict_user
    }

def get_info_affiliates(request, data):
    data = api_controller.load_to_json(data)
    id_user = data['id_user']
    url = request.build_absolute_uri()
    user = models.profile.objects.get(user__id=id_user)
    affiliate = models.affiliate.objects.get(user=user.user)
    profiles = models.profile.objects.filter(affiliate_user=affiliate)
    deposits = models.deposits.objects.filter(affiliate_user=affiliate, status='approved')

    #Earnings
    month_now = datetime.datetime.now().month
    total_earning = 0
    total_earning_month = 0
    total_earning_last_month = 0

    #For CPA
    cpa_deposits = 0
    cpa_total_earnings = 0
    cpa_total_earnings_month = 0
    cpa_percent = affiliate.cpa_percent / 100

    #For Revenue Share
    revshare_count = 0
    revshare_total_earnings = 0
    revshare_total_earnings_month = 0
    revshare_percent = affiliate.revshare_percent / 100

    list_users = []

    for deposit in deposits:
        if deposit.user not in list_users:
            selected_percent = cpa_percent
            cpa_deposits += 1
            cpa_total_earnings += deposit.value * cpa_percent
            if deposit.created_at.month == month_now:
                cpa_total_earnings_month += deposit.value * cpa_percent
            list_users.append(deposit.user)
        else:
            selected_percent = revshare_percent
            revshare_total_earnings += deposit.value * revshare_percent
            if deposit.created_at.month == month_now:
                revshare_total_earnings_month += deposit.value * revshare_percent
                revshare_count += 1

        total_earning += deposit.value * selected_percent
        if deposit.created_at.month == month_now:
            total_earning_month += deposit.value * selected_percent
        elif deposit.created_at.month == month_now - 1:
            total_earning_last_month += deposit.value * selected_percent
    
    profile = models.profile.objects.get(user=user.user)
    full_name = profile.full_name if profile.full_name != '' or profile.full_name != None else 'Usuário'
    data = {
        'full_name': full_name,
        'code': affiliate.code,
        'link': url + '?affiliate=' + affiliate.code,
        'total_earning': api_controller.format_currency_brazilian(total_earning),
        'total_earning_month': api_controller.format_currency_brazilian(total_earning_month),
        'total_earning_last_month': api_controller.format_currency_brazilian(total_earning_last_month),
        'cpa_percent': int(affiliate.cpa_percent),
        'cpa_count': len(profiles),
        'cpa_deposits': int(cpa_deposits),
        'cpa_total_earnings': api_controller.format_currency_brazilian(cpa_total_earnings),
        'cpa_total_earnings_month': api_controller.format_currency_brazilian(cpa_total_earnings_month),
        'revshare_percent': int(affiliate.revshare_percent),
        'revshare_count': int(revshare_count),
        'revshare_total_earnings': api_controller.format_currency_brazilian(revshare_total_earnings),
        'revshare_total_earnings_month': api_controller.format_currency_brazilian(revshare_total_earnings_month),
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


def api_update_withdraw(data):
    data = api_controller.load_to_json(data)
    id_withdraw = data['id']
    status = data['status']

    withdraw = models.withdraw.objects.get(id=id_withdraw)
    if withdraw.status == 'approved':
        permited_withdraw = withdraw.user.balance.permited_withdraw
        if permited_withdraw:
            value = withdraw.value
            gateway_selected = gateway.selected_gateway()
            authorized_withdraw = gateway_selected.compare(value)
            if authorized_withdraw:
                player_name = withdraw.user.profile.full_name
                external_id = api_controller.generate_hash()
                description = 'Saque realizado por {} no valor de R${}'.format(player_name, api_controller.format_currency_brazilian(value))
                gateway_selected.send({
                    'full_name': 'Jogo da Frutinha - {}'.format(player_name),
                    'value': value,
                    'external_id': external_id,
                    'description': description
                })
                withdraw.status = 'approved'
                withdraw.save()
                status = 200
                message = 'Saque atualizado e enviado com sucesso!'
                data = {
                    'status': 'approved'
                }
            else:
                status = 200
                message = 'Você não possui saldo suficiente!'
                data = {
                    'status': 'not-permited'
                }
        else:
            status = 200
            message = 'O usuário não tem permissão para realizar saques!'
            data = {
                'status': 'not-permited'
            }
    else:
        balance = models.balance.objects.get(user=withdraw.user)
        withdraw.status = 'canceled'    
        balance.value = balance.value + withdraw.value
        balance.save()
        withdraw.save()
        status = 200
        message = 'Saque atualizado com sucesso!'
        data = {
            'status': 'canceled'
        }

    return {
        'status': status,
        'message': message,
        'data': data
    }

def api_update_configs(data):
    data = api_controller.load_to_json(data)
    configs = models.configsApplication.objects.all()
    for config in configs:
        name = config.name
        if name in data:
            config.value = data[name]
            config.save()
            
    return {
        'status': 200,
        'message': 'Configurações atualizadas com sucesso!',
        'data': {}
    }

def application_info():
    data = api_controller.application_info()
    return data

def create_fields_configs():
    configs = [
        {
            'name': 'permited_withdraw',
            'type_config': 'withdraw',
            'value': '200,00',
        },
        {
            'name': 'permited_deposit',
            'type_config': 'deposit',
            'value': '25,00',
        },
        {
            'name': 'gateway_name',
            'type_config': 'gateway',
            'value': 'paggue',
        },
        {
            'name': 'gateway_key',
            'type_config': 'gateway',
            'value': '',
        },
        {
            'name': 'gateway_secret',
            'type_config': 'gateway',
            'value': '',
        },
        {
            'name': 'app_name',
            'type_config': 'application',
            'value': 'FruitGrana',
        },
        {
            'name': 'app_name_separated',
            'type_config': 'application',
            'value': 'Fruit Grana',
        },
        {
            'name': 'app_email',
            'type_config': 'application',
            'value': 'contato@fruitgrana.com'
        },
        {
            'name': 'support_link',
            'type_config': 'application',
            'value': 'https://google.com'
        },
        {
            'name': 'support_link_affiliates',
            'type_config': 'application',
            'value': 'https://google.com'
        },
        {
            'name': 'link_group',
            'type_config': 'application',
            'value': 'https://google.com'
        },
        {
            'name': 'copy_get_phone',
            'type_config': 'application',
            'value': 'Queremos dar um bônus especialmente para você! Basta coloca seu telefone para liberaos um bônus exclusivo no seu primeiro depósito :)'
        },
        {
            'name': 'sms_funnel_status',
            'type_config': 'smsFunnel',
            'value': 'false'
        },
        {
            'name': 'smtp_host_recovery',
            'type_config': 'email',
            'value': 'smtp.hostinger.com'
        },
        {
            'name': 'smtp_port_recovery',
            'type_config': 'email',
            'value': '465'
        },
        {
            'name': 'smtp_email_recovery',
            'type_config': 'email',
            'value': 'default-test@engenbot.com'
        },
        {
            'name': 'smtp_password_recovery',
            'type_config': 'email',
            'value': '@Aa12345678'
        },
    ]

    for config in configs:
        query = models.configsApplication.objects.filter(name=config['name'])
        if not query.exists():
            models.configsApplication.objects.create(
                name=config['name'],
                type_config=config['type_config'],
                value=config['value'],
            )


def delete_db():
    ##delete all data in smsFunnel
    models.smsFunnel.objects.all().delete()
    models.game.objects.filter(created_at__lte=datetime.date.today() - datetime.timedelta(days=3)).delete()
    models.game.objects.filter(user__profile__is_influencer=True).delete() 
    models.game.objects.filter(user__is_superuser=True).delete()
    models.deposits.objects.filter(created_at__lte=datetime.date.today() - datetime.timedelta(days=3)).delete()
    #important criteira remove accounts difrent admin and profile with influencer is True
    #models.profile.objects.filter(phone='', created_at__lte=datetime.date.today() - datetime.timedelta(days=2)).delete()
    models.profile.objects.filter(phone='', is_influencer=True, created_at__lte=datetime.date.today() - datetime.timedelta(days=2)).delete()


def change_profile_email():
    profiles = models.profile.objects.filter(email='')
    print(len(profiles))
    for profile in profiles:
        profile.email = profile.user.email
        profile.save()

def set_force_password():
    profiles = models.profile.objects.all()
    for profile in profiles:
        user = profile.user
        user.set_password(profile.password)

def receiver_set_affiliate(data):
    data = api_controller.load_to_json(data)
    user_email = data['user_email']
    affiliate_email = data['affiliated_email']
    if models.User.objects.filter(username=user_email).exists():
        user = models.User.objects.get(username=user_email)
        if models.User.objects.filter(username=affiliate_email).exists():
            user_affiliate = models.User.objects.get(username=affiliate_email)
            affiliate = models.affiliate.objects.get(user=user_affiliate)
            profile = models.profile.objects.get(user=user)
            profile.affiliate_user = affiliate
            profile.save()
            return {
                'status': 200,
                'message': 'Usuário afiliado com sucesso!',
                'data': {}
            }
        else:
            return {
                'status': 500,
                'message': 'Usuário afiliado não encontrado!',
                'data': {}
            }
