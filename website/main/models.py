from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title
    #
    # class Meta:
    #     verbose_name='Задача'
    #     verbose_name_plural='Задачи'


class Main(models.Model):
    title = models.CharField('Заголовок', max_length=55)
    main = models.TextField('Основное')
    img = models.FileField(upload_to='img/')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Registration(models.Model):
    name = models.CharField('Имя', max_length=10)
    surname = models.CharField('Фамилия', max_length=10)
    mail = models.CharField('E-mail', max_length=20)
    password = models.CharField('Пароль', max_length=20)
    password_2 = models.CharField('Пароль', max_length=20)
