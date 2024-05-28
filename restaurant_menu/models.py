from django.db import models
from django.contrib.auth.models import User


MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts")
)

STATUS = (
    (1, "Available"),
    (0, "Unavailable")
)

class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True) # Makes each meal unique and no recurrence
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    # deletes the menu item when the user/cook acc is deleted
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True) # Records timestamp
    date_updated = models.DateTimeField(auto_now=True)     # Records when the item is updated

    def __str__(self):
        return self.meal
