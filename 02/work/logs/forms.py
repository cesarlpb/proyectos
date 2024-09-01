from django import forms
from django_flatpickr.widgets import DateTimePickerInput
from logs.models import WorkLog

class WorkLogForm(forms.ModelForm):
    class Meta:
        model = WorkLog
        fields = ['title', 'description', 'start_time', 'end_time']
        widgets = {
            'start_time': DateTimePickerInput(),
            'end_time': DateTimePickerInput(),
        }
