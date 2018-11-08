from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your name', 'class':"form-control"}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'placeholder':'Your Email (Optional)', 'class':'form-control'}),required=False)
    feedback = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your Feedback','class':'form-control'}))
