from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

class userlist(LoginRequiredMixin, TemplateView):
    template_name = "memo/index.html"

    def get(self, request, *args, **kwargs):
        context = super(userlist, self).get_context_data(**kwargs)
        context['text'] = 'Login OK!!'
        return render(self.request, self.template_name, context)
    
    @login_required
    def index(request):
        return HttpResponse('Login OK!!')
    
class IndexView(View):
    def get(self, request):
        return HttpResponse('Hello, this is the Index View')