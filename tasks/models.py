from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
        ('in_progress', 'В процесі'),
        ('done', 'Виконано'),
        ('postponed', 'Відкладено'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    
    def __str__(self):
        return f'{self.user.username} - {self.get_role_display()}'

    def change_role(self, new_role):
        if new_role in dict(self.ROLE_CHOICES):
            self.role = new_role
            self.save()
        else:
            raise ValueError(f"{new_role} - такой роли нет")