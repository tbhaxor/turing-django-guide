from django.forms import forms, fields
from django.forms import models
from django.forms.widgets import Textarea
from .models import Task


class GreetForm(forms.Form):
    name = fields.CharField(max_length=64,
                            required=True,
                            empty_value=False,
                            help_text='Enter your name to get personlised message',
                            label='Your Full Name')
    pass


class TaskForm(models.ModelForm):
    class Meta:
        # reference the target model
        model = Task

        # fields you want to use to create the fields
        fields = ('name', 'description')

        # customize the behaviour of the input field on HTML level
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20})
        }
