
from django.urls import path
from .import views

urlpatterns = [
    path('admin/',views.alldata),
    path('filterdata/',views.filterdata),
    path('values/',views.value),
    path('valueslist',views.vlist),
    path('ex/',views.ex)

]
