"""juntagrico_crowdfunding URL Configuration
"""
from django.conf.urls import url
from juntagrico_crowdfunding import views as crowdfunding

urlpatterns = [
    url(r'^cf/?$', crowdfunding.list_funding_projects),
    url(r'^cf/list/(?P<funding_project_id>.*?)/$', crowdfunding.list_fundables),
    url(r'^cf/view/(?P<fundable_id>.*?)/', crowdfunding.view_fundable),
    url(r'^cf/fund/(?P<fundable_id>.*?)/', crowdfunding.fund),
    url(r'^cf/confirm', crowdfunding.confirm),
    url(r'^cf/edit/order', crowdfunding.edit_order),
    url(r'^cf/edit/funder', crowdfunding.edit_funder),
    url(r'^cf/thanks/(?P<funding_project_id>.*?)$', crowdfunding.thanks),
    url(r'^cf/contribution', crowdfunding.contribution),
]
