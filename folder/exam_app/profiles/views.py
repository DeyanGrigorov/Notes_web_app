from django.shortcuts import render, redirect

from exam_app.core.profile_utils import get_profile
from exam_app.notes.models import Note
from exam_app.profiles.forms import ProfileForm


def profile_page(request):
    profile = get_profile()

    context = {
        'profile': profile,

    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    notes = Note.objects.all()
    profile.delete()
    notes.delete()
    return redirect("home")
