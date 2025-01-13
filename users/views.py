from django.contrib.messages.context_processors import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.core.mail import send_mail

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        login(self.request, user)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш каталог продуктов!'
        message = 'Спасибо что зарегистрировались в нашем каталоге! Удачных покупок!'
        from_email = 'testvlad59@yandex.ru'
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)
