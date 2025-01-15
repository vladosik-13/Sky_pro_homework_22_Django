# forms.py
from django import forms
from django.core.exceptions import ValidationError
from catalog.models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image', 'category']

    def clean_name(self):
        data = self.cleaned_data['name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word.lower() in data.lower():
                raise ValidationError(f'Название не должно содержать слова "{word}"')
        return data

    def clean_description(self):
        data = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word.lower() in data.lower():
                raise ValidationError(f'Описание не должно содержать слова "{word}"')
        return data

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена не может быть отрицательной.')
        return price

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'введите наименование продукта'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'введите описание продукта'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'введите цену'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})

class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_published']