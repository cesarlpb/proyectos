#################################### Script ####################################
# Loads worklogs from txt file
# Requires: django_extensions
# Run:      python manage.py runscript load_worklogs
#################################### Script ####################################

import re

from django.utils import timezone
from datetime import datetime, timedelta

from logs.models import WorkLog
from project.utils import load_env_variable


def parse_log_file(file_path):
    with open(file_path, 'r') as file:
        log_content = file.read()
    
    pattern = r'Título:\s*(.*?)\nDescripción:\s*(.*?)\nInicio:\s*(.*?)\nFinal:\s*(.*?)\nDuración:\s*(\d{2}):(\d{2})'
    matches = re.findall(pattern, log_content, re.DOTALL)

    for match in matches:
        title, description, start_time, end_time, hours, minutes = match
        
        # Convertir a datetime y hacerlos timezone-aware
        start_time = timezone.make_aware(datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S'))
        end_time = timezone.make_aware(datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S'))
        duration = timedelta(hours=int(hours), minutes=int(minutes))

        WorkLog.objects.create(
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
            duration=duration
        )
        
        
def run():
    file_path = load_env_variable("WORK_LOG_PATH")
    parse_log_file(file_path)
