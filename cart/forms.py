from django import forms

SIZES = (
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
)

class CartAddProductForm(forms.Form):
    Rozmiar = forms.TypedChoiceField(choices=SIZES)