from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from website import models
from . import forms
from django.contrib.auth import logout


@login_required
def admin_index(request):
    return render(request, 'admin-index.html')


@login_required
def update_settings(request):
    setting = models.SiteSetting.objects.all().first()
    if request.method == 'POST':
        form = forms.SiteSettingsForm(request.POST, instance=setting)
        if form.is_valid():
            setting = form.save()
            setting.save()
    else:
        form = forms.SiteSettingsForm(instance=setting)
    return render(request, 'change-settings.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('website:index')


@login_required
def list_article(request):
    article_list = models.Article.objects.all()
    return render(request, 'list-article.html', {'article_list': article_list})


@login_required
def add_article(request):
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
    else:
        form = forms.ArticleForm()
    return render(request, 'add-article.html', {'form': form})


@login_required
def edit_article(request, pk):
    article = get_object_or_404(models.Article, pk=pk)
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
    else:
        form = forms.ArticleForm(instance=article)
    return render(request, 'edit-article.html', {'form': form})


@login_required
def list_product(request):
    product_list = models.Product.objects.all()
    return render(request, 'list-product.html', {'product_list': product_list})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
    else:
        form = forms.ProductForm()
    return render(request, 'add-product.html', {'form': form})


@login_required
def edit_product(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
    else:
        form = forms.ProductForm(instance=product)
    return render(request, 'edit-product.html', {'form': form})


@login_required
def add_picture(request):
    if request.method == 'POST':
        form = forms.PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.author = request.user
            picture.save()
    else:
        form = forms.PictureForm()
    return render(request, 'add-picture.html', {'form': form})


@login_required
def list_picture(request):
    picture_list = models.Picture.objects.all()
    return render(request, 'list-picture.html', {'picture_list': picture_list})
