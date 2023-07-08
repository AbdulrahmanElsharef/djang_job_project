from django import forms
from board.models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude=['slug']