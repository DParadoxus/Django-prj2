from django.contrib import admin
from article.models import Article, Comments, Tag

# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date', 'tag_article']
    inlines = [ArticleInline]
    list_filter = ['article_date']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)