from django.db import models

# Create your models here.
class Category(models.Model):
    category_title = models.CharField(max_length=200)
    def __str__(self):
        return "{}".format(self.category_title)
class Post(models.Model):
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body  = models.TextField()
    tag   = models.CharField(max_length=30)
    publish_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{}".format(self.title)