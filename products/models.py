from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name='parent', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title',max_length=50)
    description = models.TextField(blank=True)
    avatar= models.ImageField(blank=True,upload_to='categories')
    is_enabled = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
class Product(models.Model):
    parent = models.ForeignKey('self', verbose_name='parent', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=50)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to='products/')
    is_enabled = models.BooleanField(default=True)
    category=models.ManyToManyField('Category', verbose_name='Categories',blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'
class File(models.Model):
    product = models.ForeignKey('product', verbose_name='product', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=50)
    file = models.FileField('file',upload_to='files/%y/%m/%d')
    is_enabled = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = 'file'
        verbose_name_plural = 'files'

# Create your models here.
