from django_exam_prep_6.plant_app.models import Profile, Plant

from django.forms import models
from django import forms


class BaseProfileForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hidden_fields()

    def save(self, commit=True):
        if commit:
            Plant.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __hidden_fields(self):
        for _, f in self.fields.items():
            f.widget = forms.HiddenInput()


class BasePlantForm(models.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class CreatePlantForm(BasePlantForm):
    pass


class PlantEditForm(BasePlantForm):
    pass


class PlantDeleteForm(BasePlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __disable_fields(self):
        for _, f in self.fields.items():
            f.disabled = True
