from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
#table profile user
class profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=16, blank=True, null=True, default='')
    phone = models.CharField(max_length=15, blank=True, null=True, default='')
    email = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')
    in_game = models.BooleanField(default=False)
    ip = models.CharField(max_length=255, blank=True, null=True)
    is_influencer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_access = models.BooleanField(default=True)
    game_test = models.IntegerField(default=3)
    affiliate_email = models.CharField(max_length=255, blank=True, null=True, default='')
    vanish = models.BooleanField(default=False)
    first_deposit = models.BooleanField(default=False)
    qt_deposit = models.IntegerField(default=0)
    qt_withdraw = models.IntegerField(default=0)
    utm = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profile'
        managed = True
    
    def __str__(self):
        return self.email
    
class affiliate(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, default='')
    code = models.CharField(max_length=12)
    personalized_code = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_earnings_day = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_earnings_month = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_earnings_last_month = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cpa_count = models.IntegerField(default=0)
    cpa_percent = models.DecimalField(max_digits=10, decimal_places=2, default=16.00)
    cpa_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cpa_day = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cpa_month = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cpa_last_month = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    revshare_percent = models.DecimalField(max_digits=10, decimal_places=2, default=30.00)
    revshare_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    revshare_day = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    revshare_month = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    revshare_last_month = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    indication_percent = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    indication_count = models.IntegerField(default=0)
    indication_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) #new lines
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'affiliate'
        managed = True
    
    def __str__(self):
        return self.email
    
class balance(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, default='')
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    value_affiliate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    value_original = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    value_ggr = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_deposit_bigger = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    permited_withdraw = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'balance'
        managed = True
    
    def __str__(self):
        return self.email
    
class withdraw(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, default='')
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('in_progress', 'In Progress'),
        ('canceled', 'Canceled')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    details = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'withdraw'
        managed = True
    
    def __str__(self):
        return self.email
    
class deposits(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=255, default=None)
    email = models.CharField(max_length=255, default='')
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pix_code = models.CharField(max_length=255, blank=True, null=True)
    qr_code = models.TextField(blank=True, null=True)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('in_progress', 'In Progress'),
        ('canceled', 'Canceled')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'deposits'
        managed = True
    
    def __str__(self):
        return self.email
    
class configsApplication(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type_config = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'configsApplication'
        managed = True
    
    def __str__(self):
        return self.name

class game(models.Model):
    id = models.AutoField(primary_key=True)
    hash_game = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default='')
    bet = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payout = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_win = models.BooleanField(default=False)
    is_started = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class ggr(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ggr'
        managed = True
    
    def __str__(self):
        return self.name
    
class ggr_history(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=255, default=None)
    cpf = models.CharField(max_length=255, default='')
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('in_progress', 'In Progress'),
        ('canceled', 'Canceled')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ggr_history'
        managed = True
    
    def __str__(self):
        return self.external_id
    
class withdraw_free(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=255, default='')
    ip = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 'withdraw_free'
        managed = True

    def __str__(self):
        return self.cpf

class dashboards(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type_dashboard = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    forced_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dashboards'
        managed = True
    
    def __str__(self):
        return self.name
    
#when User is created also created profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance, email=instance.email)
        affiliate.objects.create(email=instance.email)
        balance.objects.create(email=instance.email)
