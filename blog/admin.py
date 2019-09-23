from django.contrib import admin
from .models import Post

admin.site.register(Post)

# we have created a new GUI for Post.
# in admin.py we have crated a new data base field for Post class.
# While we open localhost:8000/admin/ we will see a new filed for Post.
