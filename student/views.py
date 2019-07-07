from django.shortcuts import render
from django.views.generic import TemplateView
from book.models import Book
from . import models



class HomeTemplateView(TemplateView):
    template_name = 'student/home.html'


class ProfileTemplateView(TemplateView):
    books = Book.objects.all()
    template_name = 'student/profile.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        try:
            profile = models.Profile.objects.get(user=user)
            context['books'] = self.books.filter(program=profile.program)
        except Exception:
            print("You have to edit your profile")
        
        context['page'] = 'content'
        
        return context
