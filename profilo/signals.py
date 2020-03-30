from django.db.models.signals import  post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,lastname=instance.last_name, firstname=instance.first_name)
        print('Profile created')

# post_save.connect(create_profile, sender=User)
@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        try:
            instance.profile.save()
            print('Profile updated')
        except:
            print(instance.last_name)
            Profile.objects.create(user=instance, lastname=instance.last_name, firstname=instance.first_name)
            print('Profile created for an existing user')
