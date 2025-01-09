from django.db import models
from accounts.models import CustomUser

class Post(models.Model):

    user=models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    content = models.TextField(max_length=200)
    verbose_name = '投稿内容'

    image1=models.ImageField(
        verbose_name='イメージ1',
        blank=True,
        null=True,
        upload_to='Posts',
    )

    image2=models.ImageField(
        verbose_name='イメージ2',
        upload_to='Posts',
        blank=True,
        null=True
    )
    posted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='投稿日時')




