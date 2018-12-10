from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import UserProfile
from .models import Project, Task

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email',max_length=254, help_text='Required a valid email address.')
    class Meta:
        model = UserProfile
        fields = ('email', )

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ('name' , 'added_by') 

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ('name' , 'added_by')	
			
	

