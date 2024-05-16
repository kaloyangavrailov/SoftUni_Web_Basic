from django.shortcuts import render, redirect

from exam_prep_5.web.forms import CreateProfileForm, AddAlbumForm, AlbumEditForm, AlbumDeleteForm, ProfileDeleteForm
from exam_prep_5.web.models import Profile, Album


def get_profile():
    try:
        profile = Profile.objects.get()
    except Profile.DoesNotExist:
        profile = None

    return profile


# Create your views here.


def get_album(pk):
    try:
        album = Album.objects.filter(pk=pk).get()
    except Album.DoesNotExist:
        album = None

    return album


def get_all_albums():
    try:
        albums = Album.objects.all()
    except Album.DoesNotExist:
        albums = None

    return albums


def index(request):
    profile = get_profile()
    has_profile = False
    if profile:
        albums = get_all_albums()
        has_profile = True
        context = {
            'has_profile': has_profile,
            'albums': albums
        }
        return render(request, 'core/home-with-profile.html', context=context)
    else:
        if request.method == "GET":
            form = CreateProfileForm()
        else:
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        context = {
            'form': form,
            'has_profile': has_profile
        }
        return render(request, 'core/home-no-profile.html', context=context)


def album_add(request):
    if request.method == "GET":
        form = AddAlbumForm()
    else:
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'albums/add-album.html', context=context)


def album_details(request, pk):
    album = get_album(pk)
    if album:
        context = {
            'album': album
        }
    return render(request, 'albums/album-details.html', context=context)


def album_edit(request, pk):
    album = get_album(pk)

    if request.method == "GET":
        form = AlbumEditForm(instance=album)
    else:
        form = AddAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album
    }
    return render(request, 'albums/edit-album.html', context=context)


def album_delete(request, pk):
    album = get_album(pk)
    if request.method == "GET":
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'album': album
    }
    return render(request, 'albums/delete-album.html', context=context)


def profile_details(request):
    profile = get_profile()
    albums = get_all_albums()
    albums_count = albums.count()
    context = {
        'profile': profile,
        'album_count': albums_count
    }
    return render(request, 'profiles/profile-details.html', context=context)


def profile_delete(request):
    profile = get_profile()
    if request.method == "GET":
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'profiles/profile-delete.html', context=context)
