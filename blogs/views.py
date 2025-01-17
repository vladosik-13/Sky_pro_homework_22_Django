from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/blog_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'object'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.views_count += 1
        self.object.save()
        return response


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'is_published']
    success_url = reverse_lazy('blogs:blog_list')
    template_name = 'blogs/blog_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание нового блога'
        return context


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'is_published']
    template_name = 'blogs/blog_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование блога'
        return context

    def get_success_url(self):
        return reverse_lazy('blogs:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blog_list')
    template_name = 'blogs/blog_confirm_delete.html'