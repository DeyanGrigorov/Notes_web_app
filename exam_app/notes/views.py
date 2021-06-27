from django.shortcuts import render, redirect

from exam_app.core.profile_utils import get_profile
from exam_app.notes.forms import AddNote, EditNote, DeleteNote
from exam_app.notes.models import Note


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    notes = Note.objects.all()

    context = {
        'notes': notes
    }

    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = AddNote(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddNote()

    context = {
        'form': form
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditNote(instance=note)

    context = {
        'form': form
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    else:
        form = DeleteNote(instance=note)

    context = {
        'form': form
    }
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)
