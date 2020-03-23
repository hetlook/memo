import datetime
from django.shortcuts import render, get_object_or_404, redirect 
from django.views.generic import ListView, View
from django.utils import timezone

from .models import Todo
from siteinfo.models import Banner, Footer

# Create your views here.
class TodoListView(ListView):
    model = Todo
    context_object_name = 'todo_list'
    template_name = 'todo/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        now = timezone.now()
        tomorrow = now + datetime.timedelta(days=1)
        start_week = now - datetime.timedelta(now.weekday()) + datetime.timedelta(days=7)

        start_week = datetime.datetime(start_week.year, start_week.month, start_week.day)
        end_week = start_week + datetime.timedelta(days=7)

        todos = Todo.objects.all()
        context['todo_today'] = todos.filter(updated__day=now.today().day, updated__month=now.today().month, updated__year=now.today().year)
        
        context['todo_tomorrow'] = todos.filter(updated__day=tomorrow.day, updated__month=tomorrow.month, updated__year=tomorrow.year)
        
        context['todo_next_week'] = todos.filter(updated__range=[start_week, end_week])

        context['todo_doing'] = todos.filter(finish='doing')

        context['todo_done'] = todos.filter(finish='done')

        context['siteinfo'] = {
            'footer': Footer.objects.all().first(),
            'banner': Banner.objects.all().first()
        }

        return context

class TodoDeleteView(View):
    def post(self, request, id):
        todo = get_object_or_404(Todo, id=id)
        todo.delete()
        return redirect('todo:home')
