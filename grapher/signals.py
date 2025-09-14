from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Profile


def create_photographer_from_user(instance, created, *args, **kwargs):
    if created:

        Profile.objects.create(
            user=instance,
            first=instance.username,
            # last = instance.username,
            
            # email=instance.email
        )
    print("customer_card created succesfully ! ")


post_save.connect(create_photographer_from_user, sender=User)
