from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.views import generic
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from braces.views import SelectRelatedMixin

from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

# @login_required
# def PostList(request):
#     logged_in_user = request.user
#     todo_list_user = Todo.objects.filter(user = logged_in_user)
#     return render(request, 'todo/list_view.html', {'lists': todo_list_user})

class TodoList(generic.ListView):
    model = models.Todo
    template_name = 'todo/list_view.html'

    def get_queryset(self):
        try:
            self.todo_user = User.objects.prefetch_related('todos').get(username__iexact=self.kwargs.get('username'))

        except User.DoesNotExist:
            raise Http404
        else:
            return self.todo_user.todos.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_user'] = self.todo_user
        return context

class CreateList(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields = ('title','details','is_priority')
    model = models.Todo

    def form_valid(self,form):
        print("##############$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        print(self.object.user)
        print(self.request.user)
        print("#######################################################")
        self.object.save()
        return super().form_valid(form)

# @login_required
# def new(request):
#     form = forms.TodoForm(request.POST)
#     if form.is_valid():
#         profile = form.save(commit = False)
#         profile.user = request.user
#         profile.save()
#     context = {'title','details',}
