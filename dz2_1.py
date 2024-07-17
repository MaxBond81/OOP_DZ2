#из списка строк удаляем непечатные символы
with open('recipes.txt') as f:
   list_recipes=f.readlines()
   list_recipes_strip=[]
   for k in list_recipes:
       list_recipes_strip.append(k.strip())

#разделяем список на блюда
list_recipes_strip=','.join(list_recipes_strip).split(",,")
list_recipes_diches = []
for k in list_recipes_strip:
   list_recipes_diches.append(k.split(','))

#удаляем из блюд символ "|"
list_recipes_all=[]
for dishes in list_recipes_diches:
   list_recipes_all_0=[]
   for k in dishes[0:2]:
      list_recipes_all_0.append(k)
   for k in dishes[2:]:
      k=k.split(' | ')
      list_recipes_all_0.append(k)
   list_recipes_all.append(list_recipes_all_0)

#создаем необходимый  словарь
cook_book = {}
for dishes in list_recipes_all:
   cook_book.setdefault(dishes[0], [])
   for k in dishes[2:]:
      ingredient = {}
      ingredient.setdefault("name_ingredient",k[0])
      ingredient.setdefault("quantity", int(k[1]))
      ingredient.setdefault("measure", k[2])
      cook_book[dishes[0]].append(ingredient)

#создаем список ингридиентов необходимых блюд
def get_shop_list_by_dishes(dishes, person):
   ingredients_list = []
   for k in dishes:
      for dish, ingredient in cook_book.items():
         if dish == k:
            ingredients_list.append(ingredient)

#формируем необходимый словарь
   new_dict ={}
   for dishes in ingredients_list:
      for ingredient in dishes:
         if ingredient["name_ingredient"] not in new_dict:
            new_dict[ingredient["name_ingredient"]] = {"measure": ingredient["measure"], "quantity": person*ingredient["quantity"]}
         else:
            new_dict[ingredient["name_ingredient"]]["quantity"] += person*ingredient['quantity']
   print(new_dict)

get_shop_list_by_dishes(["Фахитос","Омлет"], 2)




