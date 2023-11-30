from . import models
import datetime

def calculate_bet_gain(value):
    now = datetime.datetime.now()
    bet_total = models.dashboards.objects.filter(name='bet_total').first()
    bet_month = models.dashboards.objects.filter(name='bet_month').first()
    bet_week = models.dashboards.objects.filter(name='bet_week').first()
    bet_day = models.dashboards.objects.filter(name='bet_day').first()

    bet_total_count = models.dashboards.objects.filter(name='bet_total_count').first()
    bet_month_count = models.dashboards.objects.filter(name='bet_month_count').first()
    bet_week_count = models.dashboards.objects.filter(name='bet_week_count').first()
    bet_day_count = models.dashboards.objects.filter(name='bet_day_count').first()

    bet_total.value = float(bet_total.value) + value
    bet_total_count.value = int(bet_total_count.value) + 1

    # Verify if bet_month.forced_date is 30 days ago from now
    if bet_month.forced_date is None or (now - datetime.datetime.combine(bet_month.forced_date, datetime.datetime.min.time())).days >= 30:
        bet_month.forced_date = now.date()
        bet_month.value = value
        bet_month_count.value = 1
    else:
        bet_month.value = float(bet_month.value) + value
        bet_month_count.value = int(bet_month_count.value) + 1

    # Verify if bet_week.forced_date is 7 days ago from now
    if bet_week.forced_date is None or (now - datetime.datetime.combine(bet_week.forced_date, datetime.datetime.min.time())).days >= 7:
        bet_week.forced_date = now.date()
        bet_week.value = value
        bet_week_count.value = 1
    else:
        bet_week.value = float(bet_week.value) + value
        bet_week_count.value = int(bet_week_count.value) + 1

    # Verify if bet_day.forced_date is 1 day ago from now
    if bet_day.forced_date is None or (now - datetime.datetime.combine(bet_day.forced_date, datetime.datetime.min.time())).days >= 1:
        bet_day.forced_date = now.date()
        bet_day.value = value
        bet_day_count.value = 1
    else:
        bet_day.value = float(bet_day.value) + value
        bet_day_count.value = int(bet_day_count.value) + 1

    bet_total.save()
    bet_month.save()
    bet_week.save()
    bet_day.save()
    bet_total_count.save()
    bet_month_count.save()
    bet_week_count.save()
    bet_day_count.save()

def calculate_users_gain(value, operator='sum'):
    try:
        users_gain = models.dashboards.objects.filter(name='users_gain').first()
        if operator == 'sum':
            users_gain.value = float(users_gain.value) + value
        else:
            users_gain.value = float(users_gain.value) - value
            if users_gain.value < 0:
                users_gain.value = 0
        
        users_gain.save()
    except Exception as e:
        print(e)

def calculate_home_gain(value, operator='sum'):
    try:
        home_gain = models.dashboards.objects.filter(name='house_gain').first()
        if operator == 'sum':
            home_gain.value = float(home_gain.value) + value
        else:
            home_gain.value = float(home_gain.value) - value
        
        home_gain.save()
    except Exception as e:
        print(e)

def calculate_registers():
    try:
        now = datetime.datetime.now()
        register_total = models.dashboards.objects.filter(name='register_total').first()
        register_month = models.dashboards.objects.filter(name='register_month').first()
        register_week = models.dashboards.objects.filter(name='register_week').first()
        register_day = models.dashboards.objects.filter(name='register_day').first()
        
        if register_month.forced_date is None or (now - datetime.datetime.combine(register_month.forced_date, datetime.datetime.min.time())).days >= 30:
            register_month.forced_date = now.date()
            register_month.value = 1
        else:
            register_month.value = int(register_month.value) + 1

        if register_week.forced_date is None or (now - datetime.datetime.combine(register_week.forced_date, datetime.datetime.min.time())).days >= 7:
            register_week.forced_date = now.date()
            register_week.value = 1
        else:
            register_week.value = int(register_week.value) + 1

        if register_day.forced_date is None or (now - datetime.datetime.combine(register_day.forced_date, datetime.datetime.min.time())).days >= 1:
            register_day.forced_date = now.date()
            register_day.value = 1
        else:
            register_day.value = int(register_day.value) + 1

        register_total.value = int(register_total.value) + 1

        register_total.save()
        register_month.save()
        register_week.save()
        register_day.save()
    except Exception as e:
        print(e)

