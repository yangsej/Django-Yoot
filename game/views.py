from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse 
from django.core.urlresolvers import reverse
from django.views import generic
from .forms import SignUpForm

# Create your views here.
def IndexView(request):
    title = '윷놀이'
    form = SignUpForm(request.POST or None)
    context = {
        'title': title,
        'form': form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        nickname = form.clean_nickname()
        instance.nickname = nickname
        instance.save()

    
    return render(request,'index.html', context)
##
##def Waiting(request):
####    try:
##        return HttpResponse("플레이어를 기다리는중...")
##        return BoardView.as_view()
####    except:
##        return Waiting(request)
    
class BoardView(generic.DetailView):
    model = None
    template_name = ''
    
