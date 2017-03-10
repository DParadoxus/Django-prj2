from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from article.models import Article, Comments, Tag

# Create your views here.
def basic_one(request):
    view = "basic_one"
    html = "<html><body>tata %s tata</body></html>" % view
    return HttpResponse(html)

def template_two(request):
    view = "template_two"
    t = get_template('page.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)

def template_three(request):
    view = "template_three"
    return render_to_response('page.html', {'name': view})

def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})

def article(request, article_id):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id), 'comments': Comments.objects.filter(comments_article_id=article_id)})

#def tag(request, slug):
#    return render_to_response('tag_articles.html', {'articles': Article.objects.all(), 'tag': Tag.objects.select_related().get(slug=slug)})