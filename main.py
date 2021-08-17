class Cook_book():

    def my_cook_book(self, input_file):
        with open('riceptes.txt', 'r') as menu:
            self.cook_book = {}
            for line in menu:
                dish_name = line.strip()
                reciptes = int(menu.readline().strip())
                ingredients_dish = []
                for count in range(reciptes):
                    string_data = menu.readline().strip()
                    string_data = ''.join(string_data.split())
                    string_data = string_data.split('|')
                    ingredients = {'ingredient_name': string_data[0], 'quantity': int(string_data[1]),
                               'measure': string_data[2]}
                    ingredients_dish.append(ingredients)
                    self.cook_book[dish_name] = ingredients_dish
                menu.readline()
            return print(self.cook_book)


    def get_shop_list_by_dishes(self, dishes, person_count):
        if getattr(self, 'cook_book', 'No') == 'No':
            print('Импортируйте файл кулинарной книги, перед тем, как формировать лист покупок!')
        else:
            result = {}
            for dish in dishes:
                if dish in self.cook_book:
                    new_shop_list = self.cook_book[dish]
                    for element in new_shop_list:
                        ingredient = element['ingredient_name']
                        measure = element['measure']
                        quantity = int(element['quantity']) * person_count
                        result[ingredient] = {measure: quantity}
                else:
                    print('Такого рецепта в книге еще нет.')
        return print(result)


book = Cook_book()
book.my_cook_book('riceptes.txt')
book.get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 10)
