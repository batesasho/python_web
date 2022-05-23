from django.shortcuts import render, redirect

from exam.web.forms import CreateProfileForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from exam.web.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    profile = get_profile()
    albums = Album.objects.all()
    if not profile:
        return redirect('profile create')

    context = {
            'albums': albums,
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    if request.method == "POST":
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = AddAlbumForm()
    context = {
            'form': form,
    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk = pk)
    context = {
            'album': album,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk = pk)
    if request.method == "POST":
        form = EditAlbumForm(request.POST, instance = album)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = EditAlbumForm(instance = album)
    context = {
            'form': form,
            'album': album,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk = pk)
    if request.method == "POST":
        form = DeleteAlbumForm(request.POST, instance = album)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = DeleteAlbumForm(instance = album)
    context = {
            'form': form,
            'album': album,
    }
    return render(request, 'delete-album.html', context)


def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
            'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    total_number_of_albums = len(Album.objects.all())
    context = {
            'profile': profile,
            'total_number_of_albums': total_number_of_albums,
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = DeleteProfileForm(instance = profile)
    context = {
            'form': form,
    }
    return render(request, 'profile-delete.html', context)
