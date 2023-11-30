from . import models
from . import gateway
from api import controller as api_controller
import datetime
from urllib.parse import urlparse
from . import gateway

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
        users_gain = models.dashboards.objects.get(name='users_gain')
        house_gain = models.dashboards.objects.get(name='house_gain')
        bet_day = models.dashboards.objects.get(name='bet_day')
        bet_week = models.dashboards.objects.get(name='bet_week')
        bet_month = models.dashboards.objects.get(name='bet_month')
        bet_total = models.dashboards.objects.get(name='bet_total')

        bet_total_count = models.dashboards.objects.get(name='bet_total_count')
        bet_month_count = models.dashboards.objects.get(name='bet_month_count')
        bet_week_count = models.dashboards.objects.get(name='bet_week_count')
        bet_day_count = models.dashboards.objects.get(name='bet_day_count')

        dict_gains = {
            'users': api_controller.format_currency_brazilian(users_gain.value),
            'home': api_controller.format_currency_brazilian(house_gain.value),
            'game_today': api_controller.format_currency_brazilian(bet_day.value),
            'count_game_today': bet_day_count.value, 
            'game_week': api_controller.format_currency_brazilian(bet_week.value),
            'count_game_week': bet_week_count.value,
            'game_month': api_controller.format_currency_brazilian(bet_month.value),
            'count_game_month': bet_month_count.value,
            'game_total': api_controller.format_currency_brazilian(bet_total.value),
            'count_game_total': bet_total_count.value,
        }
        metrics = dict_gains

    elif dash == 'registers':
        register_total = models.dashboards.objects.get(name='register_total')
        register_month = models.dashboards.objects.get(name='register_month')
        register_week = models.dashboards.objects.get(name='register_week')
        register_today = models.dashboards.objects.get(name='register_today')
        dict_new_users = {
            'today': register_today.value,
            'week': register_week.value,
            'month': register_month.value,
            'last_month': 0,
            'total': register_total.value,
        }
        metrics = dict_new_users

    elif dash == 'deposits':
        deposits_total = models.dashboards.objects.get(name='deposit_total')
        deposits_month = models.dashboards.objects.get(name='deposit_month')
        deposits_week = models.dashboards.objects.get(name='deposit_week')
        deposits_today = models.dashboards.objects.get(name='deposit_today')
        deposits_first = models.dashboards.objects.get(name='deposit_first')

        deposits_total_count = models.dashboards.objects.get(name='deposit_total_count')
        deposits_month_count = models.dashboards.objects.get(name='deposit_month_count')
        deposits_week_count = models.dashboards.objects.get(name='deposit_week_count')
        deposits_today_count = models.dashboards.objects.get(name='deposit_today_count')
        deposits_first_count = models.dashboards.objects.get(name='deposit_first_count')
        dict_deposits = {
            'first_deposit': api_controller.format_currency_brazilian(deposits_first.value),
            'count_first_deposit': deposits_first_count.value,
            'today': api_controller.format_currency_brazilian(deposits_today.value),
            'count_today': deposits_today_count.value,
            'week': api_controller.format_currency_brazilian(deposits_week.value),
            'count_week': deposits_week_count.value,
            'month': api_controller.format_currency_brazilian(deposits_month.value),
            'count_month': deposits_month_count.value,
            'total': api_controller.format_currency_brazilian(deposits_total.value),
            'count_total': deposits_total_count.value,
        }
        metrics = dict_deposits

    elif dash == 'withdraws':
        withdraws_pending = models.dashboards.objects.get(name='withdraw_pending')
        withdraws_recused = models.dashboards.objects.get(name='withdraw_recused')
        withdraws_approved = models.dashboards.objects.get(name='withdraw_approved')
        
        withdraws_pending_count = models.dashboards.objects.get(name='withdraw_pending_count')
        withdraws_recused_count = models.dashboards.objects.get(name='withdraw_recused_count')
        withdraws_approved_count = models.dashboards.objects.get(name='withdraw_approved_count')
        dict_withdraws = {
            'approved': api_controller.format_currency_brazilian(withdraws_approved.value),
            'count_approved': withdraws_approved_count.value,
            'recused': api_controller.format_currency_brazilian(withdraws_recused.value),
            'count_recused': withdraws_recused_count.value,
            'pending': api_controller.format_currency_brazilian(withdraws_pending.value),
            'count_pending': withdraws_pending_count.value,
        }
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
            withdraws = models.withdraw.objects.filter(email=query)
    else:
        withdraws = models.withdraw.objects.all()

    dict_withdraws = []
    for withdraw in withdraws:
        item = {}
        profile = models.profile.objects.get(email=withdraw.email)
        item['id'] = withdraw.id
        item['full_name'] = profile.full_name
        item['email'] = profile.email
        item['influencer'] = profile.is_influencer
        item['value'] = api_controller.format_currency_brazilian(withdraw.value)
        item['status'] = withdraw.status
        
        withdraw_user = models.withdraw.objects.filter(email=withdraw.email, status='approved')
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
        if query == '':
            profiles = models.profile.objects.all()
        else:
            profiles = models.profile.objects.filter(email=query)
    else:
        profiles = models.profile.objects.all()

    dict_users = []
    for profile in profiles:
        balance = models.balance.objects.filter(email=profile.email)[0]
        item = {}
        item['id'] = profile.user.id
        item['full_name'] = profile.full_name
        item['email'] = profile.user.email
        item['activated'] = profile.user.is_active
        item['influencer'] = profile.is_influencer
        item['balance'] = api_controller.format_currency_brazilian(balance.value)
        item['permited_withdraw'] = balance.permited_withdraw
        item['created_at'] = profile.created_at.strftime('%d/%m/%Y %H:%M:%S')
        item['deposited'] = profile.qt_deposit
        dict_users.append(item)

    dict_users = sorted(dict_users, key=lambda k: k['created_at'], reverse=True)
    
    return {
        'users': dict_users
    }

