from django.contrib import admin
from first_app.models import Post, Topic, AccessRecord, Webpage

admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
