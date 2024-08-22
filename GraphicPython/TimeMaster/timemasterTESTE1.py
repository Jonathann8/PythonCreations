from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
import time

class CronometroApp(App):
    elapsed_time = StringProperty("00:00:00.000")
    current_time = StringProperty("00:00:00")

    def build(self):
        self.start_time = None
        self.paused_time = 0
        self.running = False
        self.lap_times = []
        self.notes = []
        self.trash = []

        # Criando o TabbedPanel
        self.tab_panel = TabbedPanel(do_default_tab=False)

        # Aba do Relógio (primeira aba)
        relogio_tab = TabbedPanelItem(text='Relógio')
        relogio_layout = BoxLayout(orientation='vertical')
        self.clock_label = Label(text=self.current_time, font_size='48sp', color=[1, 1, 1, 1], size_hint=(1, 0.7))
        relogio_layout.add_widget(self.clock_label)
        relogio_tab.add_widget(relogio_layout)
        self.tab_panel.add_widget(relogio_tab)

        # Aba do Cronômetro (segunda aba)
        cronometro_tab = TabbedPanelItem(text='Cronômetro')
        cronometro_layout = BoxLayout(orientation='vertical')
        self.label = Label(text=self.elapsed_time, font_size='48sp', color=[1, 1, 1, 1], size_hint=(1, 0.7))
        cronometro_layout.add_widget(self.label)

        button_layout = BoxLayout(size_hint=(1, 0.2))
        self.start_button = Button(text="Start", background_color=[0.298, 0.737, 0.447, 1])
        self.start_button.bind(on_press=self.start)
        button_layout.add_widget(self.start_button)

        self.pause_button = Button(text="Pause", background_color=[1, 0.603, 0.25, 1])
        self.pause_button.bind(on_press=self.pause)
        button_layout.add_widget(self.pause_button)

        self.reset_button = Button(text="Reset", background_color=[1, 0.263, 0.231, 1])
        self.reset_button.bind(on_press=self.reset)
        button_layout.add_widget(self.reset_button)

        self.lap_button = Button(text="Lap", background_color=[0.8, 0.8, 0.8, 1])
        self.lap_button.bind(on_press=self.record_lap)
        button_layout.add_widget(self.lap_button)

        self.clear_lap_button = Button(text="Clear Lap Times", background_color=[0.8, 0.8, 0.8, 1])
        self.clear_lap_button.bind(on_press=self.clear_lap_times)
        button_layout.add_widget(self.clear_lap_button)

        cronometro_layout.add_widget(button_layout)
        cronometro_tab.add_widget(cronometro_layout)
        self.tab_panel.add_widget(cronometro_tab)

        # Aba do Bloco de Notas (terceira aba)
        notas_tab = TabbedPanelItem(text='Notas')
        notas_layout = BoxLayout(orientation='vertical')

        self.notes_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        self.notes_layout.bind(minimum_height=self.notes_layout.setter('height'))

        self.note_input = TextInput(hint_text='Digite sua nota aqui...', size_hint_y=None, height=100)
        save_button = Button(text="Salvar Nota", size_hint_y=None, height=50)
        save_button.bind(on_press=self.save_note)

        notas_layout.add_widget(self.note_input)
        notas_layout.add_widget(save_button)
        notas_layout.add_widget(self.notes_layout)

        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(notas_layout)
        notas_tab.add_widget(scroll_view)
        self.tab_panel.add_widget(notas_tab)

        # Aba da Lixeira (quarta aba)
        lixeira_tab = TabbedPanelItem(text='Lixeira')
        lixeira_layout = BoxLayout(orientation='vertical')

        self.trash_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        self.trash_layout.bind(minimum_height=self.trash_layout.setter('height'))

        restore_button = Button(text="Restaurar Selecionado", size_hint_y=None, height=50)
        restore_button.bind(on_press=self.restore_selected_note)
        delete_button = Button(text="Apagar Selecionado", size_hint_y=None, height=50)
        delete_button.bind(on_press=self.delete_selected_note)
        empty_trash_button = Button(text="Esvaziar Lixeira", size_hint_y=None, height=50)
        empty_trash_button.bind(on_press=self.empty_trash)

        lixeira_layout.add_widget(self.trash_layout)
        lixeira_layout.add_widget(restore_button)
        lixeira_layout.add_widget(delete_button)
        lixeira_layout.add_widget(empty_trash_button)

        lixeira_scroll_view = ScrollView(size_hint=(1, 1))
        lixeira_scroll_view.add_widget(lixeira_layout)
        lixeira_tab.add_widget(lixeira_scroll_view)
        self.tab_panel.add_widget(lixeira_tab)

        Clock.schedule_interval(self.update_clock, 1)

        return self.tab_panel

    def update_clock(self, dt):
        self.current_time = time.strftime("%H:%M:%S")
        self.clock_label.text = self.current_time

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
            Clock.schedule_interval(self.update_time, 0.01)

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

    def record_lap(self, instance):
        if self.running or not self.running:
            lap_time = self.elapsed_time
            self.lap_times.append(lap_time)
            self.show_lap_times()

    def show_lap_times(self):
        layout = GridLayout(cols=1, padding=10, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        for lap in self.lap_times:
            lap_label = Label(text=lap, font_size='20sp', size_hint_y=None, height=40)
            layout.add_widget(lap_label)

        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(layout)

        popup = Popup(title='Lap Times', content=scroll_view, size_hint=(0.8, 0.8))
        popup.open()

    def clear_lap_times(self, instance):
        self.lap_times.clear()
        self.show_lap_times()

    def save_note(self, instance):
        note_text = self.note_input.text.strip()
        if note_text:
            note_id = len(self.notes) + 1
            note_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            note_checkbox = CheckBox(size_hint_x=None, width=40)
            note_label = Label(text=note_text, size_hint_x=None, width=240)
            delete_button = Button(text="Apagar", size_hint_x=None, width=80)
            delete_button.bind(on_press=self.delete_note)
            note_box.add_widget(note_checkbox)
            note_box.add_widget(note_label)
            note_box.add_widget(delete_button)
            self.notes_layout.add_widget(note_box)
            self.notes.append((note_id, note_box, note_text))
            self.note_input.text = ""

    def delete_note(self, instance):
        for note_id, note_box, note_text in self.notes:
            if instance in note_box.children:
                self.notes_layout.remove_widget(note_box)
                self.notes = [(nid, nb, nt) for nid, nb, nt in self.notes if nb != note_box]
                self.move_to_trash(note_box, note_text)
                break

    def move_to_trash(self, note_box, note_text):
        trash_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        trash_checkbox = CheckBox(size_hint_x=None, width=40)
        trash_label = Label(text=note_text, size_hint_x=None, width=240)
        restore_button = Button(text="Restaurar", size_hint_x=None, width=80)
        restore_button.bind(on_press=self.restore_note)
        delete_button = Button(text="Apagar", size_hint_x=None, width=80)
        delete_button.bind(on_press=self.delete_from_trash)
        trash_box.add_widget(trash_checkbox)
        trash_box.add_widget(trash_label)
        trash_box.add_widget(restore_button)
        trash_box.add_widget(delete_button)
        self.trash_layout.add_widget(trash_box)
        self.trash.append((note_box, note_text))

    def restore_note(self, instance):
        for trash_box, note_text in self.trash:
            if instance in trash_box.children:
                self.restore_note_instance(trash_box, note_text)
                break

    def delete_from_trash(self, instance):
        for trash_box, note_text in self.trash:
            if instance in trash_box.children:
                self.delete_from_trash_instance(trash_box, note_text)
                break

    def empty_trash(self, instance):
        self.trash_layout.clear_widgets()
        self.trash.clear()

    def restore_selected_note(self, instance):
        for trash_box, note_text in self.trash:
            if trash_box.children[0].active:
                self.restore_note_instance(trash_box, note_text)
                break

    def delete_selected_note(self, instance):
        for trash_box, note_text in self.trash:
            if trash_box.children[0].active:
                self.delete_from_trash_instance(trash_box, note_text)
                break

    def restore_note_instance(self, trash_box, note_text):
        self.trash_layout.remove_widget(trash_box)
        self.trash.remove((trash_box, note_text))
        self.notes.append((len(self.notes) + 1, trash_box, note_text))
        self.notes_layout.add_widget(trash_box)

    def delete_from_trash_instance(self, trash_box, note_text):
        self.trash_layout.remove_widget(trash_box)
        self.trash.remove((trash_box, note_text))

if __name__ == "__main__":
    CronometroApp().run()
