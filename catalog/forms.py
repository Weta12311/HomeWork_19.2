from django.forms import ModelForm, ValidationError, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field, in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Product
        exclude = ("user",)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        bad_words_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                          'радар']

        for word in bad_words_list:
            if word in cleaned_data:
                raise ValidationError('Торвар с таким названием запрещен к продадаже на этой площадке')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        bad_words_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                          'радар']
        for word in bad_words_list:
            if word in cleaned_data:
                raise ValidationError('Торвар с таким описанием запрещен к продадаже на этой площадке')

        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Version
        fields = "__all__"


