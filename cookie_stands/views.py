from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import CookieStand
from .serializer import CookieStandSerializer
from .permissions import IsOwnerOrReadOnly

class CookieStandList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer

class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer
