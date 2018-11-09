from django import forms
from testapp.models import Educational
class Educational(forms.ModelForm):
    item = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Item Name"}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':"price of each item",'ng-model':'price'}))
    qty = forms.IntegerField(widget=forms.NumberInput(attrs={'ng-model':'qty','placeholder':'Quantity'}))
    class Meta:
        model =Educational
        fields ="__all__"

from testapp.models import Electronics
class Electronics(forms.ModelForm):
    item = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Item Name"}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':"price of each item",'ng-model':'price'}))
    qty = forms.IntegerField(widget=forms.NumberInput(attrs={'ng-model':'qty','placeholder':'Quantity'}))
    class Meta:
        model =Electronics
        fields ="__all__"
