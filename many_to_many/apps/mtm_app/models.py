from __future__ import unicode_literals
import re
from django.db import models

Name_Regex= re.compile (r'^[a-zA-Z]+$')

class UserManager(models.Manager):
    def validateUser(self, name, interest):
        status = True
        if not Name_Regex.match(name): #check for valid name
            status = False
        if not Name_Regex.match(interest): #check for valid interest
            status = False
        if len(name) < 1: #check for name input
            status = False
        if len(interest) < 1: #check for interest input
            status = False
        if User.objects.filter(name = name):
              #if there is a user.....
            # if len(User.objects.filter(name = name).filter(interests = interest)) > 0:
            #     #user already has that interest!!!!!
            #     return False
            q = User.objects.filter(name = name)
            qints = q[0].ints.all()
            for i in qints:
                print i.interest_name
                if interest == i.interest_name:
                    return False # This means you have a duplicate Name and Interest

                else:
                    this_user = User.objects.get(name = name)
                    this_interest = Interests.objects.create(interest_name = interest)
                    this_interest.users.add(this_user)
                    return True
                # get user, create interest, add interest to user
        if status == False:
            return False
        else:
            x = User.objects.create(name = name)
            y = Interests.objects.create(interest_name = interest)
            y.users.add(x)
            print "we created a new user and interest"
            return True
            #create user, get user, create interest, join interest to user


class User(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    objects= UserManager()

class Interests(models.Model):
    interest_name = models.CharField(max_length=45)
    users = models.ManyToManyField(User, related_name="ints")
    created_at = models.DateTimeField(auto_now_add = True)


#
# class User(models.Model):
#     name= models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class Interest(models.Model):
#     interests= models.CharField(max_length=200)
#     users= models.ManyToManyField(User, related_name="interest")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
