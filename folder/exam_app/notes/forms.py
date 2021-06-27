from django import forms

from exam_app.notes.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class AddNote(NoteForm):
    pass


class DeleteNote(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():

            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class EditNote(NoteForm):
    pass
