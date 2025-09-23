from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from .serializers import ChallengeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Challenge
from rest_framework.response import Response
from rest_framework import status


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

class InterestedApiView(UpdateAPIView):
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Challenge.objects.all()
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        challenge = self.get_object()
        user = self.request.user
        challenge.users.add(user)
        challenge.refresh_from_db()
        serializer = self.get_serializer(challenge)
        return Response(serializer.data, status=status.HTTP_200_OK)


        return challenge