from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Picture)
admin.site.register(models.Gallery)
admin.site.register(models.Article)
admin.site.register(models.Product)
admin.site.register(models.Slider)
admin.site.register(models.CommentArticle)
admin.site.register(models.CommentProduct)
admin.site.register(models.CommentGallery)
admin.site.register(models.ProductType)
