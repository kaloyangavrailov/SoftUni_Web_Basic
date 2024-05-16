from django.shortcuts import render, redirect

from web_basics_exam_retake.recipe_app.forms import ProfileCreateForm, CreateRecipeForm, EditRecipeForm, \
    DeleteRecipeForm, ProfileEditForm, ProfileDeleteForm
from web_basics_exam_retake.recipe_app.models import Profile, Recipe


def get_profile():
    try:
        profile = Profile.objects.get()
    except Profile.DoesNotExist:
        profile = None
    return profile


def get_recipe(pk):
    try:
        recipe = Recipe.objects.filter(pk=pk).get()
    except Recipe.DoesNotExist:
        recipe = None
    return recipe


def get_all_recipes():
    try:
        recipes = Recipe.objects.all()
    except Recipe.DoesNotExist:
        recipes = None
    return recipes


def check_has_profile():
    profile = get_profile()
    if profile:
        return True
    else:
        return False


# Create your views here.
def index(request):
    has_profile = check_has_profile()
    context = {
        'has_profile': has_profile
    }
    return render(request, 'core/home-page.html', context=context)


def recipe_catalogue(request):
    has_profile = check_has_profile()
    recipes = get_all_recipes()
    context = {
        'has_profile': has_profile,
        'recipes': recipes
    }
    return render(request, 'core/catalogue.html', context=context)


def recipe_create(request):
    has_profile = check_has_profile()
    if request.method == "GET":
        form = CreateRecipeForm()
    else:
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe-catalogue')
    context = {
        'has_profile': has_profile,
        'form': form
    }
    return render(request, 'recipe/create-recipe.html', context=context)


def recipe_details(request, pk):
    recipe = get_recipe(pk)
    has_profile = check_has_profile()
    ingredients = recipe.ingredients.split(', ')
    context = {
        'has_profile': has_profile,
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, 'recipe/details-recipe.html', context=context)


def recipe_edit(request, pk):
    recipe = get_recipe(pk)
    has_profile = check_has_profile()
    if request.method == "GET":
        form = EditRecipeForm(instance=recipe)
    else:
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe-catalogue')
    context = {
        'has_profile': has_profile,
        'recipe': recipe,
        'form': form
    }
    return render(request, 'recipe/edit-recipe.html', context=context)


def recipe_delete(request, pk):
    recipe = get_recipe(pk)
    has_profile = check_has_profile()
    if request.method == "GET":
        form = DeleteRecipeForm(instance=recipe)
    else:
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe-catalogue')
    context = {
        'has_profile': has_profile,
        'recipe': recipe,
        'form': form
    }
    return render(request, 'recipe/delete-recipe.html', context=context)


def profile_create(request):
    has_profile = check_has_profile()
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe-catalogue')
    context = {
        'has_profile': has_profile,
        'form': form
    }
    return render(request, 'profile/create-profile.html', context=context)


def profile_details(request):
    recipes = get_all_recipes()
    recipes_count = recipes.count()
    has_profile = check_has_profile()
    profile = get_profile()
    context = {
        'has_profile': has_profile,
        'profile': profile,
        'recipes_count': recipes_count
    }
    return render(request, 'profile/details-profile.html', context=context)


def profile_edit(request):
    has_profile = check_has_profile()
    profile = get_profile()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    context = {
        'has_profile': has_profile,
        'form': form
    }
    return render(request, 'profile/edit-profile.html', context=context)


def profile_delete(request):
    has_profile = check_has_profile()
    profile = get_profile()
    if request.method == "GET":
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'has_profile': has_profile,
        'form': form
    }
    return render(request, 'profile/delete-profile.html', context=context)

