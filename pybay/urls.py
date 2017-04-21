from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

import symposion.views
from symposion.teams import urls as teams_urls
from symposion.proposals import urls as proposals_urls
from symposion.sponsorship import urls as sponsor_urls
from symposion.speakers import urls as speaker_urls

from pybay.views import pybay_cfp_create


WIKI_SLUG = r"(([\w-]{2,})(/[\w-]{2,})*)"


urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="frontend/index.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),

    # url(r"^teams/", include(teams_urls)),
    # url(r"^proposals/", include(proposals_urls)),
    # url(r"^account/signup/$", SignupView.as_view(), name="account_signup"),
    # url(r"^account/login/$", symposion.views.LoginView.as_view(), name="account_login"),
    url(r"^account/", include("account.urls")),

    # url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),
    # url(r"^speaker/", include(speaker_urls)),
    # url(r"^sponsors/", include("symposion.sponsorship.urls")),
    # url(r"^boxes/", include("pinax.boxes.urls")),
    # url(r"^teams/", include("symposion.teams.urls")),
    # url(r"^reviews/", include("symposion.reviews.urls")),
    # url(r"^schedule/", include("symposion.schedule.urls")),
    # url(r"^markitup/", include("markitup.urls")),

    # url(r"^markitup/", include("markitup.urls")),


    url(r"^sponsors$", TemplateView.as_view(template_name="frontend/sponsors.html"), name="pybay_sponsors"),
    url(r"^cfp$", pybay_cfp_create, name="pybay_cfp"),
    # url(r"^", include("symposion.cms.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
