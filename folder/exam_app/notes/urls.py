from django.urls import path

from exam_app.notes.views import home, add_note, edit_note, delete_note, note_details

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', note_details, name='note details'),

]
