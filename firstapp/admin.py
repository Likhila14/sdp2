from django.contrib import admin
from .models import Anniversary, Birthday, Register

admin.site.register(Register)
admin.site.register(Birthday)
admin.site.register(Anniversary)

# Register your models here.
