from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Task, User

class CustomUserAdmin(UserAdmin):
    """
    Custom admin view for User model
    """
    model = User
    list_display = [
        'username', 'email', 'first_name', 'last_name', 
        'mobile', 'is_staff', 'is_active'
    ]
    list_filter = ['is_staff', 'is_active']
    
    # Fieldsets for user creation and editing
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'mobile')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Additional fields for user creation
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'mobile', 'is_staff', 'is_active')
        }),
    )

class TaskAdmin(admin.ModelAdmin):
    """
    Admin configuration for Task model
    """
    list_display = [
        'name', 'status', 'task_type', 
        'created_at', 'completed_at'
    ]
    list_filter = ['status', 'task_type', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']
    
    # Customize the form for many-to-many relationship
    filter_horizontal = ['assigned_users']

    def get_queryset(self, request):
        """
        Optimize the queryset to reduce database queries
        """
        return super().get_queryset(request).prefetch_related('assigned_users')

# Register models with custom admin classes
admin.site.register(User, CustomUserAdmin)
admin.site.register(Task, TaskAdmin)