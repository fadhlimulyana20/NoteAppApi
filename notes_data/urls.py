from django.urls import path

from .api import NoteList, NoteDetail

urlpatterns = [
    path('', NoteList.as_view()),
    path('<int:pk>/', NoteDetail.as_view())
]
