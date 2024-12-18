from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Product, Customer, Order, Profile

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Profile)


class ProfileInLine(admin.StackedInline):
  model = Profile

class UserAdmin(admin.ModelAdmin):
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  inlines = [ProfileInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
