

def make_dough(ingredient1,ingredient2):
    if (ingredient1 == 'water')and(ingredient2 == 'flour'):
        return 'dough'
    elif (ingredient1 == 'flour')and(ingredient2 == 'water'):
        return 'dough'
    else:
        return 'Not dough'

def bake_dough(ingredient):
    if ingredient == 'dough':
        return 'naan'
    else:
        return 'not naan'

def run_factory(ing1,ing2):
    if (ing1 == 'water')and(ing2 == 'flour'):
        return 'naan'
    if (ing1 == 'flour')and(ing2 == 'water'):
        return 'naan'
    else:
        return 'not naan'