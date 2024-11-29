
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    following = models.ManyToManyField(#ユーザーのフォロー関係
        'self',
        symmetrical=False,#一方的な関係を表現
        related_name='followers',#逆参照
        verbose_name='フォロー中'#フィールド名
    )
    name = models.CharField(
        max_length=30,#最大文字数
        verbose_name='名前'#フィールド名
    )
    email = models.EmailField(
        unique=True,  # 同じメールアドレスはだめ※一意制約
        verbose_name='メールアドレス'
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,  # フォームでの入力が必須ではない
        null=True,  # データベースでNULL値を許可
        verbose_name='電話番号'
    )

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,#オブジェクトが消された時＝関連するものまで消す
        related_name='posts',
        verbose_name='ユーザー'
    )
    content = models.TextField(
        max_length=280,
        verbose_name='内容'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='作成日時'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='更新日時'
    )
    def __str__(self):
        return f'{self.user.username}: {self.content[:20]} (作成日時: {self.created_at}, 更新日時: {self.updated_at})'



class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='ユーザー'
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='投稿'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='作成日時'
    )
    def __str__(self):
        return f'{self.user.username} likes {self.post.content[:20]}'

