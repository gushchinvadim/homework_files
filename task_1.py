cook_book = {}

# def my_cook_book(): 

with open('recipes.txt') as f:
    for line in f:
        dish_name = line.strip()
        # print(dish_name)
        new_list = []
        count = f.readline()

        # print(count)
        # print(count)
        
        for i in range(int(count)):
            dish_ing = f.readline()
            # print(dish_ing)
            ingredient_name, quantity, measure  = dish_ing.strip().split('|')
            new_list.append({'ingredient_name': ingredient_name, 'quantity': quantity,'measure': measure})
            dep = {dish_name: new_list}
        separate = f.readline()
        cook_book.update(dep)

    print(f'cook_book = {cook_book}')

  
    



