from django_filters import FilterSet
from .models import Post, Category
import datetime


class PostFilter(FilterSet):
   class Meta:
       model = Post
       fields = {

           'title': ['icontains'],
       }

class CategFilter(FilterSet):
   class Meta:
       model = Category
       fields = {

           'categ_name': ['icontains'],
       }
