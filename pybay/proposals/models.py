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

    MEETUP_CHOICE_YES = 1
    MEETUP_CHOICE_MAYBE =2
    MEETUP_CHOICE_NO = 3

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
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    talk_links = models.CharField(choices=CATEGORY_CHOICES, max_length=200) #Not sure what this refers to.
    what_will_attendees_learn = models.TextField()
    first_name = models.CharField(default= "default_name", max_length=100)
    last_name = models.CharField(default= "default_last_name", max_length=100)
    email = models.CharField(default="default_email@gmail.com", max_length=100)
    website = models.CharField(default= "www.default.com", max_length=100)
    phone = models.CharField(default=9999999999,max_length=20)
    speaker_bio = models.TextField(default= "default speaker bio")
    speaker_and_talk_history = models.TextField(default= "default speaker history")
    meetup_talk = models.CharField(choices=MEETUP_CHOICES, max_length=100, default="No")
    links_to_past_talks = models.TextField(default="N/A", max_length=100)
    audience_level = models.CharField(choices=AUDIENCE_LEVELS, max_length=100)

    class Meta:
        abstract = True


class TalkProposal(Proposal):
    class Meta:
        verbose_name = "talk proposal"


class TutorialProposal(Proposal):
    class Meta:
        verbose_name = "tutorial proposal"
