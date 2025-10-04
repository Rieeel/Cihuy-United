from django import forms
from django.forms import ModelForm
from main.models import Category, Product
from django.utils.html import strip_tags


class ProductForm(ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select category",
        widget=forms.Select(attrs={'class': 'w-full bg-[#1a2233] text-white rounded-md p-2'})
    )
    class Meta:
        model = Product
        fields = ["name", "price", "stock", "description",
                  "thumbnail", "category", "is_featured", ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-md bg-[#1a2233] text-white border border-[#374151] focus:outline-none focus:ring-2 focus:ring-[#90caf9]'
            }),
            'category': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 rounded-md bg-[#0f172a] text-white border border-[#374151] focus:outline-none focus:ring-2 focus:ring-[#90caf9]'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 rounded-md bg-[#0f172a] text-white border border-[#374151] focus:outline-none focus:ring-2 focus:ring-[#90caf9]'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 rounded-md bg-[#0f172a] text-white border border-[#374151] focus:outline-none focus:ring-2 focus:ring-[#90caf9]'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 rounded-md bg-[#0f172a] text-white border border-[#374151] focus:outline-none focus:ring-2 focus:ring-[#90caf9]',
                'rows': 4
            }),
            'thumbnail': forms.URLInput(attrs={
                'class': 'w-full px-3 py-2 bg-[#1a2233] border border-[#374151] rounded-md text-gray-200 focus:outline-none focus:ring-2 focus:ring-[#90caf9]',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
