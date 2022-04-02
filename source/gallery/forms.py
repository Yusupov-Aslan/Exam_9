from django.contrib.auth import get_user_model

from gallery.models import Photo
from django import forms

UserModel = get_user_model()


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        user_id = None
        if 'user_id' in kwargs:
            user_id = kwargs.pop('user_id')
        super(PhotoForm, self).__init__(*args, **kwargs)
        if user_id:
            user = UserModel.objects.get(id=user_id)
            self.fields['album'].queryset = user.albums.all()
