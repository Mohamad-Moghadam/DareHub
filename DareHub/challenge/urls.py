from django.urls import path
from .views import CreateChallengeView, ListChallengeView, RetrieveChallengeView

urlpatterns = [
    path("newchallenge", CreateChallengeView.as_view(), name="newchallenge"),
    path("allchallenges", ListChallengeView.as_view(), name="allchallenges"),
    path("retrievechallenge/<str:title>", RetrieveChallengeView.as_view(), name="retrievechallenge"),
]
