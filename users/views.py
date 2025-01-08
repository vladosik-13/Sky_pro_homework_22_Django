from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')  # Указываем маршрут для входа с использованием пространства имён

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)