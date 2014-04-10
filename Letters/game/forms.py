#-*- coding: utf-8 -*-
from django import forms

class LettersForm(forms.Form):
    max=30
    arg1 = forms.CharField(label="*", max_length=max)
    arg2 = forms.CharField(label="*", max_length=1)
    arg3 = forms.CharField(label="*", max_length=1)
    arg4 = forms.CharField(label="*", max_length=1)
    arg5 = forms.CharField(label="*", max_length=1)
    arg6 = forms.CharField(label="*", max_length=1)
    arg7 = forms.CharField(label="*", max_length=1)
    arg8 = forms.CharField(label="*", max_length=1)
    arg9 = forms.CharField(label="*", max_length=1)
