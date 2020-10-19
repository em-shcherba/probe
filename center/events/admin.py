from django.contrib import admin
from .models import User, Event, Post

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Post)
