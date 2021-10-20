from django.db import models
from django.contrib.auth.models import User



def get_profile_image_fillepath(self, filename):
    return f'profile_images/{self.user_id.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return 'images/default_profile_image.png'



class AccountProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_profile_image_fillepath, default=get_default_profile_image)


    def __str__(self):
        return self.user_id.username


    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/{self.user_id.pk}/'):]