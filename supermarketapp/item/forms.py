from django import forms
from .models import Category, Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ItemForm(forms.ModelForm):
    code = forms.CharField(label='Mã hàng hóa', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mã hàng hóa'
    }))

    name = forms.CharField(label='Tên mặt hàng', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tên mặt hàng'
    }))

    count = forms.IntegerField(initial=0, label='Số lượng', widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))

    cost = forms.DecimalField(initial=0, label='Giá', widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))

    description = forms.CharField(label='Mô tả', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 10,
        'cols': 10,
    }), required=False)

    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Phân loại', widget=forms.Select(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = Item
        fields = ['code', 'name', 'count', 'cost', 'description', 'category']

    def clean_count(self, *args, **kwargs):
        count = self.cleaned_data.get('count')
        if count < 0:
            raise forms.ValidationError()
        return count

    def clean_cost(self, *args, **kwargs):
        cost = self.cleaned_data.get('cost')
        if cost < 0:
            raise forms.ValidationError()
        return cost


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=256, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))

    password1 = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    password2 = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
