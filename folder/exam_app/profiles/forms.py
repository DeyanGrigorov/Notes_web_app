from django import forms
from django.db import models

from exam_app.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfile(ProfileForm):
    pass
