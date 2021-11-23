from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels ={ 
            'created_date':"Date of creation",
            }
    def __init__(self,*args,**kwargs):
        super(OrderForm,self).__init__(*args,**kwargs)
        self.fields['product'].empty_label="--SELECT--"
        self.fields['customer'].empty_label="--SELECT--"
class SignInForm(UserCreationForm):
    class Meta :
        model = User
        fields = ['username','email','password1','password2']
