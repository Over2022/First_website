# from django.db import models
#
#
# class Task(models.Model):
#     title = models.CharField('Название', max_length=50)
#     task = models.TextField('Описание')
#
#     def __str__(self):
#         return self.title
#
#
# class Main(models.Model):
#     title = models.CharField('Заголовок', max_length=55)
#     main = models.TextField('Основное')
#     img = models.FileField(upload_to='img/')
#     data = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.main, self.img
