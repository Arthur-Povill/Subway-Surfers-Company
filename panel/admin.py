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
        'affiliate_email',
        'created_at', 
        'updated_at'
    )

class affiliateAdmin(admin.ModelAdmin):
    search_fields = ('id', 'email', 'code')
    list_display = (
        'id', 
        'email',
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
    search_fields = ('id', 'email')
    list_display = (
        'id', 
        'email', 
        'value', 
        'permited_withdraw',
        'created_at', 
        'updated_at'
    )

class withdrawAdmin(admin.ModelAdmin):
    search_fields = ('id', 'email')
    list_display = (
        'id', 
        'email', 
        'value', 
        'status', 
        'created_at', 
        'updated_at'
    )

class depositsAdmin(admin.ModelAdmin):
    search_fields = ('id', 'email', 'external_id')
    list_display = (
        'id', 
        'external_id',
        'email', 
        'value', 
        'status', 
        'created_at', 
        'updated_at'
    )

class gameAdmin(admin.ModelAdmin):
    search_fields = ('id', 'email')
    list_display = (
        'id', 
        'hash_game',
        'email', 
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

class ggrAdmin(admin.ModelAdmin):
    search_fields = ('id', 'email')
    list_display = (
        'id', 
        'name',
        'value',
        'created_at', 
        'updated_at'
    )

class ggr_historyAdmin(admin.ModelAdmin):
    search_fields = ('id', 'cpf')
    list_display = (
        'id', 
        'cpf',
        'value',
        'created_at', 
    )

class dashboardsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = (
        'id', 
        'name', 
        'type_dashboard',
        'value', 
        'created_at', 
        'updated_at'
    )

admin.site.register(models.profile, profileAdmin)
admin.site.register(models.affiliate, affiliateAdmin)
admin.site.register(models.balance, balanceAdmin)
admin.site.register(models.withdraw, withdrawAdmin)
admin.site.register(models.deposits, depositsAdmin)
admin.site.register(models.configsApplication, configsAdmin)
admin.site.register(models.game, gameAdmin)
admin.site.register(models.ggr, ggrAdmin)
admin.site.register(models.ggr_history, ggr_historyAdmin)
admin.site.register(models.dashboards, dashboardsAdmin)
