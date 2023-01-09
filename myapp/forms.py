from django import forms
from .models import *

class EmployeeDetailsModelForm(forms.ModelForm):
    name = forms.CharField(
        error_messages={'required':'The Field is required'},
        widget = forms.TextInput(
            attrs={
                'id':'name',
                'class':'form-control'
            })
    )

    email = forms.EmailField(
        error_messages={'required':'The Field is required'},
        widget = forms.EmailInput(
            attrs={
                'id':'name',
                'class':'form-control'
            })
    )

    mobile = forms.CharField(
        error_messages={'required':'The Email is required'},
        widget= forms.TextInput(
            attrs={
                'id':'mobile',
                'class':'form-control'
            })
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICE,
         widget=forms.RadioSelect(
             attrs={
                'id':'gender',
                'class':'form-control'
            })
    )

    class Meta:
        model = employeeDetails
        fields = ['id','name','email','mobile','gender','country','state','district','prejoblocation','emp_img','emp_app']