from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Welcome', font_size=50, pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        self.add_widget(Button(text='Click to explore', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                on_release=self.change_screen,background_color=(1, 0, 50, 30)))

    def change_screen(self, *args):
        screen_manager.current = 'second'


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='This is my first try to make an android app in python. \n Happy to see an user here! ', font_size=30, pos_hint={'center_x': 0.5, 'center_y': 0.6}))
        self.add_widget(Button(text='Home', size_hint=(0.1, 0.1), pos_hint={'x': 0, 'y': 0.910},
                                on_release=self.go_home,background_color=(1, 11, 2, 1)))
        self.add_widget(Button(text='Exit', size_hint=(0.1, 0.09), pos_hint={'right': 0.20, 'y': 0.910},
                                on_release=self.exit_app, background_color=(1, 0, 0, 1)))

    #my added
        self.add_widget(Button(text='Go to calculator', size_hint=(0.2, 0.1), pos_hint={'right': 0.6, 'y': 0.40},
                               on_release=self.go_cal,background_color=(1, 0, 50, 30)))


    def go_home(self, *args):
        screen_manager.current = 'first'

    def exit_app(self, *args):
        App.get_running_app().stop()

    def go_cal(self, *args):
        screen_manager.current='third'


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(
            Label(text='Calculate here!! ', font_size=27, pos_hint={'center_x': 0.5, 'center_y': 0.8}))
#        self.add_widget(Button(text='Home', size_hint=(0.1, 0.07), pos_hint={'x': 0.80, 'y': 0}, on_release=self.goi))
        self.add_widget(Button(text='Home', size_hint=(0.1, 0.07), pos_hint={'x': 0.80, 'y': 0}, on_release=self.goi,
                               background_color=(1,17, 0, 1)))

        self.add_widget(Button(text='Exit', size_hint=(0.1, 0.07),pos_hint={'right': 1, 'y': 0}, on_release=self.ex ,background_color=(1, 0, 0, 1)))
# pos_hint={'right': 0.20, 'y': 0.910}

        # Add the calculator to the screen
        calculator = Calculator()
        self.add_widget(calculator)

    def goi(self,*args):
        screen_manager.current='first'

    def ex(self,*args):
        App.get_running_app().stop()


class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create the main layout for the app
        main_layout = BoxLayout(orientation='vertical')

        # Create the input field for the calculator
        self.input_field = TextInput(font_size=54, size_hint_y=0.3, multiline=True)
        main_layout.add_widget(self.input_field)

        # Create the button grid for the calculator
        button_grid = GridLayout(cols=4, size_hint_y=0.3)

        # Define the button labels
        button_labels = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '.', '0', '=', '/', 'Clear']

        # Create a button for each label and add it to the button grid
        for label in button_labels:
            button = Button(text=label, font_size=24)
            if label == 'Clear':
                button.bind(on_press=self.clear_input)
            else:
                button.bind(on_press=self.button_pressed)
            button_grid.add_widget(button)

        main_layout.add_widget(button_grid)

        self.add_widget(main_layout)

    def button_pressed(self, button):
        # Get the current text in the input field
        current_text = self.input_field.text

        if button.text == '=':
            # Evaluate the current expression and display the result
            try:
                result = eval(current_text)
                self.input_field.text = str(result)
            except:
                self.input_field.text = 'Infinity. \n i.e. Anything divisible by is infinity ;)'
        else:
            # Append the button text to the input field
            self.input_field.text = current_text + button.text

    def clear_input(self, button):
        self.input_field.text = ''

class CalculatorApp(App):
    def build(self):
        return Calculator()


class MyScreenManager(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        global screen_manager
        screen_manager = MyScreenManager()
        screen_manager.add_widget(FirstScreen(name='first'))
        screen_manager.add_widget(SecondScreen(name='second'))
        screen_manager.add_widget(ThirdScreen(name='third'))

        return screen_manager


if __name__ == '__main__':
    Window.clearcolor = (0.5, 0, 1, 1) # purple color for first screen
    MyApp().run()
