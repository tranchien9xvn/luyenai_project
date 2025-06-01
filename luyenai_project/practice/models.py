from django.db import models

class Week(models.Model):
    number = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=100)  # ví dụ "Tuần 3"

    def __str__(self):
        return f"Tuần {self.number}: {self.title}"

class Exercise(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # ví dụ "Luyện tập viết prompt"

    def __str__(self):
        return f"{self.title} ({self.week})"

class Question(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Câu hỏi: {self.text[:50]}"
