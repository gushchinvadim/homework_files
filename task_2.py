cook_book = {}

with open('recipes.txt') as f:
    for line in f:
        dish_name = line.strip()
        new_list = []
        count = f.readline()

        for i in range(int(count)):
            dish_ing = f.readline()
            ingredient_name, quantity, measure = dish_ing.strip().split(' | ')
            new_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            dep = {dish_name: new_list}
        separate = f.readline()
        cook_book.update(dep)

    # print(f'cook_book = {cook_book}')


def list_of_stores_with_ingredients(dishes: list, person_count: int):
    total = {}
    for dish in dishes:
        if dish in cook_book.keys():
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                total[ingredient["ingredient_name"]] = {
                    "measure": ingredient["measure"],
                    "quantity": int(ingredient["quantity"]) * person_count
                }
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    return total


result = list_of_stores_with_ingredients(["Example", "Омлет", "Фахитос"], 5)
print(result)

list_of_stores_with_ingredients(["Омлет"], 2)
