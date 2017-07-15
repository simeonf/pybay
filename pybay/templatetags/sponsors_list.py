from django import template

from symposion.sponsorship.models import Sponsor

register = template.Library()


@register.inclusion_tag('frontend/sponsors_footer.html', takes_context=True)
def sponsors_footer(context):
    sponsors = Sponsor.objects.filter(active=True)
    return {
        'sponsors': sponsors,
    }
