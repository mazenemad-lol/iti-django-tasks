from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Article
from .forms import ArticleForm


def home(request):
    articles = Article.objects.all()
    form = ArticleForm()
    return render(request, 'app1/home.html', {
        'articles': articles,
        'form': form,
    })


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تمت إضافة المقال بنجاح إلى قاعدة البيانات!')
    return redirect('app1:home')


def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث المقال "{article.title}" بنجاح!')
            return redirect('app1:home')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'app1/edit.html', {
        'form': form,
        'article': article,
    })


def delete_article(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        messages.success(request, f'تم حذف المقال "{article.title}" بنجاح!')
    return redirect('app1:home')
