from django.contrib import admin

from .models import TalkProposal, TutorialProposal

class TalkProposalAdmin(admin.ModelAdmin):
    exclude = ('additional_notes', 'additional_notes_html', 'abstract_html')

admin.site.register(TalkProposal, TalkProposalAdmin)
admin.site.register(TutorialProposal)
