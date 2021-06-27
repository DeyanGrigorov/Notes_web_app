from django.urls import path

from exam_app.profiles.views import profile_page, create_profile, profile_delete

urlpatterns = [
    path('', profile_page, name='profile page'),
    path('create/', create_profile, name='create profile'),
    path('delete/', profile_delete, name='delete profile'),

]
