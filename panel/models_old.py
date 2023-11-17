from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
#table profile user
class profile(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    cpf = models.CharField(max_length=16, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    personalized_username = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    bet_game = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    in_game = models.BooleanField(default=False)
    ip = models.CharField(max_length=255, blank=True, null=True)
    is_influencer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_access = models.BooleanField(default=True)
    affiliate_user = models.ForeignKey('affiliate', on_delete=models.SET_NULL, blank=True, null=True, default=None)
    vanish = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profile'
        managed = True
    
    def __str__(self):
        return self.email
    
class affiliate(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    code = models.CharField(max_length=12)
    personalized_code = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cpa_percent = models.DecimalField(max_digits=10, decimal_places=2, default=90.00)
    cpa_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    revshare_percent = models.DecimalField(max_digits=10, decimal_places=2, default=30.00)
    revshare_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    indication_percent = models.DecimalField(max_digits=10, decimal_places=2, default=10.00) #new lines 
    indication_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) #new lines
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'affiliate'
        managed = True
    
    def __str__(self):
        return self.user.username
    
class balance(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    value_affiliate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    permited_withdraw = models.BooleanField(default=True)
    only_fake = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'balance'
        managed = True
    
    def __str__(self):
        return self.user.username
    
class withdraw(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
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
        return self.user.username
    
class deposits(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=255, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
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
    affiliate_user = models.ForeignKey('affiliate', on_delete=models.SET_NULL, blank=True, null=True, default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'deposits'
        managed = True
    
    def __str__(self):
        return self.user.username
    
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    bet = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payout = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_win = models.BooleanField(default=False)
    is_started = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class smsFunnel(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'smsFunnel'
        managed = True
    
    def __str__(self):
        return self.external_id

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

#when User is created also created profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
        affiliate.objects.create(user=instance)
        balance.objects.create(user=instance)
