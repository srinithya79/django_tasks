from django.shortcuts import render
from .forms import UploadFileForm

# Create your views here.

def upload_files(request):
    if request.method == "POST":
        uf = UploadFileForm(request.POST, request.FILES)
        if uf.is_valid():
            uf.save()
    else:
        uf = UploadFileForm()
    return render(request, 'test.html',{'uf':uf})
