from django.test import TestCase
from pybay.forms import CallForProposalForm

from symposion.proposals.models import ProposalKind


class CfpFormTestCase(TestCase):
    fixtures=[
        "conference",
        "proposal_base",
        # "sites",
        # "sponsor_benefits",
        # "sponsor_levels",
    ]
    
    def _get_data(self):
        return {
            'first_name': "Daniel",
            'last_name': "Pyrathon",
            'email': "pirosb3@gmail.com",
            'website': "woo.com",
            'phone': "+14155289519",
            'category': "fundamentals",
            'audience_level': 1,
            'speaker_bio': 'wooo',
            'talk_title': 'wooo',
            'description': 'wooo',
            'abstract': 'wooo',
            'what_will_attendees_learn': 'wooo',
            'speaker_and_talk_history': 'wooo',
        }

    def test_cfp_form_works(self):
        form = CallForProposalForm(self._get_data())
        self.assertTrue(form.is_valid())
        self.assertEqual(
            len(form.cleaned_data), 13
        )

    def test_cannot_ommit_fields(self):
        all_fields = set(self._get_data().keys())
        all_fields.remove('website')

        for field_name in all_fields:
            data = self._get_data()
            del data[field_name]

            form = CallForProposalForm(data)
            self.assertFalse(form.is_valid())
            self.assertIn(field_name, form.errors)

    def test_form_save_models(self):
        form = CallForProposalForm(self._get_data())
        self.assertTrue(form.is_valid())

        speaker, proposal = form.save_to_models()
        self.assertEqual(speaker.name, "Daniel Pyrathon")
