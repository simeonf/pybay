from django.contrib import admin

from .models import TalkProposal, TutorialProposal


class TalkProposalAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'status')


admin.site.register(TalkProposal, TalkProposalAdmin)
admin.site.register(TutorialProposal)
