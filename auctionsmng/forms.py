from django import forms
from auctions.models import Auction
from products.models import Product, Image, Category, Condition
from .widgets import CustomClearableFileInput


class DateInput(forms.DateInput):
    input_type = 'date'

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'creation_date': DateInput()
        }  
        
    image = forms.ImageField(label="Image", required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        condition = Condition.objects.all()
        category = Category.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class AuctionForm(forms.ModelForm):

    class Meta:
        model = Auction
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        product = Product.objects.all()

        # self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'