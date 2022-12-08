from restaraunt.models import *


# Users
user_1 = User.objects.create(email='nikname21@gmail.com', password='defender42')
user_2 = User.objects.create(email='altywa1998@gmail.com', password='nono34')


# Clients
client = Client.objects.create(user=user_1, name='Азат Соколов', card_number=4147_5657_9878_9009)


# Workers
worker = Worker.objects.create(user=user_2, name='Алтынай Алиева', position='Оператор кассы')


# Food
food_1 = Food.objects.create(name='Шаурма', start_price=200, type_of_cuisine='Фастфуд', calories=500)
food_2 = Food.objects.create(name='Гамбургер', start_price=180, type_of_cuisine='Фастфуд', calories=350)
food_3 = Food.objects.create(name='Паста', start_price=450, type_of_cuisine='Итальянская', calories=400)
food_4 = Food.objects.create(name='Боул', start_price=600, type_of_cuisine='Европейская', calories=500)
food_5 = Food.objects.create(name='Суши', start_price=400, type_of_cuisine='Японская', calories=500)

# Ingredients
ingredients_1 = Ingredient.objects.create(name='Сыр', extra_price=80, calories=150)
ingredients_2 = Ingredient.objects.create(name='Курица', extra_price=100, calories=250)
ingredients_3 = Ingredient.objects.create(name='Говядина', extra_price=120, calories=300)
ingredients_4 = Ingredient.objects.create(name='Салат', extra_price=50, calories=50)
ingredients_5 = Ingredient.objects.create(name='Фри', extra_price=50, calories=70)
ingredients_6 = Ingredient.objects.create(name='Рыба', extra_price=120, calories=270)
ingredients_7 = Ingredient.objects.create(name='Рис', extra_price=70, calories=100)
ingredients_8 = Ingredient.objects.create(name='Творог', extra_price=100, calories=170)
ingredients_9 = Ingredient.objects.create(name='Куринные яйца', extra_price=50, calories=120)


order_1 = food_1.orders.set([ingredients_8, ingredients_1, ingredients_4, ingredients_5], through_defaults={'client':client, 'worker':worker})
# p = FoodCounter.objects.create(ingredient=ingredients_9, food=food_1, client=client, worker=worker)
# print(p.ingredient.name)
# food_2.orders.set([ingredients_2, ingredients_4], through_defaults={'client':client, 'worker':worker})
# order_2 = food_2.start_price + ingredients_2.extra_price + ingredients_4.extra_price
# print(order_2)
