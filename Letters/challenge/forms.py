#-*- coding: utf-8 -*-
from django import forms

class LettersForm(forms.Form):
    solution = forms.CharField(label="Solution", max_length=9,required=False)

class ChiffresForm(forms.Form):
    op1 = forms.CharField(label="op1", max_length=11,required=True)
    op2 = forms.CharField(label="op2", max_length=11,required=False)
    op3 = forms.CharField(label="op3", max_length=11,required=False)
    op4 = forms.CharField(label="op4", max_length=11,required=False)
    op5 = forms.CharField(label="op5", max_length=11,required=False)