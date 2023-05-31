from django.db import models
from django.utils.crypto import get_random_string



class Account(models.Model):

    Email_id = models.EmailField(unique=True)
    Account_id = models.CharField(max_lenght = 50,unique=True)
    Account_name = models.CharField(max_length = 100)
    app_secret_token = models.CharField(max_length=50,default=get_random_string)

    def save(self,*args,**kwargs):
        if not self.Account_id:
            self.Account_id = get_random_string(length = 10)
        super().save(*args,**kwargs)
