from django.contrib import admin
from .models import (Users, Categories, Activities, Bookings, Payments, Vendors, Reviews, Promotions,
                     TwoFactorAuthentication, ApiAccess, IntegrationLogs, AuditLogs, LoginAttempts, MagicLinkTokens)


# Register your models here.

admin.site.register(Users)
admin.site.register(Categories)
admin.site.register(Activities)
admin.site.register(Bookings)
admin.site.register(Payments)
admin.site.register(Vendors)
admin.site.register(Reviews)
admin.site.register(Promotions)
admin.site.register(TwoFactorAuthentication)
admin.site.register(ApiAccess)
admin.site.register(IntegrationLogs)
admin.site.register(AuditLogs)
admin.site.register(LoginAttempts)
admin.site.register(MagicLinkTokens)
