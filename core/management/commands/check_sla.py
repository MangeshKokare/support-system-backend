# core/management/commands/check_sla.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import Query

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        overdue_queries = Query.objects.filter(
            status='pending',
            sla_deadline__lt=timezone.now()
        )

        for query in overdue_queries:
            # Reassign or escalate
            print(f"Escalating Query ID: {query.id}")