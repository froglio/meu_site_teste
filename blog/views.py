from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from . models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'custom' # Se nao for usar, o padrao é object

class BlogCreateView(SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['autor', 'titulo', 'conteudo']
    
    success_message = "%(calculated_field)s - Criado com sucesso!"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.titulo,
        )

class BlogUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['autor', 'titulo', 'conteudo']
    
    success_message = "%(calculated_field)s - Alterado com sucesso!"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.titulo,
        )

class BlogDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')

    success_message = "Registro deletado com sucesso!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)