from django.contrib import admin
from read.models import Book, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id", "username", "first_name", "last_name", "birthday"
    )
    list_filter = ("username", "birthday",)
    search_fields = ("username", "birthday",)
    empty_value_display = '-пусто-'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "pub_date",)
    list_filter = ("id", "pub_date",)
    search_fields = ("title", "pub_date",)
    empty_value_display = '-пусто-'
