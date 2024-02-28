from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)

class UserRating(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)
    rating = models.CharField(max_length=20)

    def __str__(self):
        return f'Rating for {self.user.username}'

class Category(models.Model):
    CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Project', 'Project'),
        ('Hobby', 'Hobby'),
        ('Science', 'Science'),
        ('Health and Sport', 'Health and Sport'),
        ('Finances', 'Finances'),
        ('Other', 'Other')
    ]

    name = models.CharField(max_length=100, choices=CHOICES, unique=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    priority = models.CharField(max_length=10, choices=[
                                                        ('High', 'High'),
                                                        ('Norma l', 'Normal'),
                                                        ('Low', 'Low'),
                                                        ('None', 'None')
                                                        ], default='None')
    category = models.ManyToManyField(Category, related_name='category', blank=True)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title
