from apscheduler.schedulers.background import BackgroundScheduler
from . import tasks
def start_jobs():
    # Configure o logging para capturar saídas de print
    scheduler = BackgroundScheduler()

    def log_start_job():
        print("Iniciando tarefa")
    
    #Set cron to runs every 20 min.
    cron_job = {'month': '*', 'day': '*', 'hour': '*', 'minute':'*/1'}
    
    #Add our task to scheduler.
    scheduler.add_job(tasks.new_deposit, 'cron', **cron_job)
    scheduler.add_job(tasks.account_inactivated, 'cron', **cron_job) 
    scheduler.add_job(tasks.recovery_user, 'cron', **cron_job)
    scheduler.start()