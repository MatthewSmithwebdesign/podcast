from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList


from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.contrib.table_block.blocks import TableBlock

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        requried=True,
        help_text='Text to display',
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Center text to display"


class LinkValue(blocks.StructValue):
    """ Logic for links"""
    def url(self) -> str:
        internal_page = self.get("internal_page")
        external_link = self.get("external_link")
        if internal_page:
            return internal_page.url
        elif external_link:
            return external_link
        return ""

class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(
        max_length=50,
        default='More Details'
    )
    internal_page = blocks.PageChooserBlock(
        required=False
    )
    external_link = blocks.URLBlock(
        required=False
    )

    class Meta:
        value_class = LinkValue

    def clean(self, value):
        internal_page = value.get("internal_page")
        external_link = value.get("external_link")
        errors = {}
        if internal_page and external_link:
            errors["internal_page"] = ErrorList(["Both of these fields cannot be filled. Please select or enter only one option."])
            errors["external_link"] = ErrorList(["Both of these fields cannot be filled. Please select or enter only one option."])
        elif not internal_page and not external_link:
            errors["internal_page"] = ErrorList(["Please select a page or enter a URL for one of these options."])
            errors["external_link"] = ErrorList(["Please select a page or enter a URL for one of these options."])

        if errors:
            raise ValidationError("Validation error in your Link", params=errors)

        return super().clean(value)

class Card(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100,
        help_text="Bold text for this card max length of 100 characters.",
        required=False

    )
    image= ImageChooserBlock(
        help_text="Image will be auto cropped to 570px by 370px."

    )
    link = Link(help_text="Enter a link or select a page")


class CardsBlock(blocks.StructBlock):

    cards= blocks.ListBlock(
        Card()
    )
    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard Cards"

class RadioSelectBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.widget =forms.RadioSelect(
            choices=self.field.widget.choices
        )


class ImageAndTextBlock(blocks.StructBlock):

    image = ImageChooserBlock (help_text='will be cropped to 786x562px')
    image_alignment = RadioSelectBlock(
        choices=(
            ("left", "Image to the left"),
            ("right", "Image to the right")
        ),
        default='left',
        help_text='Image on the left with text on the right or Image on the right and text on the left'
    )
    title = blocks.CharBlock(max_length=60, help_text=' max length is 60 characters')
    text = blocks.CharBlock(max_length=140, required=False)
    link = Link()

    class Meta:
      template = "streams/image_and_text_block.html"
      icon = "image"
      label = "Image & Text"

class CallToActionBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=200, help_text='max length is 200 characters')
    link = Link()

    class Meta:
        template ="streams/call_to_action_block.html"
        icon = "plus"
        label = "Call to Action"

    # youtube embed stream field
class YouTubeEmbedBlock(blocks.StructBlock):
    youtube_id = blocks.CharBlock(max_length=30,help_text= 'youtube id here',  required=True)
    class Meta:
        template = "streams/youtube.html"
        icon = "media"
        label = "YouTube"

class SpotifyEmbedBlock(blocks.StructBlock):
    artist_id = blocks.CharBlock(max_length=30,help_text= ' enter the artist id for spotify', required=True)

    class Meta:
        template = "streams/spotify.html"
        icon = "pilcrow"
        label = "Spotify"


class PodcastEmbedBlock(blocks.StructBlock):
    artist_id = blocks.CharBlock(max_length=30,help_text= ' enter the artist id for spotify', required=True)

    class Meta:
        template = "streams/spotify_pod.html"
        icon = "pilcrow"
        label = "Podcast"
