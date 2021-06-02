from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.core.fields import RichTextField


@register_setting
class HoursSettings(BaseSetting):

    hours = RichTextField(
        blank=True,
        null=True,
        features=[],
        )
    panels = [
        FieldPanel("hours")
    ]


@register_setting
class ContactSettings(BaseSetting):

    contact = RichTextField(
        blank=True,
        null=True,
        features=['link'],
        )
    panels = [
        FieldPanel("contact")
    ]




@register_setting
class SocialMediaSettings(BaseSetting):

    facebook = models.URLField(
        blank=True,
        help_text='enter your Facebook URL'
    )
    twitter = models.URLField(
        blank=True,
        help_text='enter your Twitter URL'
    )
    instagram = models.URLField(
        blank=True,
        help_text='enter your Instagram URL'
    )

    youtube = models.URLField(
        blank=True,
        help_text='enter your Youtube URL'
    )


    panels = [
        FieldPanel("facebook"),
        FieldPanel("twitter"),
        FieldPanel("instagram"),
        FieldPanel("youtube"),

    ]






