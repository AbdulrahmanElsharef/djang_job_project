from django import forms
from .models import Apply_job , Job


class ApplyForm(forms.ModelForm):

    class Meta:
        model = Apply_job
        exclude = ('job',)


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        exclude = ('user','slug')