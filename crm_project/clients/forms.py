from django import forms
from .models import Client

class ClientAdminForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data['email']
        if Client.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("Клиент с таким email уже существует.")
        return email