"""forms.py"""
from django.core.files import File
import requests
import os
from django import forms
from .models import *
from django.core.files.temp import NamedTemporaryFile

class UploadForm(forms.ModelForm):

    url = forms.CharField(
        max_length=256, required=False, widget=forms.TextInput(
            attrs={'class': 'form-control w-100'}
        )
    )

    class Meta:
        model = Image
        fields = (
            'image',
            'url'
        )

    def clean(self):
        cleaned = super().clean()
        print(cleaned)
        image = cleaned.get('image')
        url = cleaned.get('url')
        if (not image and not url) or (image and url):
            raise forms.ValidationError('Fill one field')
        return cleaned

    def clean_url(self):
        try:
            if self.cleaned_data.get('url'):
                url = self.cleaned_data.get('url')
                r = requests.get(url)
                if r.status_code != requests.codes.ok:
                    raise forms.ValidationError('Enter correct url')
                return url
            else:
                return self.cleaned_data.get('url')
        except:
            raise forms.ValidationError('Enter correct url like http://example.com/image.jpg')

    def save(self):
        print(self.cleaned_data)
        if self.cleaned_data.get('url'):
            url = self.cleaned_data.get('url')
            r = requests.get(url)
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(r.content)
            img_temp.flush()
            new_image = Image()
            new_image.image.save(
                os.path.basename(self.cleaned_data.get('url')),
                File(img_temp)
            )
            return new_image
        else:
            new_image = Image.objects.create(
                image=self.cleaned_data.get('image'),
                url=''
            )
            return new_image