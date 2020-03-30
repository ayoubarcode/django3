from django.db.models.signals import  post_save
from django.contrib.auth.models import User,Group

def create_group(sender, instance, created, **kwargs):
    if created:
        try:
            group = Group.objects.get(name='users')
        except  Group.DoesNotExist:
            group = Group.objects.create(name="users")
            instance.groups.add(group)


post_save.connect(create_group, sender=User)

# try:
#     group = Group.objects.get(name="users")
# except Group.DoesNotExist:
#     Group.objects.crate(name="users")
    