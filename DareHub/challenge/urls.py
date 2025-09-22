from django.urls import path
from .views import CreateChallengeView

urlpatterns = [
    path("newchallenge", CreateChallengeView.as_view(), name="newchallenge"),
]
