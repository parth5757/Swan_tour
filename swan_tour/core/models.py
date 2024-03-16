from django.db import models
from app.models import BaseModel
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# from .managers import User    
from django.utils.translation import gettext_lazy as _

class State(BaseModel):
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='image/state')

    
    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        ordering = ('created_at',)

class City(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=4, unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/city')


    def code_genrator(self):
        # genrating unique city code
        code = self.name[:3].upper()        

        # check that city code is exist or not
        existing_city = City.objects.filter(code=code).first()

        # check if code is been exist than it will make it 4 characte code
        if existing_city:
            code = self.name[:4].upper()

        # setup genrated code for city
        self.code =code
    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        ordering = ('created_at',)

class Place(BaseModel):
    '''the places this only add by superadmin'''
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/places')

    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        ordering = ('created_at',)


class Contact(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    message = models.TextField(max_length = 1000)


    def __str__(self) -> str:
        return str(self.first_name)
    
    class Meta:
        ordering = ('created_at',)




#we are not using currently an abstract user we use the simple user
# class User(BaseModel, AbstractUser, PermissionsMixin):
#     username = models.CharField(max_length=10, unique=True)
#     email = models.EmailField(_('email address'), unique=True)
#     password = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=10)
#     last_name = models.CharField(max_length=10)
#     is_active = models.BooleanField(("Active Status"), default=True)
#     is_staff = models.BooleanField(("staff status"), defualt=False)