def calculate_deposits(value):
    try:
        now = datetime.datetime.now()
        deposit_total = models.dashboards.objects.filter(name='deposit_total').first()
        deposit_month = models.dashboards.objects.filter(name='deposit_month').first()
        deposit_week = models.dashboards.objects.filter(name='deposit_week').first()
        deposit_day = models.dashboards.objects.filter(name='deposit_day').first()

        deposit_total_count = models.dashboards.objects.filter(name='deposit_total_count').first()
        deposit_month_count = models.dashboards.objects.filter(name='deposit_month_count').first()
        deposit_week_count = models.dashboards.objects.filter(name='deposit_week_count').first()
        deposit_day_count = models.dashboards.objects.filter(name='deposit_day_count').first()

        deposit_total.value = float(deposit_total.value) + value
        deposit_total_count.value = int(deposit_total_count.value) + 1

        # Verify if deposit_month.forced_date is 30 days ago from now
        if deposit_month.forced_date is None or (now - datetime.datetime.combine(deposit_month.forced_date, datetime.datetime.min.time())).days >= 30:
            deposit_month.forced_date = now.date()
            deposit_month.value = value
            deposit_month_count.value = 1
        else:
            deposit_month.value = float(deposit_month.value) + value
            deposit_month_count.value = int(deposit_month_count.value) + 1

        # Verify if deposit_week.forced_date is 7 days ago from now
        if deposit_week.forced_date is None or (now - datetime.datetime.combine(deposit_week.forced_date, datetime.datetime.min.time())).days >= 7:
            deposit_week.forced_date = now.date()
            deposit_week.value = value
            deposit_week_count.value = 1
        else:
            deposit_week.value = float(deposit_week.value) + value
            deposit_week_count.value = int(deposit_week_count.value) + 1

        # Verify if deposit_day.forced_date is 1 day ago from now
        if deposit_day.forced_date is None or (now - datetime.datetime.combine(deposit_day.forced_date, datetime.datetime.min.time())).days >= 1:
            deposit_day.forced_date = now.date()
            deposit_day.value = value
            deposit_day_count.value = 1
        else:
            deposit_day.value = float(deposit_day.value) + value
            deposit_day_count.value = int(deposit_day_count.value) + 1

        deposit_total.save()
        deposit_month.save()
        deposit_week.save()
        deposit_day.save()

        deposit_total_count.save()
        deposit_month_count.save()
        deposit_week_count.save()
        deposit_day_count.save()
    except Exception as e:
        print(e)

def calculate_deposit_first(value):
    try:
        deposit_first = models.dashboards.objects.filter(name='deposit_first').first()
        deposit_first_count = models.dashboards.objects.filter(name='deposit_first_count').first()
        deposit_first.value = float(deposit_first.value) + value
        deposit_first_count.value = int(deposit_first_count.value) + 1
        deposit_first.save()
        deposit_first_count.save()
    except Exception as e:
        print(e)

def calculate_withdraw_approved(value):
    try:
        withdraw_approved = models.dashboards.objects.filter(name='withdraw_approved').first()
        withdraw_approved_count = models.dashboards.objects.filter(name='withdraw_approved_count').first()
        withdraw_approved.value = float(withdraw_approved.value) + value
        withdraw_approved_count.value = int(withdraw_approved_count.value) + 1
        withdraw_approved.save()
        withdraw_approved_count.save()
    except Exception as e:
        print(e)

def calculate_withdraw_recused(value):
    try:
        withdraw_recused = models.dashboards.objects.filter(name='withdraw_recused').first()
        withdraw_recused_count = models.dashboards.objects.filter(name='withdraw_recused_count').first()
        withdraw_recused.value = float(withdraw_recused.value) + value
        withdraw_recused_count.value += 1
        withdraw_recused.save()
        withdraw_recused_count.save()
    except Exception as e:
        print(e)

def calculate_withdraw_pending(value, operator='sum'):
    try:
        withdraw_pending = models.dashboards.objects.filter(name='withdraw_pending').first()
        withdraw_pending_count = models.dashboards.objects.filter(name='withdraw_pending_count').first()

        if operator == 'sum':
            withdraw_pending.value = float(withdraw_pending.value) + value
            withdraw_pending_count.value = float(withdraw_pending_count.value) + value
        else:
            withdraw_pending.value = float(withdraw_pending.value) - value
            withdraw_pending_count.value = float(withdraw_pending_count.value) - value

        withdraw_pending.save()
        withdraw_pending_count.save()
    except Exception as e:
        print(e)











    
