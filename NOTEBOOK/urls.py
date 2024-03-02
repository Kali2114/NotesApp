
from django.urls import path

from .views import AddNoteView, UpdateNoteView, DeleteNoteView, HomeView, DetailNoteView, CustomLoginView, RegisterView, \
    logout_view, UserProfileView, pin_note, unpin_note

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('add_note/', AddNoteView.as_view(), name='add_note'),
    path('update_note/<int:pk>/', UpdateNoteView.as_view(), name='update_note'),
    path('delete_note/<int:pk>/', DeleteNoteView.as_view(), name='delete_note'),
    path('details_note/<int:pk>', DetailNoteView.as_view(), name='detail_note'),
    path('pin/<int:pk>', pin_note, name='pin_note'),
    path('unpin/<int:pk>', unpin_note, name='unpin_note'),
    path('user_profile/', UserProfileView.as_view(), name='user_profile'),
    path('category/<str:category_name>/', HomeView.as_view(), name='category_notes'),
]
