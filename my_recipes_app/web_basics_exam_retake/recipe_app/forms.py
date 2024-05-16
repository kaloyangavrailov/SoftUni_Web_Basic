from django.forms import models
from django import forms
from web_basics_exam_retake.recipe_app.models import Profile, Recipe


class ProfileCreateForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'chef']


class CreateRecipeForm(models.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    ingredients = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'ingredient1, ingredient2, ...'}), help_text=Recipe.INGREDIENTS_HELP_TEXT)
    instructions = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter detailed instructions here...'}))
    image_url = forms.URLField(required=False,widget=forms.URLInput(attrs={'placeholder': 'Optional image URL here...'}))


class EditRecipeForm(models.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class DeleteRecipeForm(models.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

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


class ProfileEditForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __set_hidden_fields(self):
        for _, f in self.fields.items():
            f.widget = forms.HiddenInput()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Recipe.objects.all().delete()
            self.instance.delete()
        return self.instance
