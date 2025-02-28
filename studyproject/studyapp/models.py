from django.db import models

class StudyPost(models.Model):

    CATEGORY=(
        ('Python','Pythonの勉強'),
        ('Django','Djangoの勉強'),
        ('HTML/CSS','HTML/CSSの勉強'),
        ('JavaScript','JavaScriptの勉強'),
        ('その他','その他の勉強')
    )
    title = models.CharField(
        verbose_name='タイトル',
        max_length=100
        )
    comment = models.TextField(
        verbose_name='コメント',
        blank=True,#空白を許可
        null=True#nullを許可
        )
    posted_at= models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
        )
    category = models.CharField(
        verbose_name='カテゴリ',
        max_length=50,
        choices=CATEGORY
    )

    def __str__(self):
        return self.title
