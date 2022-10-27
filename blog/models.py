from django.conf import settings
from django.db import models
from django.utils import timezone
# Post= name, It can be changeable. 
# Always start a class name with an uppercase letter.
# class= defining(tanımlamak) an object
# models.Model means that the post is a django model
# so django knows that it should be saved in database. 
# More info = https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types
class Post(models.Model):
    # this is a link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # this is how you define text with a limited number of characters
    title = models.CharField(max_length=200)
    # this is for long text without a limit
    # sound ideal for blog post content.
    text = models.TextField()
    # this is a date and time
    created_date = models.DateTimeField(default=timezone.now)
    # null = if true, django will store empty values as NULL in the database.
    # avoid using null on string-based fields such as CharField and TextField.
    # blank = if true, the field is allowed to be blank(boşluk).
    published_date = models.DateTimeField(blank=True, null=True)
    # Publish function (publish name changeable(I think function name changeable))
    # Tha naming rule is that we use lowercase and underscores instead of spaces 
    # (example = calculate_average_price)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # Use "dunder" for str. It's mean double-underscore.
    # When we call str, we will get a text(string) with a Post title.
    # Also notice that both def publish and def str, are indented inside our class.
    # Because python is sensitive to whitespace, we need to indent our methods inside the class.
    def __str__(self): # Don't forget colon
        return self.title




