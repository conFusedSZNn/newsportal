from celery import shared_task
from .models import Post, Category
import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

@shared_task
def weekly_sendnews():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(datecr__gte=last_week)
    categories = set(posts.values_list('category__categ_name', flat=True))
    subscribers = set(
        Category.objects.filter(categ_name__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'weekly_sendnews.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
