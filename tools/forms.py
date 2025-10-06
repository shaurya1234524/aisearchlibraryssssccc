from django import forms
from .models import Tool

# forms.py
from django import forms


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name', 'description', 'image', 'category', 'tags', 'pricing', 'website']
        widgets = {
            'category': forms.Select(attrs={'class': 'category-select'}),
            'pricing': forms.Select(attrs={'class': 'pricing-select'}),
        }
