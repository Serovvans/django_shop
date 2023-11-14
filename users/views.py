from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.views.generic import CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.shortcuts import redirect

from users.models import User
from users.forms import UserForm, UserProfileForm
from users.utils import generate_code
from config import settings


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy("users:verify_email")
    template_name = 'users/register.html'

    def form_valid(self, form):
        code = generate_code()
        new_user = form.save()
        send_mail(
            subject='верификация почты',
            message=f"Ваш код подтверждения - {str(code)}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user]
        )
        new_user.is_active = False
        new_user.email_code = code
        return super().form_valid(form)


class VerificationView(TemplateView):
    template_name = 'users/verify_email.html'

    def post(self, request):
        email_code = request.POST.get('email_code')
        user_code = User.objects.filter(email_code=email_code).first()

        if user_code is not None and user_code.email_code == email_code:
            user_code.is_active = True
            user_code.save()
            return redirect('users:login')
        else:
            return redirect('users:verify_email_error')


class ErrorVerificationView(TemplateView):
    template_name = 'users/verify_email_error.html'
    success_url = reverse_lazy('users:msg_email')


class GenerateNewPasswordView(TemplateView):
    template_name = 'users/generate_new_password.html'

    def post(self, request):
        new_password = User.objects.make_random_password()
        email = request.POST.get('email')
        send_mail(
            subject='Вы сменили пароль',
            message=f'Ваш новый пароль {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        user = User.objects.filter(email=email).first()
        user.set_password(new_password)
        user.save()
        return redirect('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm

    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
