from django.db import models

# Create your models here.
class Tag(models.Model):
    class Meta():
        db_table = 'tag'
    tag_text = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, verbose_name='URL')
    def __str__(self):
        return self.tag_text
    def save(self):
        self.slug = slugify(self.tag_text)
        super(Tag, self).save()

class Article(models.Model):
    class Meta():
        db_table = 'article'
    article_title = models.CharField(max_length = 200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    tag_article = models.ForeignKey(Tag)
    def __str__(self):
        return self.article_title

class Comments(models.Model):
    class Meta():
        db_table = 'comments'
    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article)
    def __str__(self):
        return self.comments_text

