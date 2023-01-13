from django.urls import path
from .views import *
urlpatterns = [

    path("",index),
    path("add_activity/",add_activity),
    path("add_food/",add_food),
    path("add_exercise/",add_exercise),
    path("read_activity/",read_activity),
    path("read_food/",read_food),
    path("read_exercise/",read_exercise),
    path("delete_food/<int:id>", delete_food),
    path("delete_exe/<int:id>",delete_exe),
    path("update_food/<int:id>",update_food),
    path("update_exe/<int:id>",update_exe),
]