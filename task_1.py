from pprint import pprint
cook_book = {}

with open('recipes.txt') as f:
    for line in f:
        dish_name = line.strip()
        new_list = []
        count = f.readline().strip()

        for _ in range(int(count)):
            dish_ing = f.readline().strip()
            ingredient_name, quantity, measure  = dish_ing.split('|')
            new_list.append({'ingredient_name': ingredient_name, 'quantity': quantity,'measure': measure})
            dep = {dish_name: new_list}
        separate = f.readline()
        cook_book.update(dep)
    cook_book[dish_name] = new_list

print (f'cook_book = {cook_book}')

  
    



