from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView, DeleteView

from gallery.forms import PhotoForm, AlbumForm
from gallery.models import Photo, Album, PhotoToken


class IndexView(TemplateView):
    template_name = 'index.html'


class PhotoListView(LoginRequiredMixin, ListView):
    model = Photo
    context_object_name = 'photos'
    queryset = Photo.objects.none()
    template_name = 'photo/list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Photo.objects.filter(Q(is_private=False) | Q(user=self.request.user)).order_by("-created_at")
        return Photo.objects.filter(is_private=False).order_by("-created_at")


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = "photo/create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user_id'] = self.request.user.id
        return kwargs

    def get_success_url(self):
        return reverse("gallery:photo_detail", kwargs={"pk": self.object.pk})


class PhotoDetailView(LoginRequiredMixin, DetailView):
    template_name = "photo/detail.html"
    model = Photo
    context_object_name = 'photo'


class PhotoTokenDetailView(DetailView):
    template_name = "photo/detail.html"
    model = Photo
    context_object_name = 'photo'
    pk_url_kwarg = 'token'

    def get_object(self, queryset=None):
        token = self.kwargs.get(self.pk_url_kwarg)
        pt = PhotoToken.objects.get(token=token)
        return pt.photo


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'photo/update.html'
    form_class = PhotoForm

    def get_success_url(self):
        return reverse("gallery:photo_detail", kwargs={"pk": self.object.pk})


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = reverse_lazy('gallery:photo_list')


class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    context_object_name = 'albums'
    queryset = Album.objects.none()
    template_name = 'album/list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Album.objects.filter(Q(is_private=False) | Q(user=self.request.user)).order_by("-created_at")
        return Album.objects.filter(is_private=False).order_by("-created_at")


class AlbumDetailView(LoginRequiredMixin, DetailView):
    template_name = "album/detail.html"
    model = Album
    context_object_name = 'album'


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "album/create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("gallery:album_detail", kwargs={"pk": self.object.pk})


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    context_object_name = 'album'
    template_name = 'album/update.html'
    form_class = AlbumForm

    def get_success_url(self):
        return reverse("gallery:album_detail", kwargs={"pk": self.object.pk})


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'album/delete.html'
    success_url = reverse_lazy('gallery:album_list')


class GeneratePhotoToken(View):
    def get(self, request, *args, **kwargs):
        photo_id = kwargs.get('pk')
        PhotoToken.objects.filter(photo_id=photo_id).delete()
        PhotoToken.objects.create(photo_id=photo_id)
        return redirect('gallery:photo_detail', photo_id)
