from django.contrib import admin

# import your models
from collection.models import Profile

# setup automated slug creation
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
