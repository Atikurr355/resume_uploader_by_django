from django.shortcuts import render,redirect
from .forms import ResumeForm
from .models import Resume
from django.views import View
# Create your views here.


class IndexView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        context= {
            'form':form,
            'candidates':candidates,
        }
        return render(request, 'resume/index.html',context)

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

class CandidateView(View):
    def get(self,request, pk):
        candi = Resume.objects.all()
        candidate = Resume.objects.get(id=pk)
        context= {
            'candidate':candidate,
            'candis':candi,
        }
        return render(request, 'resume/candidate.html',context)