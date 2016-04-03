from __future__ import unicode_literals

from django.db import models

from django.contrib import admin
from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

#customize user table add feild,so make new table with relations
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image=models.ImageField(upload_to='images/user', blank=True)

class  Article(models.Model):
	subject=models.CharField(max_length=150)
	description=models.TextField()
	image=models.ImageField(upload_to='images/article', blank=True)
	date=models.DateTimeField(default=datetime.now())
	is_publish=models.BooleanField()
	is_denied=models.BooleanField()
	user_id= models.ForeignKey(User,on_delete=models.CASCADE)
	# class Meta:		
	# 		permissions = (("is_mark", "mark"),)

		

class Comment(models.Model):
	content=models.CharField(max_length=500)
	date=models.DateTimeField(default=datetime.now())
	Article_comment_id= models.ForeignKey(Article,on_delete=models.CASCADE)
	reply= models.ForeignKey("self")

class Tag(models.Model):
	word=models.CharField(max_length=50)
	Article_Tag_id= models.ForeignKey(Article,on_delete=models.CASCADE)

class like(models.Model):
	User_like_id= models.ForeignKey(User,on_delete=models.CASCADE)
	Comment_like_id=models.ForeignKey(Comment,on_delete=models.CASCADE)

class mark(models.Model):
	User_mark_id= models.ForeignKey(User,on_delete=models.CASCADE)
	Article_mark_id=models.ForeignKey(Comment,on_delete=models.CASCADE)
		
class emotion(models.Model):
	photo=models.CharField(max_length=100)
	Comment_emotion_id= models.ForeignKey(Comment,on_delete=models.CASCADE)

class banWords(models.Model):
	word=models.CharField(max_length=100)
	
#admin.site.register(UserProfile)
#admin.site.register(Article)
#admin.site.register(Comment)
#admin.site.register(Tag)
#admin.site.register(emotion)
#admin.site.register(banWords)
