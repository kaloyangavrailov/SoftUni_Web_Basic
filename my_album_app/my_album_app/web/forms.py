from django import forms
from django.forms import models

from exam_prep_5.web.models import Profile, Album


class BaseProfileForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        }


class CreateProfileForm(BaseProfileForm):
    pass


class ProfileDeleteForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class BaseAlbumForm(models.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist_name': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'})
        }


class AddAlbumForm(BaseAlbumForm):
    pass


class AlbumEditForm(BaseAlbumForm):
    pass


class AlbumDeleteForm(BaseAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['album_name'].disabled = True
        self.fields['artist_name'].disabled = True
        self.fields['genre'].disabled = True
        self.fields['description'].disabled = True
        self.fields['image_url'].disabled = True
        self.fields['price'].disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
