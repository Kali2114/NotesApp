from .models import UserRating, CustomUser, Note
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=CustomUser)
def create_user_rating(sender, instance, created, **kwargs):
    if created:
        UserRating.objects.create(user=instance, rating='Adept')

@receiver(post_save, sender=Note)
def update_user_rating(sender, instance, created, **kwargs):
    user = instance.user
    user_notes_count = Note.objects.filter(user=user).count()

    if user_notes_count <= 5:
        rating_value = 'Adept'
    elif user_notes_count <= 10:
        rating_value = 'Writer'
    elif user_notes_count <= 15:
        rating_value = 'Artist'
    else:
        rating_value = 'Erudite'

    user_rating = UserRating.objects.get(user=user)
    user_rating.rating = rating_value
    user_rating.save()