from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView

from .forms import CustomUserCreationForm
from .models import Note, UserRating, Category


class AddNoteView(CreateView):
    model = Note
    fields = ['title', 'content', 'priority', 'category', 'pinned']
    success_url = reverse_lazy('home')
    template_name = 'add_note.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateNoteView(UpdateView):
    model = Note
    fields = ['title', 'content', 'priority', 'category', 'pinned']
    template_name = 'update_note.html'

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse_lazy('detail_note', kwargs={'pk': pk})

class DeleteNoteView(DeleteView):
    model = Note
    success_url = reverse_lazy('home')
    template_name = 'delete_note.html'

class HomeView(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = Note
    template_name = 'home.html'
    context_object_name = 'notes'

    def get_queryset(self):
        queryset = Note.objects.filter(user=self.request.user)
        query = self.request.GET.get('query')
        sort_by = self.request.GET.get('sort_by')
        category_name = self.request.GET.get('category')

        if query:
            queryset = queryset.filter(title__icontains=query)

        if category_name:
            queryset = queryset.filter(category__name=category_name)

        pinned_notes = queryset.filter(pinned=True)
        unpinned_notes = queryset.filter(pinned=False)
        pinned_notes = pinned_notes.order_by('title')

        if sort_by == 'name':
            unpinned_notes = unpinned_notes.order_by('title')
        elif sort_by == 'date':
            unpinned_notes = unpinned_notes.order_by('created_at')
        elif sort_by == 'priority':
            priority_order = {'High': 3, 'Normal': 2, 'Low': 1, 'None': 0}
            unpinned_notes = sorted(unpinned_notes, key=lambda x: priority_order.get(x.priority), reverse=True)

        sorted_notes = list(pinned_notes) + list(unpinned_notes)

        return sorted_notes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        pinned_notes = [note for note in queryset if note.pinned]
        context['pinned_notes'] = pinned_notes
        query = self.request.GET.get('query')
        sort_by = self.request.GET.get('sort_by')
        if query:
            context['searched_notes'] = queryset
        context['sort_by'] = sort_by
        context['categories'] = Category.objects.all()
        context['current_category'] = self.request.GET.get('category')
        return context

class DetailNoteView(DetailView):
    model = Note
    template_name = 'detail_note.html'
    context_object_name = 'note'

    def get_success_url(self):
        return reverse('detil_note', kwargs={'pk': self.object.pk}
        + f'?sort_by={self.request.GET.get("sort_by")}')

class CustomLoginView(LoginView):
    template_name = 'login.html'

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_rating = UserRating.objects.get(user=self.request.user)
        user_notes_count = Note.objects.filter(user=self.request.user).count()
        context['username'] = self.request.user.username
        context['user_rating'] = user_rating.rating
        context['notes_count'] = user_notes_count
        return context

def pin_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.pinned = True
    note.save()
    return redirect('home')

def unpin_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.pinned = False
    note.save()
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')
