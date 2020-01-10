from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class BaseContent(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(BaseContent):
    slug = models.SlugField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    main_picture = models.ImageField(upload_to='images/post', default='images/no-img-post.jpg', blank=True, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[self.slug])


class Slider(BaseContent):
    url = models.URLField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ImageField(upload_to='images/slider', default='images/no-img-slider.jpg')

    def __str__(self):
        return self.title


class Picture(models.Model):
    picture = models.ImageField(upload_to='images/picture', default='images/no-img-picture.jpg')
    create_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Gallery(BaseContent):
    pictures = models.ManyToManyField(Picture)
    description = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class ProductType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.name


class Product(BaseContent):
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    main_picture = models.ImageField(upload_to='images/product', default='images/no-img-product.jpg')
    pictures = models.ManyToManyField(Picture, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    product_type = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])


class BaseComment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=11, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    comment = models.TextField()

    class Meta:
        abstract = True


class CommentArticle(BaseComment):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class CommentProduct(BaseComment):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class CommentGallery(BaseComment):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class SiteSetting(models.Model):
    address = models.TextField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    small_about = models.CharField(max_length=150, blank=True, null=True)
    full_about = models.TextField(blank=True, null=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Contact(BaseComment):
    comment = None
    active = None
    message = models.TextField()

    def __str__(self):
        return self.message
