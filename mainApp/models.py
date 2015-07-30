from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=25)
    def __str__(self):
        return self.user_name
    
class Post(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    text = models.CharField(max_length=200)
    def __str__(self):
        return 'User: %s      Text: %s ' % (str(self.user), self.text)
    
    

