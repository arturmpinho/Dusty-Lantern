from django import forms
from auctions.models import Auction
from products.models import Product, Image, Category, Condition
from .widgets import CustomClearableFileInput
from django.forms.widgets import DateTimeInput


class CustomDateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    images = forms.ImageField(label="Image", required=True,
                              widget=(CustomClearableFileInput(
                                      attrs={'multiple': True})))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        condition = Condition.objects.all()
        category = Category.objects.all()

        for field_name, field in self.fields.items():
            if field_name == "category":
                field.widget.attrs['class'] = 'border-black rounded-0 \
                    mt-2 fs-4 form-select'
            elif field_name == "condition":
                field.widget.attrs['class'] = 'border-black rounded-0 \
                    mt-2 fs-4 form-select'
            else:
                field.widget.attrs['class'] = 'border-black rounded-0 \
                    mt-2 fs-4'


class EditProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    images = forms.ImageField(label="Image", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        condition = Condition.objects.all()
        category = Category.objects.all()

        for field_name, field in self.fields.items():
            if field_name == "category":
                field.widget.attrs['class'] = 'border-black rounded-0 \
                    mt-2 fs-4 form-select'
            elif field_name == "condition":
                field.widget.attrs['class'] = 'border-black rounded-0 \
                    mt-2 fs-4 form-select'
            else:
                field.widget.attrs['class'] = 'border-black rounded-0 \
                    mt-2 fs-4'


class AddAuctionForm(forms.ModelForm):

    class Meta:
        model = Auction
        exclude = ('is_sold',)
        widgets = {
            'start_date_time': CustomDateTimeInput(),
            'end_date_time': CustomDateTimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        product = Product.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 mt-2 fs-4'


class EditAuctionForm(forms.ModelForm):

    class Meta:
        model = Auction
        exclude = ('is_sold',)
        widgets = {
            'start_date_time': DateTimeInput(attrs={'type': 'text'}, ),
            'end_date_time': DateTimeInput(attrs={'type': 'text'}, ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        product = Product.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 mt-2 fs-4'
