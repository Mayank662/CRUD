from django import forms
from .models import Emp


class EmpForm(forms.ModelForm):


    class Meta:
        model = Emp
        fields = ('fullname','mobile','emp_code','position')
        labels = {
                'fullname': 'Full Name',
                'emp_code': 'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmpForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['emp_code'].required = False