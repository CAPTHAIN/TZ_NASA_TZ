from django.views.generic import ListView

from .models import *
from .parse import get_post_data


class MainPage(ListView):
    model = Post
    template_name = 'nasa/main.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    get_post_data()
