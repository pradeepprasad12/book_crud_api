from django.contrib import admin
from.models import User_book

# Register your models here.
@admin.register(User_book)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','book_name','book_author')
