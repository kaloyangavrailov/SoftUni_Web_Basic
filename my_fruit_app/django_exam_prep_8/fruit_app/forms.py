from django import forms
from django.forms import models

from django_exam_prep_8.fruit_app.models import Profile, Fruit


class ProfileEditForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image_url', 'age']

    labels = {
        'first_name': 'First Name',
        'email': 'Email',
        'image_url': 'Image_URL',
        'age': 'Age'
    }


class ProfileCreateForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))


    # widgets = {
    #     'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
    #     'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
    #     'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
    #     'password': forms.TextInput(attrs={'placeholder': 'Password'})
    # }


class BaseFruitForm(models.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        exclude = ('owner',)

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Fruit Name'}))
    image_url = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Fruit Description'}))
    nutrition = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Nutrition Info'}))


class FruitCreateForm(BaseFruitForm):
    pass


class FruitEditForm(BaseFruitForm):
    pass


class FruitDeleteForm(BaseFruitForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for _, f in self.fields.items():
            f.disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class ProfileDeleteForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def __set_hidden_fields(self):
        for _, f in self.fields.items():
            f.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Fruit.objects.all().delete()
            self.instance.delete()
        return self.instance
