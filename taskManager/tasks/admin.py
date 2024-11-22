from allauth.socialaccount.models import SocialApp
from django.contrib import admin

class SocialAppAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return request.user.is_superuser  # Only admins can access

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

admin.site.unregister(SocialApp)
admin.site.register(SocialApp, SocialAppAdmin)
