# core/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Query
from .utils import assign_query
from django.utils import timezone
from datetime import timedelta

@api_view(['POST'])
def create_query(request):
    user = assign_query()

    query = Query.objects.create(
        title=request.data['title'],
        description=request.data['description'],
        assigned_to=user,
        sla_deadline=timezone.now() + timedelta(hours=2)
    )

    # Increase workload
    user.workload += 1
    user.save()

    return Response({"message": "Query created and assigned"})



@api_view(['GET'])
def dashboard(request):
    total = Query.objects.count()
    pending = Query.objects.filter(status='pending').count()
    resolved = Query.objects.filter(status='resolved').count()

    return Response({
        "total_queries": total,
        "pending": pending,
        "resolved": resolved,
    })