def get_info_user(data):
    data = api_controller.load_to_json(data)
    id_user = data['id_user']
    user = models.profile.objects.get(user__id=id_user)
    email = user.email
    balance = models.balance.objects.get(email=email)
    affiliate = models.affiliate.objects.get(email=email)

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
        email = user.email
        user.user.is_active = activated
        user.user.save()
        user.full_name = full_name
        user.user.email = email
        user.cpf = cpf
        user.phone = phone
        user.is_influencer = influencer
        user.save()

        balance = models.balance.objects.get(email=email)  
        balance.permited_withdraw = permited_withdraw
        balance.value = value
        balance.save()

        affiliate = models.affiliate.objects.get(email=email) 
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
            profiles = models.profile.objects.filter(is_influencer=True, email=query)
    else:
        profiles = models.profile.objects.all()

    dict_users = []
    for profile in profiles:
        email = profile.email
        balance = models.balance.objects.get(email=email)
        item = {}
        item['id'] = profile.user.id
        item['full_name'] = profile.full_name
        item['email'] = profile.user.email
        item['balance'] = api_controller.format_currency_brazilian(balance.value)
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
    parsed_uri = urlparse(request.build_absolute_uri())
    scheme = parsed_uri.scheme
    domain = parsed_uri.netloc
    domain_url = f"{scheme}://{domain}/"
    id_user = data['id_user']
    user = models.profile.objects.get(user__id=id_user)
    email = user.email
    affiliate = models.affiliate.objects.get(email=email)
    balance = models.balance.objects.get(email=email)  
    profiles_affiliated = models.profile.objects.filter(affiliate_email=email)     
    data = {
        'code': affiliate.code,
        'link': domain_url.replace('partnership/', '') + 'join/' + affiliate.code,
        'total_earning': api_controller.format_currency_brazilian(affiliate.total_earnings),
        'total_eaning_day': api_controller.format_currency_brazilian(affiliate.total_earnings_day),
        'total_earning_month': api_controller.format_currency_brazilian(affiliate.total_earnings_month),
        'total_earning_last_month': api_controller.format_currency_brazilian(affiliate.total_earnings_last_month),
        'registers': len(profiles_affiliated),
        'cpa_count': int(affiliate.cpa_count),
        'cpa_percent': int(affiliate.cpa_percent),
        'cpa_total': api_controller.format_currency_brazilian(affiliate.cpa_total),
        'cpa_day': api_controller.format_currency_brazilian(affiliate.cpa_day),
        'cpa_month': api_controller.format_currency_brazilian(affiliate.cpa_month),
        'cpa_last_month': api_controller.format_currency_brazilian(affiliate.cpa_last_month),
        'revshare_percent': int(affiliate.revshare_percent),
        'revshare_total': api_controller.format_currency_brazilian(affiliate.revshare_total),
        'revshare_day': api_controller.format_currency_brazilian(affiliate.revshare_day),
        'revshare_month': api_controller.format_currency_brazilian(affiliate.revshare_month),
        'revshare_last_month': api_controller.format_currency_brazilian(affiliate.revshare_last_month),
        'indication_percent': int(affiliate.indication_percent),
        'indication_count': int(affiliate.indication_count),
        'indication_total': api_controller.format_currency_brazilian(affiliate.indication_total),
        'value': api_controller.format_currency_brazilian(balance.value),
        'value_affiliate': api_controller.format_currency_brazilian(balance.value_affiliate),
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
    print(data)

    withdraw = models.withdraw.objects.get(id=id_withdraw)
    if data['status'] == 'approved':
        balance = models.balance.objects.get(email=withdraw.email)
        permited_withdraw = balance.permited_withdraw
        if permited_withdraw:
            value = withdraw.value
            gateway_selected = gateway.selected_gateway()
            authorized_withdraw = gateway_selected.compare(value)
            if authorized_withdraw:
                profile = models.profile.objects.get(email=withdraw.email)
                player_name = profile.full_name
                external_id = api_controller.generate_hash()
                description = 'Saque realizado por {} no valor de R${}'.format(player_name, api_controller.format_currency_brazilian(value))
                gateway_selected.send({
                    'full_name': 'Subway Surfers- {}'.format(player_name),
                    'value': float(value),
                    'external_id': external_id,
                    'description': description,
                    'pix_key': profile.cpf
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
        balance = models.balance.objects.get(email=withdraw.email)
        withdraw.status = 'canceled'    
        balance.value = balance.value + withdraw.value
        balance.save()
        withdraw.save()
        status = 200
        message = 'Saque atualizado com sucesso!'
        data = {
            'status': 'canceled'
        }
    print(message)
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
            'value': '20,00',
        },
        {
            'name': 'gateway_name',
            'type_config': 'gateway',
            'value': 'suitpay',
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
            'value': 'SubwayCash',
        },
        {
            'name': 'app_name_separated',
            'type_config': 'application',
            'value': 'Subway Cash',
        },
        {
            'name': 'app_email',
            'type_config': 'application',
            'value': 'contato@subwaycash.com'
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
        {'name': 'smtp_port_recovery', 'type_config': 'email', 'value': '465'},
        {'name': 'smtp_email_recovery', 'type_config': 'email', 'value': 'default-test@engenbot.com'},
        {'name': 'smtp_password_recovery', 'type_config': 'email', 'value': '@Aa12345678'},
    ]

    for config in configs:
        query = models.configsApplication.objects.filter(name=config['name'])
        if not query.exists():
            models.configsApplication.objects.create(
                name=config['name'],
                type_config=config['type_config'],
                value=config['value'],
            )

    dashboards = [
        {'name': 'withdraw_pending_count', 'type_dashboard': 'withdraws', 'value': '0'},
        {'name': 'withdraw_recused_count', 'type_dashboard': 'withdraws', 'value': '0'},
        {'name': 'withdraw_approved_count', 'type_dashboard': 'withdraws', 'value': '0'},
        {'name': 'withdraw_pending', 'type_dashboard': 'withdraws', 'value': '0'},
        {'name': 'withdraw_recused', 'type_dashboard': 'withdraws', 'value': '0'},
        {'name': 'withdraw_approved', 'type_dashboard': 'withdraws', 'value': '0'},
        {'name': 'deposit_total_count', 'type_dashboard': 'deposits', 'value': '0'},
        {'name': 'deposit_month_count', 'type_dashboard': 'deposits', 'value': '0'},
        {'name': 'deposit_week_count', 'type_dashboard': 'deposits', 'value': '0'},
        {'name': 'deposit_day_count', 'type_dashboard': 'deposits', 'value': '0'},
        {'name': 'deposit_first_count', 'type_dashboard': 'deposits', 'value': '0'},
        {'name': 'deposit_total', 'type_dashboard': 'deposits', 'value': '0'},
        {'name': 'deposit_month', 'type_dashboard': 'deposits', 'value': '0'},
        {'name': 'deposit_week', 'type_dashboard': 'deposits', 'value': '0'},
        {'name': 'deposit_day', 'type_dashboard': 'deposits', 'value': '0'},
        {'name': 'deposit_first', 'type_dashboard': 'deposits', 'value': '0'},
        {'name': 'register_total', 'type_dashboard': 'registers', 'value': '0'},
        {'name': 'register_month', 'type_dashboard': 'registers', 'value': '0'},
        {'name': 'register_week', 'type_dashboard': 'registers', 'value': '0'},
        {'name': 'register_day', 'type_dashboard': 'registers', 'value': '0'},
        {'name': 'bet_total_count', 'type_dashboard': 'gains', 'value': '0'},
        {'name': 'bet_month_count', 'type_dashboard': 'gains', 'value': '0'},
        {'name': 'bet_week_count', 'type_dashboard': 'gains', 'value': '0'},
        {'name': 'bet_day_count', 'type_dashboard': 'gains', 'value': '0'},
        {'name': 'bet_total', 'type_dashboard': 'gains', 'value': '0'},
        {'name': 'bet_month', 'type_dashboard': 'gains', 'value': '0'},
        {'name': 'bet_week', 'type_dashboard': 'gains', 'value': '0'},
        {'name': 'bet_day', 'type_dashboard': 'gains', 'value': '0'},
        {'name': 'house_gain', 'type_dashboard': 'gains', 'value': '0'},
        {'name': 'users_gain', 'type_dashboard': 'gains', 'value': '0'},
    ]

    for dashboard in dashboards:
        query = models.dashboards.objects.filter(name=dashboard['name'])
        if not query.exists():
            models.dashboards.objects.create(
                name=dashboard['name'],
                type_dashboard=dashboard['type_dashboard'],
                value=dashboard['value'],
            )

def get_ggr_info():
    percent = models.ggr.objects.get(name='percent')
    credit = models.ggr.objects.get(name='credit')
    debit =  models.ggr.objects.get(name='debit')
    paid_out = models.ggr.objects.get(name='paid-out')
    status = models.ggr.objects.get(name='status')

    dict_ggr = {
        'percent': percent.value,
        'credit': api_controller.format_currency_brazilian(credit.value),
        'debit': api_controller.format_currency_brazilian(debit.value),
        'paid_out': paid_out.value,
        'status': status.value,
    }

    return dict_ggr

def get_ggr_history():
    ggr_history = models.ggr_history.objects.all()
    dict_ggr = []
    for ggr in ggr_history:
        item = {}
        item['cpf'] = ggr.cpf
        item['value'] = api_controller.format_currency_brazilian(ggr.value)
        dict_ggr.append(item)

    return dict_ggr

def ggr_pay(data):
    data = api_controller.load_to_json(data)
    cpf = data['cpf']
    value = float(data['value'].replace(',', '.'))

    gateway_selected = gateway.selected_gateway()
    gateway_selected.send({
        'value': value,
        'pix_key': ''
    })

    debit = models.ggr.objects.get(name='debit')
    num_debit = float(debit.value)
    credit = models.ggr.objects.get(name='credit')
    num_credit = float(credit.value)

    calculation = num_debit - (value + num_credit)
    if calculation < 0:
        rest = abs(calculation)
        calculation_credit = num_credit + rest
        credit.value = str(calculation_credit)
        credit.save()
        calculation = 0
    debit.value = str(calculation)
    debit.save()

    paid_out = models.ggr.objects.get(name='paid-out')
    num_paid_out = float(paid_out.value)
    paid_out.value = str(num_paid_out + value)
    paid_out.save()

    ggr_history = models.ggr_history.objects.create(
        cpf=cpf,
        value=value
    )

    return {
        'status': 200,
        'message': 'GGR atualizado com sucesso!',
        'data': {}
    }


