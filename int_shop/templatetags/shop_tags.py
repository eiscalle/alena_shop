from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag(takes_context=False)
def campaign_compensation(campaign, allocations=None, dealer=None):
   allocation = None
   min_max = None
   if allocations:
       try:
           allocation = filter(lambda x: x.campaign == campaign and dealer in x.dealers.all(), allocations)[0]
       except IndexError:
           pass
   else:
       min_max = campaign.get_min_max_compensation()
    return render_to_string('tags/campaign_compensation.html', {'allocation': allocation, 'min_max': min_max})