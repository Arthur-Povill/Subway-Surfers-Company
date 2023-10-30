from django.contrib import admin
from . import models

# Register your models here.
class profileAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'cpf', 'phone', 'email')
    list_display = (
        'id', 
        'full_name', 
        'cpf', 
        'phone', 
        'email', 
        'password', 
        'is_influencer', 
        'is_active', 
        'first_access',
        'affiliate_user',
        'created_at', 
        'updated_at'
    )

class affiliateAdmin(admin.ModelAdmin):
    search_fields = ('id', 'user__username', 'code')
    list_display = (
        'id', 
        'user', 
        'code', 
        'is_active', 
        'total_earnings', 
        'cpa_percent', 
        'cpa_total', 
        'revshare_percent', 
        'revshare_total', 
        'created_at', 
        'updated_at'
    )

class balanceAdmin(admin.ModelAdmin):
    search_fields = ('id', 'user__username')
    list_display = (
        'id', 
        'user', 
        'value', 
        'permited_withdraw', 
        'only_fake', 
        'created_at', 
        'updated_at'
    )

class withdrawAdmin(admin.ModelAdmin):
    search_fields = ('id', 'user__username')
    list_display = (
        'id', 
        'user', 
        'value', 
        'status', 
        'created_at', 
        'updated_at'
    )

class depositsAdmin(admin.ModelAdmin):
    search_fields = ('id', 'user__username')
    list_display = (
        'id', 
        'user', 
        'value', 
        'status', 
        'created_at', 
        'updated_at'
    )

class gameAdmin(admin.ModelAdmin):
    search_fields = ('id', 'user__username')
    list_display = (
        'id', 
        'hash_game',
        'user', 
        'bet',
        'payout',
        'is_win', 
        'is_finished',
        'created_at', 
        'updated_at'
    )

class configsAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'type_config')
    list_display = (
        'id', 
        'name',
        'type_config',
        'value',
    )	

class smsFunnelAdmin(admin.ModelAdmin):
    search_fields = ('id', 'external_id')
    list_display = (
        'id', 
        'external_id',
    )

admin.site.register(models.profile, profileAdmin)
admin.site.register(models.affiliate, affiliateAdmin)
admin.site.register(models.balance, balanceAdmin)
admin.site.register(models.withdraw, withdrawAdmin)
admin.site.register(models.deposits, depositsAdmin)
admin.site.register(models.configsApplication, configsAdmin)
admin.site.register(models.game, gameAdmin)
admin.site.register(models.smsFunnel, smsFunnelAdmin)
