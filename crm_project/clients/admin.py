from django.contrib import admin
from .models import Client, Task
from .forms import ClientAdminForm

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    form = ClientAdminForm
    list_display = ('name', 'email', 'phone', 'company', 'created_at')
    search_fields = ('name', 'email', 'phone', 'company')
    list_filter = ('company',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'due_date', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'due_date')
    search_fields = ('title', 'description', 'client__name')


