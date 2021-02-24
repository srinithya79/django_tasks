# import form class from django 
from django import forms 
  
# import FileUpload from models.py 
from .models import FileUpload 
  
# create a ModelForm 
class UploadFileForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = FileUpload 
        fields = ['file']