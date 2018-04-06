from django.db import models
from django.urls import reverse
# Create your models here.



class Product(models.Model):
    #상품이름
    name = models.CharField(max_length=10)
    #수량
    sales_count = models.PositiveSmallIntegerField(default=1)

    #가격
    sell_price = models.PositiveIntegerField(default=0)



    def get_absolute_url(self):
        return reverse('shopping:productdetail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.name


class ProductType(models.Model):
    FREE = 'F'
    SMALL = 'S'
    LARGE = 'L'
    MEDIUM = 'M'
    X_LARGE = 'X'
    XX_LARGE = 'Z'
    XXX_LARGE = 'B'
    SHIRT_SIZE_CHOICES = (
        (FREE, 'FREE'),
        (SMALL, 'S'),
        (MEDIUM, 'M'),
        (LARGE, 'L'),
        (X_LARGE, 'XL'),
    )
    PANTS_SIZE_CHOICES = (
        (FREE, 'FREE'),
        (SMALL, 'S'),
        (MEDIUM, 'M'),
        (LARGE, 'L'),
        (X_LARGE, 'XL'),
        (XX_LARGE, '2XL'),
        (XXX_LARGE, '3XL'),
    )
    #상품크기
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZE_CHOICES)
    pants_size = models.CharField(max_length=1, choices=PANTS_SIZE_CHOICES)
    #상품종류
    type = models.CharField(max_length=20)
    #상품색상
    color = models.CharField(max_length=20)


    def get_absolute_url(self):
        return reverse('shopping:productdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.type


# class Category(models.Model):
#     #카테고리 이름
#     name = models.CharField(max_length=30)
#
# class SubCategory(models.Model):
#     category = models.ForeignKey(Category)
#     name = models.CharField(max_length=30)

# class ShopCategory(models.Model):
#     categories = models.ManyToManyField(Category)
#     sub_categories = models.ManyToManyField(SubCategory)










