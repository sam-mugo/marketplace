from tabnanny import verbose
from django.db import models

# Create your models here.


class Category(models.Model):
    """Category attributes"""

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
        
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    image_url = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# class Subcategory(models.Model):
#     """SubCategory attributes"""

#     class Meta:
#         verbose_name = 'Subcategory'
#         verbose_name_plural = "Subcategories"

#     category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     description = models.TextField(max_length=1000)
#     image_url = models.CharField(max_length=150)

#     def __str__(self):
#         return self.name


class Product(models.Model):
    """Product attributes"""

    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    # subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.FloatField(max_length=100000)
    image_url = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    """Product Review attributes"""

    class Meta:
        verbose_name = 'Product Review'
        verbose_name_plural = "Product Reviews"

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    review = models.TextField(max_length=1000)
    rating = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    items = models.ManyToManyField(OrderItem)
    created_at = models.DateTimeField(auto_now_add=True)
    #order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)


    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total





