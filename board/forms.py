from django import forms
from board.models import Job,Candidate

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude=['slug','author']
        
class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
        exclude=['user','job']
