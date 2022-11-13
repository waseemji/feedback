from django.urls import path

from . import views

    # path("",views.review),
urlpatterns = [
    path("",views.ReviewView.as_view()),
    path("thank-you",views.ThankyouView.as_view()),
    path("reviews",views.ReviewsListView.as_view()),
    path("reviews/<int:pk>",views.DetailedReviewView.as_view()) #use <int:pk> when using DetailView
]