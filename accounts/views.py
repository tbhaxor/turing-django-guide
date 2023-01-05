from django.urls.base import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView

# Create your views here.


class SignupView(CreateView):
    model = User
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')
    fields = ('email', 'username', 'password')

    def form_valid(self, form):
        # set hashed password from the plain text
        form.instance.set_password(form.cleaned_data.get('password'))
        return super().form_valid(form)
