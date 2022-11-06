from django.contrib import admin
from .models import User, Immobilier, Appart, Ville

admin.site.register(User)
admin.site.register(Immobilier)
admin.site.register(Appart)
admin.site.register(Ville)