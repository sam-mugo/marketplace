from distutils.command.upload import upload
from tabnanny import verbose
import uuid
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    """Category attributes"""

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
        
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product attributes"""

    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    # subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()
    stock = models.IntegerField()
    image_url = CloudinaryField('image')

    def __str__(self):
        return f"{self.name}___ @{self.price}____________{self.category_id.name}"


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

