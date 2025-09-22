from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import CustomUser

class SignUpView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()

