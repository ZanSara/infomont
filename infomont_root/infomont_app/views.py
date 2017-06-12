from django.shortcuts import render
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'infomont_app/homepage.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return
    #    """Return the last five published questions."""
    #    return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    #model = Question
    template_name = 'infomont_app/main_rifugio.html'
    def get_queryset(self):
        return
