# core/utils.py

from .models import User

def assign_query():
    # Get least loaded support member
    user = User.objects.filter(role='support').order_by('workload').first()
    return user