from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100, verbose_name="待辦事項")
    description = models.TextField(blank=True, null=True, verbose_name="內容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新時間")

    def __str__(self) -> str:
        return self.title
