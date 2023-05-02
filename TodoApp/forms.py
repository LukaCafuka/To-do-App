from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    
    text = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder' : 'New Task'}))

    class Meta:
        model = Todo
        fields = '__all__'