from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):
    list_display=('id','user','content','posted_at')
    list_display_links=('id','user','content','posted_at')

admin.site.register(Post,PostAdmin)

