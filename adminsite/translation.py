from modeltranslation.translator import register, TranslationOptions
from website import models


@register(models.SiteSetting)
class SiteSettingTranslationOptions(TranslationOptions):
    fields = ('address', 'small_about', 'full_about')
    required_languages = {'fa': ('address', 'small_about')}


@register(models.Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'subtitle', 'content')
    required_languages = {'fa': ('title', 'slug', 'content')}

