from django.contrib import admin
from .models import Curation, Location, Category, Purpose1, Purpose2, Place

admin.site.register(Curation)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Purpose1)
admin.site.register(Purpose2)
admin.site.register(Place)

