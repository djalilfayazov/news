from django.db.models import *


class Post(Model):
    title = CharField('Post Title', max_length=512)
    image = ImageField('Post Image', upload_to='posts/')

    short = TextField('Short Description')
    full = TextField('Full Description')

    created = DateTimeField('Date & Time', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


