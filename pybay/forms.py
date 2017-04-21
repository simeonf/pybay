import random
import string

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from symposion.speakers.models import Speaker
from symposion.proposals.models import ProposalKind
from pybay.proposals.models import TalkProposal


class CallForProposalForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    website = forms.URLField(label='Website', required=False)
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                             error_message=("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    category = forms.ChoiceField(choices=TalkProposal.CATEGORY_CHOICES)
    audience_level = forms.ChoiceField(choices=TalkProposal.AUDIENCE_LEVELS)
    speaker_bio = forms.CharField(widget=forms.Textarea)
    talk_title = forms.CharField(label='Talk Title', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    abstract = forms.CharField(widget=forms.Textarea)
    what_will_attendees_learn = forms.CharField(widget=forms.Textarea)
    speaker_and_talk_history = forms.CharField(widget=forms.Textarea)

    def save_to_models(self):
        if not self.is_valid():
            raise ValidationError("Trying to save a form that is not valid")
        data = self.cleaned_data

        # Fetch the speaker
        full_name = "{} {}".format(data['first_name'], data['last_name'])
        try:
            user = User.objects.get(username=data['email'])
            speaker = user.speaker_profile
        except User.DoesNotExist:

            # Create a new user
            password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            user = User.objects.create_user(
                username=data['email'],
                email=data['email'],
                password=password,
            )

            # Create an associated speaker
            speaker = Speaker.objects.create(
                user=user,
                name=full_name,
                biography=data['speaker_bio'],
                github_account=data['website'],
                phone_number=data['phone'],
            )

        # Create a new talk
        proposal = TalkProposal.objects.create(
            kind=ProposalKind.objects.get(name='talk'),
            title=data['talk_title'],
            description=data['description'],
            abstract=data['abstract'],
            audience_level=data['audience_level'],
            speaker=speaker,
            category=data['category'],
            what_will_attendees_learn=data['what_will_attendees_learn']
        )
        return speaker, proposal
