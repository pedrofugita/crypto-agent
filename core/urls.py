from django.contrib import admin
from django.urls import path
from crypto.views import index, get_bot_response, get_chart_data 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('api/chat/', get_bot_response, name='api_chat'),
    path('api/chart/', get_chart_data, name='api_chart'),
]