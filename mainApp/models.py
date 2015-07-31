from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=25)
    def __str__(self):
        return self.user_name

class Category(models.Model):
    text = models.CharField(max_length = 25)
    def __str__(self):
        return self.text

class Post(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    date = models.DateField()
    text = models.CharField(max_length=200)
    def __str__(self):
        return 'User: %s      Text: %s ' % (str(self.user), self.text)
    

        

