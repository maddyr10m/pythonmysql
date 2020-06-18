from django import forms
import datetime
from .models import BurnRate, BurnDetail


class RegistrationForm(forms.Form):
    myitem = forms.CharField(label='Item:', max_length=50,
                             widget=forms.TextInput(attrs={'class':'form-control'}))
    paymethod = forms.CharField(label='Pay Method:', max_length=7, initial='CREDIT',
                        widget=forms.TextInput(attrs={'class':'form-control'}))
    cost = forms.DecimalField(label='Cost:', decimal_places=2, initial=0.00,
                        widget=forms.TextInput(attrs={'class':'form-control'}))
    today = datetime.date.today()
    new_date = datetime.date(year=today.year - 1, month=today.month, day=today.day)
    pub_date = forms.DateField(label='Date:', initial=datetime.date.today,
                        widget=forms.TextInput(attrs={'class':'form-control'}))


class RegistrationModal(forms.ModelForm):
    class Meta:
          model = BurnRate

          fields = [
             'myitem',
             'paymethod',
             'cost',
             'pub_date']

          widgets = {
                   'myitem':forms.TextInput(attrs={'class':'form-control','placeholder':'myitem'
                                                      }),
                   'paymethod':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paymethod'
                                                }),
                   'cost': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cost'
                                                    }),
                   'pub_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'pub_date'
                                             }),
                                                }


class DetailForm(forms.Form):
    fkey = forms.IntegerField(label='Fkey:', initial=1)
    myitem = forms.CharField(label='Item:', max_length=50)
    count_item = forms.IntegerField(label='Item Count:', initial=1)
    itemclass = forms.CharField(label='Item Class:', max_length=20, initial='FOOD')
    spendgroup = forms.CharField(label='Spend Group:', max_length=20, initial='FOOD SHOP')
    gengroup = forms.CharField(label='General Group:', max_length=20, initial='FOOD')
    cost = forms.DecimalField(label='Cost:', decimal_places=2, initial=0.00)
    taxrate = forms.DecimalField(label='Tax Rate:', decimal_places=4, initial=0.0000)
    costwithtax = forms.DecimalField(label='Cost:', decimal_places=2, initial=0.00)

