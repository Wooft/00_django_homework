from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
def index(request):
    return render(request, 'calculator/index.html')
def omlet(request):
    #Проверяем - если параметр указан, то множитель меняем на введенное значение, если нет - то множитель равен 1
    if request.GET.get('servings') == None:
        quan = 1
    else:
        quan = int(request.GET.get('servings'))
    recipe = {}
    recipe.update(DATA[request.path.strip('/')])
    for names, amount in recipe.items():
        recipe[names] = amount * quan
    context = {
        'recipe': recipe
    }
    return render(request=request, template_name='calculator/index.html', context=context)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
