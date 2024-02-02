from django.urls import path
from projects import views


urlpatterns = [
    path("",views.project_index,name="project_index"),
    path("forma",views.nagroda_forma,name="nagroda_forma"),
    #path("<int:pk>",views.proj)
]
