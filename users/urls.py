from django.urls import path
from .views import RegisterView
from django.contrib.auth.views import LoginView

app_name = 'users'  # Добавляем app_name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),  # Добавляем маршрут для входа
    # Другие маршруты
]