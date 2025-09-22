from rest_framework.generics import CreateAPIView
from .serializers import ChallengeSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Challenge


class CreateChallengeView(CreateAPIView):
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Challenge.objects.all()