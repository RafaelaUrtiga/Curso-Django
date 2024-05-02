from django.shortcuts import render, get_list_or_404, get_object_or_404 # busca uma 
#lista de elementos ou um elemento só (objeto) e se não encontra traz o erro 404
from utils.recipes.factory import make_recipe

from recipes.models import Recipe #ou .models


def home(request):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            is_published=True
        ).order_by('-id'))   
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id'))   
     
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        #'title': f'{recipes.first().category.name} - Category | '
        'title': f'{recipes.first[0].category.name} - Category | ' 
        })


def recipe(request, id):
    
    recipe = get_object_or_404(Recipe, pk=id, is_publisher=True,)
    
    
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })

'''
def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
        ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
'''


'''
def category(request, category_id):
    recipes = Recipe.objects.filter(
    category__id=category_id, #pode ser usado o filter no lugar de all
    is_published=True
    ).order_by('-id') # as 2 __ são pra chamar a FK

    if not recipes:
        # return HttpResponse(content='Not Found', status=404) 
        # pode ser dessa forma ou:
    raise Http404 # em vez de retornar levanta um erro'''
        
'''
def recipe(request, id):
    recipe = Recipe.objects.filter(
        pk=id,
        is_publisher=True,
    ).order_by('-id').first()
'''