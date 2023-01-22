from django import forms
from .models import Apply_job


class ApplyForm(forms.ModelForm):

    class Meta:
        model = Apply_job
        exclude = ('job',)
