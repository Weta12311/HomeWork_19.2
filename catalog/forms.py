from django.forms import ModelForm, ValidationError

from catalog.models import Product


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

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
