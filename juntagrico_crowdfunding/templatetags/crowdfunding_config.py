from django import template
from juntagrico_crowdfunding.config import CrowdfundingConfig

register = template.Library()


@register.simple_tag
def vocabulary(key):
    return CrowdfundingConfig.vocabulary(key)
