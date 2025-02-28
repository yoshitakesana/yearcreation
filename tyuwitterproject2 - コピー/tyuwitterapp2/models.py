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


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'  # 逆参照時に `post.comments` で取得できる
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}"  # 先頭20文字のみ表示


