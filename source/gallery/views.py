from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView, DeleteView

from gallery.forms import PhotoForm
from gallery.models import Photo, Album


class IndexView(TemplateView):
    template_name = 'index.html'


class PhotoListView(ListView):
    model = Photo
    context_object_name = 'photos'
    queryset = Photo.objects.filter(is_private=False).order_by("-created_at")
    template_name = 'photo/list.html'


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


class PhotoDetailView(DetailView):
    template_name = "photo/detail.html"
    model = Photo
    context_object_name = 'photo'


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


class AlbumListView(ListView):
    model = Album
    context_object_name = 'album'
    queryset = Album.objects.filter(is_private=False).order_by("-created_at")
    template_name = 'album/list.html'

