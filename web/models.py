from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 50, verbose_name="상품명")
    price = models.IntegerField(verbose_name = "상품가격")
    inven = models.IntegerField(verbose_name="상품재고")
    descrip = models.TextField(verbose_name="상품설명")
    reg_date = models.DateTimeField(verbose_name="등록날짜", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "shop"
        verbose_name = "상품"
        verbose_name_plural = "상품"