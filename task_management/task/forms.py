from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'assign_date': forms.DateInput(attrs={'type': 'date'})
        }
        labels = {
            'title': 'Task Title',
            'description': 'Task Description',
             'assign_date': 'Assign Date',
            'is_completed': 'Is Completed',
            'category': 'Category'
        }
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
            'assign_date': forms.DateInput(attrs={'type': 'date'})
        }