from django.contrib import admin

from .models import TalkProposal, TutorialProposal

class TalkProposalAdmin(admin.ModelAdmin):
    exclude = ('additional_notes', 'additional_notes_html', 'abstract_html')
    fields = (
        'first_name',
        'last_name',
        'email',
        'website',
        'phone',
        'category',
        'meetup_talk',
        'audience_level',
        'speaker_bio',
        'title',
        'description',
        'abstract',
        'what_will_attendees_learn',
        'speaker_and_talk_history',
        'links_to_past_talks',
    )

admin.site.register(TalkProposal, TalkProposalAdmin)
admin.site.register(TutorialProposal)
