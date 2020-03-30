from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name=("user_id"), 
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)




# post_save.connect( update_profile, sender=User)