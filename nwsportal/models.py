from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

class AuthorUser(models.Model):
    rate_au = models.FloatField(default = 0.00)
    session_client = models.OneToOneField(User, on_delete= models.CASCADE)
    userAs = models.CharField(max_length=50, default = '')
    def update_rating(self):
        sum_rating_author = self.post_set.all().aggregate(Sum(' rating_post'))['rating_post__sum']*3
        sum_rating_comm = self.author_user.comment_set.all().aggregate(Sum('rating_comment'))['rating_comment__sum']
        sum_rate = self.post_set.all().aggregate(Sum('comment__rating_comment'))['comment__rating_comment__sum']
        self.rate_auth = sum_rating_author + sum_rating_comm + sum_rate
        self.save()





class Category(models.Model):
    categ_name = models.CharField(max_length=255, unique = True, default = 'Неизвестная категория')
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return f'{self.categ_name}'

class Post(models.Model):
    one_to_many_post = models.ForeignKey('AuthorUser', on_delete = models.PROTECT)
    type_news = 'NW'
    type_article = 'AR'
    POST_TYPE = [
        (type_news, 'Новость'),
        (type_article, 'Статья'),
    ]
    post_type = models.CharField(max_length=2, choices=POST_TYPE, default = 1)
    datecr = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', through = 'PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=5000, default = '')
    rating_post = models.FloatField(default = 0.00)
    def likepost(self):
        self.rate_post += 1
        self.save()

    def dislikepost(self):
        self.rate_post -= 1
        self.save()

    def preview(self):
        return self.text[:125] + ". . ."

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]} ' \
               f' Дата публикации: {self.datecr}'
    def get_absolute_url(self):
        return reverse('post_details', args=[str(self.id)])




class PostCategory(models.Model):
    one_to_many_postcatpst = models.ForeignKey('Post', on_delete = models.CASCADE)
    one_to_many_postcatct = models.ForeignKey('Category', on_delete = models.CASCADE)

class Comment(models.Model):
    one_to_many_commpost = models.ForeignKey('Post', on_delete = models.CASCADE)
    one_to_many_commau = models.ForeignKey('AuthorUser', on_delete = models.PROTECT)
    textcomm = models.TextField(max_length = 500)
    datecomm = models.DateField(auto_now_add=True)
    rating_comment =  models.FloatField(default = 0.00)
    def likecomm(self):
        self.ratecomm += 1
        self.save()
    def dislikecomm(self):
        self.ratecomm -= 1
        self.save()


