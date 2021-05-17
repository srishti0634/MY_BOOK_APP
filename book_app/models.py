from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
# Create your models here.

class custom_user(models.Model):
    userlink=models.OneToOneField(User, on_delete=models.CASCADE)
    firstname=models.CharField('Firstname',max_length=30)
    lastname=models.CharField('Lastname',max_length=30)
    phone=models.CharField('Phone No.',max_length=15,unique=True)
    email=models.EmailField('Email',max_length=100,unique=True)
    username=models.CharField('Username',max_length=30, unique=True)
    user_pin=models.CharField('Pincode', max_length=6, validators=[MinLengthValidator(6)])

    def __str__(self):
        return self.firstname+" "+self.lastname

class Sell(models.Model):
    # CHANGE
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    book_name=models.CharField('Book Name',max_length=200, help_text="Enter the book name")
    author=models.CharField('Author',max_length=200, help_text="Enter the book's author name")
    published_by=models.CharField('Published By',max_length=200)
    FIRSTHAND='Firsthand'
    SECONDHAND='Secondhand'
    TYPE_CHOICES=[
        ('Firsthand','Firsthand'),
        ('Secondhand','Secondhand'),
    ]
    TAG_CHOICES=[
        ('ACTION','Action'),
        ('THRILLER','Thriller'),
        ('ART','Art'),
        ('ROMANCE','Romance'),
        ('FAIRYTALE','Fairytale'),
        ('TRUE CRIME','True_crime'),
        ('DRAMA','Drama'),
        ('DIARY','Diary'),
        ('COMIC','Comic'),
        ('HISTORY','History'),
        ('HORROR','Horror')
    ]
    DIS_CHOICES=[
        ('40%','40%'),
        ('50%','50%'),
        ('60%','60%'),
        ('70%','70%'),
        ('80%','80%'),
        ('90%','90%'),
        ('100%','100%')
    ]
    tags=models.CharField('Tag',max_length=20, choices=TAG_CHOICES)
    types=models.CharField('Type',max_length=30, choices=TYPE_CHOICES, default=SECONDHAND)
    price=models.DecimalField('Price',max_digits=10, decimal_places=2, help_text="Enter the book's price")
    discount=models.CharField('Discount',max_length=20, choices=DIS_CHOICES, default='40%')
    pin_code=models.CharField('Pincode', max_length=6, validators=[MinLengthValidator(6)], help_text="Enter the pincode of your suitable area to sell")
    description=models.TextField('Description',max_length=300, help_text="Please add if any extra info is there for the book", null=True)
    photo = models.ImageField('Photo Of Book',upload_to='photos/',blank=True,null=True)

    def __str__(self):
        return self.book_name+"-"+self.author

class Cart(models.Model):
    seller=models.ForeignKey(Sell, on_delete=models.CASCADE)
