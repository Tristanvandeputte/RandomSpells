import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from generate_spell_list import generate_spells

kivy.require('1.11.1')

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=10)
        self.input_box = TextInput(multiline=False, size_hint=(0.8, 1), input_filter='int')
        input_layout.add_widget(self.input_box)

        self.button = Button(text="Generate Spells", size_hint=(0.2, 1))
        self.button.bind(on_press=self.on_button_click)
        input_layout.add_widget(self.button)

        self.layout.add_widget(input_layout)

        self.output_label = Label(size_hint=(1, 0.9))
        self.layout.add_widget(self.output_label)

        return self.layout

    def on_button_click(self, instance):
        input_value = self.input_box.text
        if input_value.isdigit():
            sorcerer_level = int(input_value)
            if 1 <= sorcerer_level <= 20:
                output_value = generate_spells(sorcerer_level)
                self.output_label.text = output_value
            else:
                self.output_label.text = "Please enter a number between 1 and 20."
        else:
            self.output_label.text = "Invalid input. Please enter a number."

if __name__ == '__main__':
    MyApp().run()
