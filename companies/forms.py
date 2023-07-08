from django import forms
from board.models import Employer

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'
        exclude=['slug']