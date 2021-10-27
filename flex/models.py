from django.db import models

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks as wagtail_blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock

from streams import blocks
'''https://open.spotify.com/artist/6AOyhzwnRx5qmxHIWWIDaV?si=OYb0WeqnTIOLYkbJ2Sqeqg
https://open.spotify.com/show/2sRO4CwbOq9DbtskneuEcV?si=ade810e2325f43b4
'''
class FlexPage(Page):
    parent_page_types = ["home.HomePage", "flex.FlexPage"]
    body = StreamField(
        [
            ("title", blocks.TitleBlock()),
            ("cards", blocks.CardsBlock()),
            ("image_and_text", blocks.ImageAndTextBlock()),
            ("cta", blocks.CallToActionBlock()),
            ("youtube", blocks.YouTubeEmbedBlock()),
            ("spotify", blocks.SpotifyEmbedBlock()),
            ("podcast", blocks.PodcastEmbedBlock()),


            (
                "richtext",
                wagtail_blocks.RichTextBlock(
                    template="streams/simple_richtext_block.html",
                    features=["bold", "italic", "ol", "ul", "link"],
                ),
            ),
            (
                "large_image",
                ImageChooserBlock(
                    help_text="This image will be cropped to 1200px by 775px",
                    template="streams/large_image_block.html",
                ),
            ),


        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Flex (misc) page"
        verbose_name_plural = "Flex (misc) pages"

