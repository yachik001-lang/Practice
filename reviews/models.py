from django.db import models

class Review(models.Model):
    full_name = models.CharField("ФИО", max_length=200)
    email = models.EmailField("Email")
    text = models.TextField("Текст отзыва")
    verified = models.BooleanField("Проверено", default=False)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} — {self.created_at.strftime('%Y-%m-%d')}"