from django.urls import path
from .views import home,machine_to_excel,excel_upload_view
urlpatterns = [
    path('',home,name='home'),
    path('excel/',machine_to_excel,name='excel'),
    path('excel_upload/',excel_upload_view,name='excel_upload'),
]