

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



from django.contrib.auth.models import User



from accounts.models import AccountProfile



@receiver(post_save, sender=User)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        user = AccountProfile.objects.create(user_id=instance)
        user.save()

        Token.objects.create(user=instance)
         
    