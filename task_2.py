cook_book = {}

with open('recipes.txt') as f:
    for line in f:
        dish_name = line.strip()
        new_list = []
        count = f.readline()
        
        # print(line)
        # print(count)
        
        for i in range(int(count)):
            dish_ing = f.readline()
            ingredient_name, quantity, measure  = dish_ing.strip().split(' | ')
            new_list.append({'ingredient_name': ingredient_name, 'quantity': quantity,'measure': measure})
            dep = {dish_name: new_list}
        separate = f.readline()
        cook_book.update(dep)

    print(f'cook_book = {cook_book}')

def list_of_stores_with_ingredients(dishes, person_count):
    total = {}
    for dish in dishes:
        if dish in cook_book:
          for exist in cook_book[dish]:

            total = {'measure': cook_book['measure'],'quantity': (int(cook_book['quantity'])*int(person_count))}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    return total

list_of_stores_with_ingredients(["Омлет"], 2)
