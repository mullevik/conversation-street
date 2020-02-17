import uuid

from django.db import models
from django.conf import settings


class Profile(models.Model):
    """A custom extension of the default User model containing
    additional information about users"""
    display_name = models.CharField(max_length=50)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)


class Category(models.Model):
    """A category for questions"""
    identifier = models.UUIDField(null=False,
                                  default=uuid.uuid4,
                                  editable=False,
                                  unique=True)
    name = models.CharField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    """A tag for questions"""
    identifier = models.UUIDField(null=False,
                                  default=uuid.uuid4,
                                  editable=False,
                                  unique=True)
    name = models.CharField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    """A representation of a user liking a question"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    """A conversation question
    One question must have one author, (can have) one category,
    must have 0 to N tags and must have 0 to N likes"""
    identifier = models.UUIDField(null=False,
                                  default=uuid.uuid4,
                                  editable=False,
                                  unique=True)
    text = models.CharField(max_length=500)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(Like)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True)


class Comment(models.Model):
    """A comment under a question. Comments support forum-tree hierarchy"""
    text = models.TextField(max_length=2000)
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE)
    parent_comment = models.ForeignKey("self",
                                       on_delete=models.CASCADE,
                                       null=True,
                                       blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True)

