from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)
    
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='') #aqui mostra como salvar a imagem abrindo essas pastas. O blank permite que fique sem imagem e o default vazio, pode quebrar o layout da página, mas é possível fazer
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None #ligação entre as tabelas, se alguem apagar a categoria, tem como deletar a relação, vai setar nulo, igual a true
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    
    def __str__(self):
        return self.title
    
    #aula 52 ele pediu pra instalar o pillow - biblioteca de imagens.