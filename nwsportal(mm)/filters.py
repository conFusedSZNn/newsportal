from django_filters import FilterSet
from .models import Post
import datetime

class PostFilter(FilterSet):
   class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
       }
