from django import forms

class IngredientForm(forms.Form):
    ingredients = forms.CharField(
        label="Ingredients",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter ingredients separated by commas (e.g., tomato, onion, garlic)",
        }),
        max_length=500,
        help_text="Please separate each ingredient with a comma.",
    )
    time = forms.IntegerField(
        label="Time (in minutes)",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the time you can spend (in minutes)",
        }),
        help_text="Enter the time you want to spend cooking.",
        min_value=3,
    )
