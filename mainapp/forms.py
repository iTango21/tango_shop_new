from django import forms

from .models import Order

from django.contrib.auth.models import User
from accounttt.models import Profileee


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_date'].label = 'Дата получения заказа'

    order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = (
            #'first_name', 'last_name', 'phone', 'email', 'address', 'buying_type', 'order_date', 'comment'
            'first_name', 'last_name', 'phone', 'email', 'address', 'buying_type', 'order_date', 'comment'
        )

# class CustomSignupForm(SignupForm):
#     first_name = forms.CharField(max_length=30, label='First Name')
#     last_name = forms.CharField(max_length=30, label='Last Name')
#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.save()
#         return user


# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#
# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profileee
#         fields = ('test_field',)