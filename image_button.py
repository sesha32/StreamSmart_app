from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

# Load the KV file from the kv folder
Builder.load_file('kv/image_button.kv')

class ImageButton(ButtonBehavior, Image):
    pass
