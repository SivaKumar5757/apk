from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from plyer import notification
Config.set('graphics', 'minimum_width', '300')
Config.set('graphics', 'minimum_height', '300')
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'borderless', False)
Config.set('graphics', 'window_state', 'visible')
Config.set('kivy', 'window_icon', 'icon.png')
class Intro(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = AnchorLayout(anchor_x='center', anchor_y='center',padding = 50)
        img = Image(source='lods.png')
        layout.add_widget(img)
        self.add_widget(layout)
        Clock.schedule_once(self.switch_to_main, 3)
    def switch_to_main(self,dt):
        self.manager.current ='main'
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = AnchorLayout(anchor_x='center', anchor_y='center',padding=5)
        button = Button(text='Notify',pos=(100, 100), size_hint=(None, None),size=(100, 50))
        layout.add_widget(button)
        button.bind(on_release=self.show_notification)
        self.add_widget(layout)
    def show_notification(self, button):
        # Use the plyer notification module to show a notification
        notification.notify(
            title='Notification',
            message='This is a notification message.'
        )
    
class Dustbin(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(Intro(name="intro"))
        sm.add_widget(MainScreen(name="main"))
        return sm

if __name__ == '__main__':
    Dustbin().run()