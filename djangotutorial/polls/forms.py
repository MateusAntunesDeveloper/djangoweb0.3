from django import forms

class BuscaEstoque(forms.Form):
    pass

class ContactForm(forms.Form):
    teste = forms.ChoiceField(
 
    )
    name = forms.CharField(
        max_length=100,
        label="Your name user",
        required=True,
        help_text="Please select your correct name"
    )

    email = forms.EmailField(
        label="Select your gmail",
        help_text="Precisamos do seu mail para"
    )
    date = forms.DateField(

    )

    idade = forms.IntegerField(

    )
















