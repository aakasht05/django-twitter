from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet

# Create your views here.

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     print(self.kwargs)
    #     pk = self.kwargs.get("pk")
    #     print(pk)
    #     return Tweet.objects.get(id=pk)

class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        print(context)
        context["another_list"] = Tweet.objects.all()
        print(context)
        return context