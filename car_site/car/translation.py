from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('name', 'description')