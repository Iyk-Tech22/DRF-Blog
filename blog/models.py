from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    """ Define category model """
    name = models.CharField(max_length=150)
    
    def __str__(self):
        """ String reprs of the obj """
        return f"{self.name}"
        
class Post(models.Model):
    """ Post model """
    options = (
        ("draft", "Draft"),
        ("published", "Published")
    )
    
    title = models.CharField(max_length=150)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="published")
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default="Published")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    
    # CUSTOM MODEL MANAGER
    class PostObjects(models.Manager):
        """ Post Model Manager """
        def get_queryset(self):
            return super().get_queryset().filter(status="published")
            
    
    # MANAGERS
    objects = models.Manager()
    post_objects = PostObjects()
    
    # MODEL META DATA
    class Meta:
        ordering = ("-published",)
        
    def __str__(self):
        return f"{self.title}"
    
      
    
    