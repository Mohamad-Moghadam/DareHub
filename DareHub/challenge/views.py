from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import ChallengeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Challenge


class CreateChallengeView(CreateAPIView):
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Challenge.objects.all()

class ListChallengeView(ListAPIView):
    serializer_class = ChallengeSerializer
    permission_classes = [AllowAny]
    queryset = Challenge.objects.all()

class RetrieveChallengeView(RetrieveAPIView):
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Challenge.objects.all()
    lookup_field = 'title'