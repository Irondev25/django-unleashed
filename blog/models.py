from django.db import models
from django.core.urlresolvers import reverse
from organizer.models import Tag, Startup

# Create your models here.

# each field provides
# 1. How the date is stored in the database
# 2. Which python data type will it be manupulated in
# 3. How to validate each field
# 4. How to diaplay data in certain context such as form

# Migration is version control of database (it put simply)

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63, unique_for_month='pub_date', help_text='A label for URL config.')
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True) 
    tags = models.ManyToManyField(Tag, related_name='blog_posts', blank=True)
    startups = models.ManyToManyField(Startup, related_name='blog_posts', blank=True)

    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'


    def __str__(self):
        return "{} on {}".format(self.title, self.pub_date.strftime('%d-%m-%Y'))
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={
            'year':self.pub_date.year,
            'month':self.pub_date.month,
            'slug':self.slug
        })
    
    def get_update_url(self):
        return reverse('blog:post_update', kwargs={
            'year': self.pub_date.year,
            'month': self.pub_date.month,
            'slug': self.slug
        })

    def get_delete_url(self):
        return reverse('blog:post_delete', kwargs={
            'year': self.pub_date.year,
            'month': self.pub_date.month,
            'slug': self.slug
        })
