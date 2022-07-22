from django.db import models
from datetime import datetime
from accounts.models import Person

# Create your models here.

# creons une classe de discussion parce que les discussions seront regroupées par thème
"""
class discussionTheme(models.Model):
    name_theme = models.CharField(max_length=2000)
    date_creation=models.DateTimeField(default=datetime.now)
    id_user_create= models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"{self.name_theme}"
 """   
# créons une classe message qui contient tous les messages de notre système de discussion
class Messages(models.Model):
    content_message =  models.TextField(max_length=220000)
    date_message=models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    #id_theme = models.ForeignKey(discussionTheme, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.date_message} {self.content_message}"

class Videos_shared(models.Model):
    content_video =  models.FileField()
    user = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    #id_theme = models.ForeignKey(discussionTheme, on_delete=models.DO_NOTHING)

class Images_shared(models.Model):
    content_image =  models.FileField()
    user = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    #id_theme = models.ForeignKey(discussionTheme, on_delete=models.DO_NOTHING)



    
    

