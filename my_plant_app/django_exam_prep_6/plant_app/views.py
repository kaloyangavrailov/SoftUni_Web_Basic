from django.shortcuts import render, redirect

from django_exam_prep_6.plant_app import forms
from django_exam_prep_6.plant_app.models import Profile, Plant


def get_profile():
    try:
        profile = Profile.objects.get()
    except Profile.DoesNotExist:
        profile = None
    return profile


def get_all_plants():
    try:
        plants = Plant.objects.all()
    except Plant.DoesNotExist:
        plants = None
    return plants


def get_plant(pk):
    try:
        plant = Plant.objects.filter(pk=pk).get()
    except Plant.DoesNotExist:
        plant = None
    return plant


# Create your views here.
def index(request):
    profile = get_profile()
    has_profile = False
    if profile:
        return redirect('catalogue')
    else:
        context = {
            'has_profile': has_profile
        }
        return render(request, 'core/home-page.html', context=context)


def catalogue(request):
    profile = get_profile()
    has_profile = None
    if profile:
        has_profile = True
    else:
        has_profile = False

    plants = get_all_plants()
    has_plants = False

    if plants:
        has_plants = True
        context = {
            'has_plants': has_plants,
            'plants': plants,
            'has_profile': has_profile,
        }
        return render(request, 'core/catalogue.html', context=context)
    elif not has_profile:
        return redirect('index')
    else:
        context = {
            'has_plants': has_plants,
            'has_profile': has_profile,
        }
        return render(request, 'core/catalogue.html', context=context)


def plant_create(request):
    has_profile = True
    if request.method == "GET":
        form = forms.CreatePlantForm()
    else:
        form = forms.CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'has_profile': has_profile
    }
    return render(request, 'plant/create-plant.html', context=context)


def plant_details(request, pk):
    has_profile = True
    plant = get_plant(pk)
    context = {
        'plant': plant,
        'has_profile': has_profile
    }
    return render(request, 'plant/plant-details.html', context=context)


def plant_edit(request, pk):
    plant = get_plant(pk)
    if request.method == "GET":
        form = forms.PlantEditForm(instance=plant)
    else:
        form = forms.PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
        return redirect('catalogue')
    context = {
        'form': form,
        'plant': plant
    }
    return render(request, 'plant/edit-plant.html', context=context)


def plant_delete(request, pk):
    plant = get_plant(pk)
    if request.method == "GET":
        form = forms.PlantDeleteForm(instance=plant)
    else:
        form = forms.PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'plant': plant
    }
    return render(request, 'plant/delete-plant.html', context=context)


def profile_create(request):
    if request.method == "GET":
        form = forms.CreateProfileForm()
    else:
        form = forms.CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'profile/create-profile.html', context=context)


def profile_details(request):
    profile = get_profile()
    plants = get_all_plants()
    plants_count = plants.count()
    has_profile = True
    context = {
        'profile': profile,
        'plants_count': plants_count,
        'has_profile': has_profile
    }
    return render(request, 'profile/profile-details.html', context=context)


def profile_edit(request):
    profile = get_profile()
    has_profile = True
    if request.method == "GET":
        form = forms.EditProfileForm(instance=profile)
    else:
        form = forms.EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    context = {
        'form': form,
        'has_profile': has_profile
    }
    return render(request, 'profile/edit-profile.html', context=context)


def profile_delete(request):
    profile = get_profile()
    if request.method == "GET":
        form = forms.DeleteProfileForm(instance=profile)
    else:
        form = forms.DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'profile/delete-profile.html', context=context)
