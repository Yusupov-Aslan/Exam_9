from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Album(models.Model):
    title = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name="Описание")
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False, blank=True)


class Photo(models.Model):
    image = models.FileField(verbose_name='Изображение', upload_to='images')
    description = models.CharField(max_length=128, verbose_name="Подпись")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='Автор', related_name='photos')
    album = models.ForeignKey('gallery.Album', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Альбом', related_name='photos')
    is_private = models.BooleanField(default=False, blank=True, verbose_name='Приватный?')


class FavoriteAlbum(models.Model):
    album = models.ForeignKey('gallery.Album', on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='favorite_albums')


class FavoritePhoto(models.Model):
    photo = models.ForeignKey('gallery.Photo', on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='favorite_photos')