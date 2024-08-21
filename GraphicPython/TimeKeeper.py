from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import StringProperty
import time

class CronometroApp(App):
    elapsed_time = StringProperty("00:00:00")
    
    def build(self):
        self.start_time = None
        self.running = False
        
        layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text=self.elapsed_time, font_size='48sp', color=[1, 1, 1, 1], size_hint=(1, 0.7))
        layout.add_widget(self.label)
        
        button_layout = BoxLayout(size_hint=(1, 0.3))
        self.start_button = Button(text="Iniciar", background_color=[0.298, 0.737, 0.447, 1])
        self.start_button.bind(on_press=self.start)
        button_layout.add_widget(self.start_button)
        
        self.pause_button = Button(text="Pausar", background_color=[1, 0.603, 0.25, 1])
        self.pause_button.bind(on_press=self.pause)
        button_layout.add_widget(self.pause_button)
        
        self.reset_button = Button(text="Reiniciar", background_color=[1, 0.263, 0.231, 1])
        self.reset_button.bind(on_press=self.reset)
        button_layout.add_widget(self.reset_button)
        
        layout.add_widget(button_layout)
        
        return layout

    def update_time(self, dt):
        if self.running:
            elapsed = int(time.time() - self.start_time)
            self.elapsed_time = time.strftime('%H:%M:%S', time.gmtime(elapsed))
            self.label.text = self.elapsed_time
        
    def start(self, instance):
        if not self.running:
            self.start_time = time.time() - self._elapsed_time()
            self.running = True
            Clock.schedule_interval(self.update_time, 1)
        
    def pause(self, instance):
        if self.running:
            self.running = False
            Clock.unschedule(self.update_time)
        
    def reset(self, instance):
        self.running = False
        self.elapsed_time = "00:00:00"
        self.label.text = self.elapsed_time
        Clock.unschedule(self.update_time)

    def _elapsed_time(self):
        if self.running:
            return time.time() - self.start_time
        return 0

if __name__ == "__main__":
    CronometroApp().run()
