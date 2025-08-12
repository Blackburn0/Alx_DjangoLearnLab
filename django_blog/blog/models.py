from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import User

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    published_date = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
    

    