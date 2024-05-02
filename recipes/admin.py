from django.contrib import admin
from .models import Category, Recipe
# Register your models here. para poder aparecer os models na área do admin


class CategoryAdmin(admin.ModelAdmin):
    ...
 
@admin.register(Recipe) # por decorator   
class RecipeAdmin(admin.ModelAdmin):
    ...

  
    
admin.site.register(Category, CategoryAdmin)
