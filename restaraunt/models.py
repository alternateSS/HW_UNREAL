from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.password = 'hashed_password'
        super().save(*args, **kwargs)
        print(f'Пользователь под почтой {self.email}  сохранен')

    def __str__(self):
        return self.email


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    card_number = models.IntegerField()

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    extra_price = models.IntegerField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20)
    start_price = models.IntegerField()
    orders = models.ManyToManyField(Ingredient, related_name='food', through='Order')
    type_of_cuisine = models.CharField(max_length=20)
    calories = models.IntegerField()


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateField(auto_now_add=True)
    vegetarian = models.BooleanField(default=False, null=True)
    food_status = models.CharField(max_length=15, null=True)
    final_price = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.food.name} - {self.ingredient.name} - {self.client.name} - {self.worker.name}'

    # def save(self, *args, **kwargs):
    #     for ingredient in Ingredient.objects.filter(name=self.ingredient.name):
    #         if ingredient.name in ['Рыба', 'Курица', 'Говядина']:
    #             self.vegetarian = False
    #         self.vegetarian = True
    #     super().save(*args, **kwargs)


class FoodCounter(Order):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if self.ingredient.name in ['Рыба', 'Курица', 'Говядина']:
            self.vegetarian = False
        else:
            self.vegetarian = True
        calories_count = self.food.calories + self.ingredient.calories
        if calories_count <= 700:
            self.food_status = 'Перекус'
        elif calories_count <= 1200:
            self.food_status = 'Обед'
        elif calories_count > 1200:
            self.food_status = 'Обжиралово'
        self.final_price = self.food.start_price + self.ingredient.extra_price
        super().save(*args, **kwargs)









