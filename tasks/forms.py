from django import  forms
from .models import  Task,Product


class TaskForm(forms.ModelForm):

    class Meta:
        model =  Task
        fields = ('title','complete','user','id')
        # exclude = ('user',)
        widgets = {
        'id':forms.HiddenInput(attrs={"type":"text","class":"form-control",}),
        'title':forms.TextInput(attrs={"type":"text","class":"form-control",}),
        'complete':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        'csrfmiddlewaretoken':forms.HiddenInput(attrs={'class':'token'})
        }



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'price', 'caetgory_id');