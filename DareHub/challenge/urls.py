from django.urls import path
from .views import CreateChallengeView, ListChallengeView, RetrieveChallengeView, InterestedApiView, DoneChallenge

urlpatterns = [
    path("newchallenge", CreateChallengeView.as_view(), name="newchallenge"),
    path("allchallenges", ListChallengeView.as_view(), name="allchallenges"),
    path("retrievechallenge/<str:title>", RetrieveChallengeView.as_view(), name="retrievechallenge"),
    path("interested/<int:id>", InterestedApiView.as_view(), name="interested"),
    path("donechallenge/<int:id>", DoneChallenge.as_view(), name="donechallenge"),
]
