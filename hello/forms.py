from django import forms
from .models import Entry, Category


class EntryForm(forms.ModelForm):
    """词条表单"""
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 15, 'cols': 80, 'class': 'form-control'}),
        label='词条内容'
    )
    
    class Meta:
        model = Entry
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入词条标题'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': '词条标题',
            'category': '所属分类',
        }


class CategoryForm(forms.ModelForm):
    """分类表单"""
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入分类名称'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': '请输入分类描述（可选）'}),
        }
        labels = {
            'name': '分类名称',
            'description': '分类描述',
        }