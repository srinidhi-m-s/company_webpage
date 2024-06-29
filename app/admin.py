from django.contrib import admin
from app.models import GeneralInfo,ServiceInfo,Testimonials,Faq,ContactFormLogs,Blog,Author
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    pass
@admin.register(ServiceInfo)
class ServiceInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    pass

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactFormLogs)
class ContactFormLogsAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'is_success',
        'is_error',
        'action_time',
    ]
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'author',
        'title',
        'created_at',
    ]
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass