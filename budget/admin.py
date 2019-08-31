from django.contrib import admin

# Register your models here.
from .models import Setting, Publication, Document, Category, Work, Year


admin.site.register(Setting)
admin.site.register(Publication)
admin.site.register(Document)
admin.site.register(Category)
admin.site.register(Work)
admin.site.register(Year)