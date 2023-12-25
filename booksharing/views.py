from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('book_list')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False 
        user.save()
        return super().form_valid(form)
