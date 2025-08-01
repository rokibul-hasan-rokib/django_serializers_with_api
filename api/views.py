from rest_framework import viewsets
from rest_framework.response import Response
from .models import Custmer

from .serializers import CustmerSerializer

class CustmerViewSet(viewsets.ModelViewSet):
    queryset = Custmer.objects.all()
    serializer_class = CustmerSerializer