from django.shortcuts import render, redirect

from django_exam_prep_8.fruit_app.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from django_exam_prep_8.fruit_app.models import Profile, Fruit


def get_profile():
    try:
        profile = Profile.objects.get()
    except Profile.DoesNotExist:
        profile = None
    return profile


def get_all_fruits():
    try:
        fruits = Fruit.objects.all()
    except Fruit.DoesNotExist:
        fruits = None
    return fruits


def get_fruit(pk):
    try:
        fruit = Fruit.objects.filter(pk=pk).get()
    except Fruit.DoesNotExist:
        fruit = None
    return fruit


def index(request):
    has_profile = False
    profile = get_profile()
    if profile:
        has_profile = True
    context = {
        'has_profile': has_profile
    }
    return render(request, 'core/index.html', context=context)


def dashboard(request):
    has_profile = True
    fruits = get_all_fruits()
    context = {
        'has_profile': has_profile,
        'fruits': fruits
    }
    return render(request, 'core/dashboard.html', context=context)


def fruit_create(request):
    profile = get_profile()

    has_profile = True
    if request.method == "GET":
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.instance.owner = profile
            form.save()
            return redirect('dashboard')
    context = {
        'has_profile': has_profile,
        'form': form
    }
    return render(request, 'fruit/create-fruit.html', context=context)


def fruit_details(request,pk):
    has_profile = True
    fruit = get_fruit(pk)
    context = {
        'fruit': fruit,
        'has_profile': has_profile
    }
    return render(request, 'fruit/details-fruit.html', context=context)


def fruit_edit(request, pk):
    has_profile = True
    fruit = get_fruit(pk)
    if request.method == "GET":
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'has_profile': has_profile,
        'form': form,
        'fruit': fruit
    }
    return render(request, 'fruit/edit-fruit.html', context=context)


def fruit_delete(request,pk):
    has_profile = True,
    fruit = get_fruit(pk)
    if request.method == "GET":
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'has_profile': has_profile,
        'fruit': fruit,
        'form': form
    }
    return render(request, 'fruit/delete-fruit.html', context=context)


def profile_create(request):
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'profile/create-profile.html', context=context)


def profile_details(request):
    profile = get_profile()
    fruits = get_all_fruits()
    has_profile = True
    fruits_count = fruits.count()
    context = {
        'profile': profile,
        'fruits': fruits,
        'has_profile': has_profile,
        'fruits_count': fruits_count
    }
    return render(request, 'profile/details-profile.html', context=context)


def profile_edit(request):
    has_profile = True,
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
    has_profile = True
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
