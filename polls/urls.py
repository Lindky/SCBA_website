from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path('', views.home, name='home'),
    path("<int>/register/", views.register, name="register"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
