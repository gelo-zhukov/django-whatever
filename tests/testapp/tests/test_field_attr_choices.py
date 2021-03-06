"""
https://docs.djangoproject.com/en/1.3/ref/models/fields/#choices
"""
from django.db import models
from django.test import TestCase

from django_any.models import any_field


class AttrChoices(TestCase):
    def test_one_case_selection(self):
        """
        Even there is only one choice, it should be returned always
        """
        field = models.BooleanField(choices=[
            (False, 'This sentence is wrong')])

        result = any_field(field)

        self.assertEqual(bool, type(result))
        self.assertEqual(False, result)

    def test_choices_named_groups_support(self):
        """
        Group names completely ignored
        """
        MEDIA_CHOICES = (
            ('Audio', (('vinyl', 'Vinyl'), ('cd', 'CD'))),
            ('Video', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))),
            ('unknown', 'Unknown'))
        media = models.CharField(max_length=25, choices=MEDIA_CHOICES)

        result = any_field(media)

        self.assertTrue(result in ['vinyl', 'cd', 'vhs', 'dvd', 'unknown'])
