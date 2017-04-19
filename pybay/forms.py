from django import forms

CATEGORY_CHOICES = [
    "Fundamentals",
    "Language Internals",
    "All things Web",
    "Dealing with Data",
    "Security",
    "Performant Python",
    "Scalable Python",
    "/etc"
]
CATEGORY_CHOICES = [
    (c.lower().replace('/', ''), c) for c in CATEGORY_CHOICES
]

AUDIENCE_LEVEL_CHOICES = [
    "Beginner",
    "Intermediate",
    "Advanced",
]
AUDIENCE_LEVEL_CHOICES = [
    (c.lower().replace('/', ''), c) for c in AUDIENCE_LEVEL_CHOICES
]


class CallForProposalForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    website = forms.URLField(label='Website', required=False)
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                             error_message=("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    audience_level = forms.ChoiceField(choices=AUDIENCE_LEVEL_CHOICES)
    speaker_bio = forms.CharField(widget=forms.Textarea)
    talk_title = forms.CharField(label='First Name', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    abstract = forms.CharField(widget=forms.Textarea)
    what_will_attendees_learn = forms.CharField(widget=forms.Textarea)
    speaker_and_talk_history = forms.CharField(widget=forms.Textarea)
