from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import StringProperty
import time

class CronometroApp(App):
    elapsed_time = StringProperty("00:00:00.000")
    
    def build(self):
        self.start_time = None
        self.paused_time = 0  # Tempo em que o cronômetro foi pausado
        self.running = False
        
        layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text=self.elapsed_time, font_size='48sp', color=[1, 1, 1, 1], size_hint=(1, 0.7))
        layout.add_widget(self.label)
        
        button_layout = BoxLayout(size_hint=(1, 0.3))
        self.start_button = Button(text="Start", background_color=[0.298, 0.737, 0.447, 1])
        self.start_button.bind(on_press=self.start)
        button_layout.add_widget(self.start_button)
        
        self.pause_button = Button(text="Pause", background_color=[1, 0.603, 0.25, 1])
        self.pause_button.bind(on_press=self.pause)
        button_layout.add_widget(self.pause_button)
        
        self.reset_button = Button(text="Reset", background_color=[1, 0.263, 0.231, 1])
        self.reset_button.bind(on_press=self.reset)
        button_layout.add_widget(self.reset_button)
        
        layout.add_widget(button_layout)
        
        return layout

    def update_time(self, dt):
        if self.running:
            elapsed = time.time() - self.start_time + self.paused_time
            self.elapsed_time = self.format_time(elapsed)
            self.label.text = self.elapsed_time

    def format_time(self, elapsed):
        minutes, seconds = divmod(elapsed, 60)
        hours, minutes = divmod(minutes, 60)
        milliseconds = int((elapsed - int(elapsed)) * 1000)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{milliseconds:03}"
        
    def start(self, instance):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            Clock.schedule_interval(self.update_time, 0.01)  # Atualiza a cada 10 ms
        
    def pause(self, instance):
        if self.running:
            self.running = False
            Clock.unschedule(self.update_time)
            self.paused_time += time.time() - self.start_time
        
    def reset(self, instance):
        self.running = False
        self.paused_time = 0
        self.elapsed_time = "00:00:00.000"
        self.label.text = self.elapsed_time
        Clock.unschedule(self.update_time)

if __name__ == "__main__":
    CronometroApp().run()
