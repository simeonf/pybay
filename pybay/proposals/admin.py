from django.contrib import admin

from .models import TalkProposal, TutorialProposal

class TalkProposalAdmin(admin.ModelAdmin):
    pass

admin.site.register(TalkProposal, TalkProposalAdmin)
admin.site.register(TutorialProposal)
