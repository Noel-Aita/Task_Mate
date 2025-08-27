from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Task, TaskCategory, TaskUpdate, EducationalResource

# -----------------------
# Custom User Admin
# -----------------------
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'role')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
            'fields': (
                'first_name', 'last_name', 'email',
                'phone_number', 'license_number',
                'certification', 'experience_years', 'role'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, UserAdmin)

# -----------------------
# Inline for Task Updates
# -----------------------
class TaskUpdateInline(admin.TabularInline):
    model = TaskUpdate
    extra = 1  # show 1 empty form by default
    fields = ('update_text', 'status_change', 'updated_by')  # fields shown inline
    autocomplete_fields = ('updated_by',)  # dropdown search for users

# -----------------------
# Other Models
# -----------------------
@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'required_certification')
    search_fields = ('name', 'required_certification')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'created_by', 'assigned_to', 'due_date')
    list_filter = ('status', 'priority', 'category')
    search_fields = ('title', 'description', 'location')
    autocomplete_fields = ('created_by', 'assigned_to', 'category')
    inlines = [TaskUpdateInline]  # attach updates inline

@admin.register(TaskUpdate)
class TaskUpdateAdmin(admin.ModelAdmin):
    list_display = ('task', 'updated_by', 'status_change', 'created_at')
    list_filter = ('status_change',)
    search_fields = ('task__title', 'update_text', 'updated_by__username')

@admin.register(EducationalResource)
class EducationalResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'category', 'added_by', 'added_at')
    list_filter = ('resource_type', 'category')
    search_fields = ('title', 'description', 'url')
    autocomplete_fields = ('category', 'added_by')
