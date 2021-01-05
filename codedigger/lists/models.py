from django.db import models
from problem.models import Problem
from user.models import User
from django.template.defaultfilters import slugify
import time

TYPE_CHOICES = (
    ("1" , "List"),
    ("2" , "Ladder"),
    ("3" , "Both"),
)

class List(models.Model):
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    problem = models.ManyToManyField(Problem,through= 'ListInfo',through_fields=('p_list','problem',),related_name='problem')
    name = models.CharField(max_length=100,default=" ")
    description = models.TextField(max_length=400,blank=True,null=True)
    isAdmin = models.BooleanField(default=False)
    isTopicWise = models.BooleanField(default=True)
    type_list = models.CharField(max_length=1,choices=TYPE_CHOICES,default='1')
    slug = models.SlugField(unique=True,max_length=35,blank=True)

    def __str__(self):
        return self.name
    
    def save(self,**kwargs):
        strtime = "".join(str(time.time()).split("."))
        if not self.isAdmin:
            if len(self.name) > 20:
                string = "%s-%s-%s" % (self.name[:20],strtime[12:],self.owner.username[:2] + self.owner.username[-2:])
                self.slug = slugify(string)
                super(List,self).save()
            else:
                string = "%s-%s-%s" % (self.name,strtime[12:],self.owner.username[:2] + self.owner.username[-2:])
                self.slug = slugify(string)
                super(List,self).save()
        else:
            if len(self.name) > 30:
                string = "%s" % (self.name[:30])
                self.slug = slugify(string)
                super(List,self).save()
            else:
                string = "%s" % (self.name)
                self.slug = slugify(string)
                super(List,self).save()



class ListInfo(models.Model):   
    p_list = models.ForeignKey(List,on_delete=models.CASCADE,related_name="curr_list")
    problem = models.ForeignKey(Problem,on_delete = models.CASCADE,related_name='curr_prob')
    description = models.TextField(max_length=400,blank=True,null=True)

    def __str__(self):
        return str(self.p_list) +" " +  str(self.problem)
    
class Solved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user")
    problem = models.ForeignKey(Problem,on_delete = models.CASCADE,related_name='prob')
    def __str__(self):
        return str(self.user.username) + " "  + str(self.problem.name)