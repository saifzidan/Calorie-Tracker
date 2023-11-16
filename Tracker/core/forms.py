from django import forms
class CalorieAdd(forms.Form):
    food = forms.CharField()