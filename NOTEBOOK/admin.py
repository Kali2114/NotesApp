from django.contrib import admin

from NOTEBOOK.models import Note, CustomUser, UserRating, Category

admin.site.register(Note)
admin.site.register(CustomUser)
admin.site.register(UserRating)
admin.site.register(Category)

