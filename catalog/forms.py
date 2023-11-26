from django import forms

from catalog.models import Product, Version

BAN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'preview', 'category', 'price', 'is_published')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if any(word in cleaned_data.lower() for word in BAN_WORDS):
            raise forms.ValidationError('Запрещённый контент')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        if any(word in cleaned_data.lower() for word in BAN_WORDS):
            raise forms.ValidationError('Запрещённый контент')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = "__all__"

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if any(word in cleaned_data.lower() for word in BAN_WORDS):
            raise forms.ValidationError('Запрещённый контент')

        return cleaned_data
