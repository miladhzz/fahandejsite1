from modeltranslation.translator import register, TranslationOptions
from website import models


@register(models.SiteSetting)
class SiteSettingTranslationOptions(TranslationOptions):
    fields = ('address', 'small_about', 'full_about')
    required_languages = {'fa': ('address', 'small_about')}


@register(models.Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')
    required_languages = {'fa': ('title','content')}


@register(models.Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = {'fa': ('title', 'content')}


@register(models.Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')
    required_languages = {'fa': ('title', 'subtitle')}
