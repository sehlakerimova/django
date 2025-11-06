from django.urls import path
from . import views

app_name = 'polls'  # bu çox vacibdir

urlpatterns = [
    path('', views.index, name='index'),  # əsas səhifə
    path('<int:question_id>/', views.detail, name='detail'),  # sual detalları
    path('<int:question_id>/results/', views.results, name='results'),  # nəticələr
    path('<int:question_id>/vote/', views.vote, name='vote'),  # səsvermə
]