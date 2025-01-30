import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, ListProperty

# Import your custom ImageButton if neededfrom .imagebutton import ImageButton

# Load the KV file correctly
root = os.path.dirname(__file__)
Builder.load_file(os.path.join(root, 'main.kv'))

class CustomButton(BoxLayout):
    icon = StringProperty('')
    icon_map = StringProperty('')
    icon_people = StringProperty('')
    text = StringProperty('')
    button_color = ListProperty([0, 0, 0, 0.2])
    text_color = ListProperty([0, 0, 0, 0.1])
    events_callback = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        # Additional initialization can be done here if needed

        # Example of setting up a button click event
        self.bind(on_release=self.on_button_click)

    def on_button_click(self):
        if self.events_callback:
            self.events_callback()
