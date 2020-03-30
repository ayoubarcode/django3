from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskQuerySet(models.QuerySet):
    def deletetask(self):
        return self.save(draft=False)
    
    def tasks(self,request):
        user = request.user
        return self.filter(user=request.user, draft=True)


class TaskManager(models.Manager):
    def get_queryset(self):
        return TaskQuerySet(self.model, using=self._db)
    
    def tasks(self,request):
        return self.get_queryset().tasks(request)
    
    def deletetask(self):
        return self.get_queryset().deletetask()



class Task(models.Model):
    user = models.ForeignKey(User, verbose_name=("user_id"), on_delete=models.CASCADE, null=True, blank=True)
    title    = models.CharField(max_length=128)
    complete = models.BooleanField(default=False)
    draft    = models.BooleanField(default=True)
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    objects = TaskManager()

    class Meta:
        ordering  =['created']

    def dont_delete(self):
        self.draft = False
        self.save()


    def __str__(self):
        return self.title
    
    def __len__(self):
        return len(self.title)




SEX = [
    ('H', 'homme'),
    ('f', 'femme'),
]

class Citizen(models.Model):
    name = models.CharField(max_length=128)
    sex = models.CharField(choices=SEX, max_length=128)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'citizens'
    
    




class Category(models.Model):
    name    = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)  

    class Meta:
        ordering = ["created"]
        db_table = "categories"


    def __str__(self):
        return self.name

class Product(models.Model):
    title       = models.CharField(max_length=50)
    price       = models.CharField(max_length=50)
    caetgory_id = models.ManyToManyField(Category)
    created     = models.DateTimeField(auto_now_add=True)

    @property
    def categorie(self):
        return self.caetgory_id.name

    class Meta:
        ordering = ['created']
        db_table = "products"
    
    def __str__(self):
        return self.title

        


# products = Product.objects.all().filter(caetgory_id__name_contains="python")
