from django.db import models


class Members(models.Model):
    SEX = (
        ('М', 'Муж'),
        ('Ж', 'Жен'),
    )
    name = models.CharField(max_length=50, verbose_name='Фамилия, Имя')
    sex = models.CharField(max_length=10, choices=SEX, verbose_name='Пол')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
        ordering = ['name']


class Rafting_23(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название реки')
    days = models.IntegerField(verbose_name='Количество дней')
    content = models.TextField(verbose_name='Описание сплава')
    km_on_river = models.IntegerField(verbose_name='Километров по реке')
    km_from_perm = models.IntegerField(verbose_name='Километров от Перми')
    images = models.ImageField(upload_to='images/', blank=True)
    LEVEL = (
        ('Лёгкая', 'Лёгкая'),
        ('Средняя', 'Средняя'),
        ('Тяжелая', 'Тяжёлая'),
    )

    level = models.CharField(max_length=30, choices=LEVEL, verbose_name='Сложность')
    members = models.ManyToManyField(Members, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сплав'
        verbose_name_plural = 'Сплавы'
        ordering = ['days', 'title']


class Things(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название вещи')
    individual = models.BooleanField(verbose_name='Индивидуальные')
    common = models.BooleanField(verbose_name='Общие')
    amount = models.IntegerField(verbose_name='Количество', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'
        ordering = ['common']


class Images(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=50, verbose_name='Название')
    rafting = models.ForeignKey(Rafting_23, on_delete=models.CASCADE, verbose_name='id Сплава', related_name='+')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['rafting_id']


class ThingsOfRaftingMembers(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE, verbose_name='id Участника')
    thing = models.ForeignKey(Things, on_delete=models.CASCADE, verbose_name='id Вещи')
