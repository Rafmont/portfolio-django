from django.contrib import admin
from .models import Post
from .models import Project
from .models import Formation
from .models import Latest

admin.site.register(Post)
admin.site.register(Project)
admin.site.register(Formation)
admin.site.register(Latest)