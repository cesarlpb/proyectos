from django.urls import reverse_lazy
from django.utils import timezone
from pytz import timezone as pytz_timezone

from django.views.generic import ListView, CreateView
from logs.forms import WorkLogForm
from logs.models import WorkLog

class WorkLogListView(ListView):
    model = WorkLog
    form_class = WorkLogForm
    template_name = 'logs/worklog_list.html'
    context_object_name = 'logs'
    success_url = reverse_lazy('log_list')
    
    def form_valid(self, form):
        log = form.save(commit=False)
        log.duration = log.end_time - log.start_time
        log.save()
        return super().form_valid(form)

class WorkLogCreateView(CreateView):
    model = WorkLog
    template_name = 'logs/worklog_form.html'
    fields = ['title', 'description', 'start_time', 'end_time']
    success_url = reverse_lazy('log_list')

    def form_valid(self, form):
        log = form.save(commit=False)

        # Solo guardar en UTC, Django lo maneja automáticamente
        log.duration = log.end_time - log.start_time
        log.save()
        return super().form_valid(form)