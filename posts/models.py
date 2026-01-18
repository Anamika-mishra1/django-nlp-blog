from django.db import models

# Create your models here.
from textblob import TextBlob

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    sentiment = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        blob = TextBlob(self.content)
        self.sentiment = blob.sentiment.polarity
        super().save(*args, **kwargs)
    
    def get_sentiment_label(self):
        if self.sentiment > 0.1:
            return "Positive 😊"
        elif self.sentiment < -0.1:
            return "Negative 😞"
        return "Neutral 😐"
    
    def __str__(self):
        return self.title
