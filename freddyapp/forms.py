from django import forms

from freddyapp.models import Animatronic


class AnimatronicForm(forms.ModelForm):
    class Meta:
        model = Animatronic
        fields = '__all__'
        labels = {
            'animal': 'Animal type',
            'build_date': 'Build date',
        }
        widgets = {
            'build_date': forms.DateInput(attrs={'type': 'date'}),
            'parties': forms.CheckboxSelectMultiple()
        }
        error_messages = {
            'name': {
                'max_length': 'The name of the animatronic must not be more than 50 characters long',
                'required': 'The name of the animatronic is required'
            },
            'build_date': {
                'required': 'The build date is required'
            }
        }