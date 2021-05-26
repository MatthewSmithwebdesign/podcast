from django.db import models


from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

# Create your blocks here.

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
