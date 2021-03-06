from django.db import models

# Create your models here.

class Thread(models.Model):
    """ 
    Contains data about a thread which is a simple unit of a blog
    """
    
    title = models.CharField(max_length = 200) # the title
    author = models.CharField(max_length = 50) # The Author @Shahid : put default as "Robocon IITM"
    timestamp = models.DateTimeField(auto_now = True, null = False) # Autogenerated timestamp
    pic = models.ImageField(upload_to = 'blog', blank=True) # Picture at the heading of a blog. @Shahid put a default image.
    description = models.TextField() # A big description for the blog.

    def __unicode__(self):
        return self.title

