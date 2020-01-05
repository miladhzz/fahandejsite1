from django.db import models
from django.contrib.auth.models import User


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
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    main_picture = models.ImageField(upload_to='images/post', default='images/no-img-post.jpg', blank=True, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title


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
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    main_picture = models.ImageField(upload_to='images/product', default='images/no-img-product.jpg')
    pictures = models.ManyToManyField(Picture)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    product_type = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


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
    post = models.ForeignKey(Article, on_delete=models.CASCADE)

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
