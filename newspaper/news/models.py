from os import R_OK
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models import DateTimeField
from django.db.models import Sum 

# Create your models here.


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def updateRating(self):
        postRat = self.post_set.all().aggregate(postrating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commemtRat = self.authorUser.comment_set_all().aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commemtRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOISES = (
        (NEWS, 'новость'),
        (ARTICLE, 'статья'),
    )
    categorType = models.CharField(max_length=2, choices=CATEGORY_CHOISES, default=ARTICLE)
    dateCreation = DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='postCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()
    
    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        try:
            return self.commentPost.author.authorUser.username
        except: 
            return self.commentUser.username
    
    def like(self):
        self.rating += 1
        self.save()
    
    def dislike(self):
        self.rating -= 1
        self.save()