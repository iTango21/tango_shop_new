from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

#import phonenumbers
#from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField

class Profileee(models.Model):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15, verbose_name='Имя', null=True, blank=True)
    last_name = models.CharField(max_length=25, verbose_name='Фамилия', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    phone = PhoneField(blank=True, help_text='Номер телефона')
    #address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    tg_id = models.CharField(max_length=15, verbose_name='Телеграмм ID', default='1234567', null=True, blank=True)
    #date_of_birth = models.DateField(blank=True, null=True)
    #photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    # first_name = User.first_name
    # last_name  = User.last_name

    def __str__(self):
        return 'Profile for user {}, {}'.format(
            User.first_name,
            User.last_name
        )

    # def __str__(self):
    #     return 'Profile for user'