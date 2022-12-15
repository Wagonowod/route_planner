from django.db import models
from django.urls import reverse


class Rafting(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название реки')
    days = models.IntegerField(verbose_name='Количество дней')
    content = models.TextField(verbose_name='Описание сплава')
    short_content = models.TextField(verbose_name='Краткое описание сплава', null=True)
    km_on_river = models.IntegerField(verbose_name='Километров по реке')
    km_from_perm = models.CharField(max_length=50, verbose_name='Километров от Перми')
    title_image = models.ImageField(upload_to='images/title/', blank=True, verbose_name='Главное фото')
    preview_image = models.ImageField(upload_to='images/preview/', blank=True, verbose_name='Превью')
    LEVEL = (
        ('Лёгкая', 'Лёгкая'),
        ('Средняя', 'Средняя'),
        ('Тяжелая', 'Тяжёлая'),
    )

    level = models.CharField(max_length=30, choices=LEVEL, verbose_name='Сложность')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    members = models.ManyToManyField('Members')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('rafting', kwargs={'rafting_slug': self.slug})

    class Meta:
        verbose_name = 'Сплав'
        verbose_name_plural = 'Сплавы'
        ordering = ['days', 'title']


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


class Things(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название вещи')
    individual = models.BooleanField(verbose_name='Индивидуальные')
    amount = models.IntegerField(verbose_name='Количество', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'
        ordering = ['individual']


class Images(models.Model):
    image = models.ImageField(upload_to='images/basic', blank=True)
    title = models.CharField(max_length=50, verbose_name='Название')
    rafting = models.ForeignKey(Rafting, on_delete=models.CASCADE, verbose_name='id Сплава', related_name='images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['rafting_id']


class Timings(models.Model):
    time = models.CharField(max_length=30, verbose_name='Время')
    action = models.TextField(verbose_name='Действие')
    DAY = (
        ('1', 'День 1'),
        ('2', 'День 2'),
        ('3', 'День 3'),
        ('4', 'День 4'),
        ('5', 'День 5'),
    )
    day = models.CharField(max_length=10, choices=DAY, verbose_name='День', null=True)
    rafting = models.ForeignKey(Rafting, on_delete=models.CASCADE, verbose_name='id сплава')
    order = models.IntegerField(verbose_name='Порядок', null=True)

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Тайминг'
        verbose_name_plural = 'Тайминги'
        ordering = ['time']


class ThingsOnRaftings(models.Model):
    rafting_id = models.ForeignKey(Rafting, on_delete=models.CASCADE)
    thing_id = models.ForeignKey(Things, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Members, on_delete=models.CASCADE, null=True)
    is_checked = models.BooleanField()

    class Meta:
        verbose_name = 'Вещь на сплаве'
        verbose_name_plural = 'Вещи на сплаве'
