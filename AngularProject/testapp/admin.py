from django.contrib import admin
from testapp.models import Educational
# Register your models here.
class EducationalAdmin(admin.ModelAdmin):
    list_display=('item','price','qty')

admin.site.register(Educational,EducationalAdmin)
