import datetime
from itertools import zip_longest
from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

from ..models import (AddOnBenefitRow, AlaCarteBenefitRow, Benefit, BenefitApplies, ExplanationRow,
                     SponsorCategory, SponsorPackage, SponsorLevel)

register = template.Library()

@register.filter()
def get_all_applies(benefit, levels):
    return benefit.list_all_applies(levels)

@register.simple_tag(takes_context=True)
def load_extra_benefits(context):
    alacarte = AlaCarteBenefitRow.objects.all().order_by('order')
    addon = AddOnBenefitRow.objects.all().order_by('order')
    context['extra_benefits'] = zip_longest(addon, alacarte)
    return ''

@register.simple_tag(takes_context=True)
def load_sponsor_cats_levels_packages(context):
    context['sponsor_cats'] = SponsorCategory.objects.all().order_by('order')
    context['sponsor_packages'] = SponsorPackage.objects.all().order_by('order')
    context['sponsor_levels'] = SponsorLevel.objects.all().order_by('order')
    return ''

@register.simple_tag(takes_context=True)
def load_explanations(context):
    context['explanations'] = ExplanationRow.objects.all().order_by('order')
    return ''

@register.filter
@stringfilter
def checkmark(text):
    checkmark = '<span class="glyphicon glyphicon-ok"></span>'
    output = checkmark if text.lower() == 'yes' else '<span>{}</span>'.format(text)
    return mark_safe(output)

@register.filter
@stringfilter
def comma2br(text):
    output = "<br>".join(text.split(","))
    return mark_safe(output)

@register.filter
@stringfilter
def count_content_lines(text):
    output = [line for line in text.strip().split("\n")[:-1] if line.strip()]
    return len(output)
