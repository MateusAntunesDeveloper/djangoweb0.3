from django.http import HttpResponse
from . models import Quest
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic



class IndexView(generic.ListView):
    template_name = "polls/index.html"
    content_object_name = "latest_question_list"

    def get_queryset(self):
        return Quest.objects.order_by("-pub_date")[:5]

class HerderByIndex(IndexView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
class DetailView(generic.DetailView):
    model = Quest
    template_name = "polls/detail.html"

class HerderByDetail(DetailView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ResultView(generic.DeleteView):
    model = Quest
    template_name = "polls/results.html"

def vote(request, question_id):
    return HttpResponse("You re voting on question %s" % question_id)
    


class HerderByView(ResultView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
