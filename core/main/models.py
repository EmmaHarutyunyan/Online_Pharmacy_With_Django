from django.db import models

# Create your models here.

class Slide(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
class Home_products(models.Model):

    pr_name=models.CharField(max_length=100)
    pr_img=models.ImageField(upload_to='images/')
    pr_price=models.PositiveIntegerField()

    class Meta:
        verbose_name='Home product'
        verbose_name_plural='Home products'

    def __str__(self):
        return self.pr_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity_available = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class About(models.Model):
    about_title1=models.CharField(max_length=50)
    about_title2=models.CharField(max_length=50)
    about_img=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.about_title1

class ContactUs(models.Model):

    fname = models.CharField('Contact first name', max_length=60)
    lname = models.CharField('Contact last name', max_length=60)
    email = models.EmailField('Contact email')
    message = models.TextField('Contact text')


    class Meta:
        verbose_name='Contact Us'
        verbose_name_plural='Contact Us'

    def __str__(self):
        return self.fname
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price

    def total_price_sale(self):
        return self.quantity * self.product.sale_price if self.product.on_sale else self.total_price()

    