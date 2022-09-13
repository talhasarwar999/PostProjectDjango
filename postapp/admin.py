from django.contrib import admin
from .models import *



# Registered models
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(PostComment)
admin.site.register(PostMedia)