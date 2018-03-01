from django.db import models

from symposion.proposals.models import ProposalBase


class Proposal(ProposalBase):

    AUDIENCE_LEVEL_NOVICE = 1
    AUDIENCE_LEVEL_EXPERIENCED = 2
    AUDIENCE_LEVEL_INTERMEDIATE = 3

    AUDIENCE_LEVELS = [
        (AUDIENCE_LEVEL_NOVICE, "Novice"),
        (AUDIENCE_LEVEL_INTERMEDIATE, "Intermediate"),
        (AUDIENCE_LEVEL_EXPERIENCED, "Experienced"),
    ]

    MEETUP_CHOICE_YES =  "Yes"
    MEETUP_CHOICE_MAYBE = "Maybe"
    MEETUP_CHOICE_NO =  "No"

    MEETUP_CHOICES = [
         (MEETUP_CHOICE_YES, "Yes"),
         (MEETUP_CHOICE_MAYBE, "Maybe"),
         (MEETUP_CHOICE_NO, "No")
    ]

    CATEGORY_CHOICES = [
        "Fundamentals",
        "Language Internals",
        "All things Web",
        "Dealing with Data",
        "Security",
        "Performant Python",
        "Scalable Python",
        "DevOps",
        "/etc"
    ]
    CATEGORY_CHOICES = [
        (c.lower().replace('/', ''), c) for c in CATEGORY_CHOICES
    ]

    audience_level = models.IntegerField(choices=AUDIENCE_LEVELS)

    recording_release = models.BooleanField(
        default=True,
        help_text="By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box."
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    talk_links = models.CharField(max_length=200)
    what_will_attendees_learn = models.TextField()
    meetup_talk = models.CharField(choices=MEETUP_CHOICES, max_length=100, default="No")
    speaker_and_talk_history = models.TextField()
    speaker_website = models.TextField(null=True, blank=True)
    location_override = models.CharField(max_length=200, blank=True)

    class Meta:
        abstract = True


class TalkProposal(Proposal):
    class Meta:
        verbose_name = "talk proposal"


class TutorialProposal(Proposal):
    class Meta:
        verbose_name = "tutorial proposal"

    ticket_price = models.CharField(max_length=50, blank=True)
    sold_out = models.BooleanField(default=False)
