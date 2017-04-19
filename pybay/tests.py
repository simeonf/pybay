from django.test import TestCase
from pybay.forms import CallForProposalForm


class CfpFormTestCase(TestCase):
    
    def _get_data(self):
        return {
            'first_name': "Daniel",
            'last_name': "Pyrathon",
            'email': "pirosb3@gmail.com",
            'website': "woo.com",
            'phone': "+14155289519",
            'category': "fundamentals",
            'audience_level': 'beginner',
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
