from django_filters import FilterSet
from .models import Post, Category
import datetime

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {

           'title': ['icontains'],
       }

class CategFilter(FilterSet):
   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Category
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {

           'categ_name': ['icontains'],
       }
