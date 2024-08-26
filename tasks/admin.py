from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Task, UserProfile


# Register your models here.
@admin.register(Task)
class TakeAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "assigned_to")
    list_filter = ("status", "assigned_to")
    search_fields = ("title", "description")

#user = User.objects.create_user(username='john_doe', email='john@example.com', password='password123')
#user_profile = UserProfile.objects.create(user=user, role='user')
#
#user_profile = UserProfile.objects.get(user__username='john_doe')
#user_profile.change_role('admin')
#
#group = Group.objects.create(name='Managers')
#user.groups.add(group)