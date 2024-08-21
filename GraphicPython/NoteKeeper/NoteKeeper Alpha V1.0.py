import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QPlainTextEdit, QCheckBox, QLabel, QColorDialog, QComboBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer, QDateTime

class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Manager")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #121212; color: #FFFFFF;")

        # Layout principal
        layout = QVBoxLayout()

        # Bloco de notas
        self.notes = QPlainTextEdit(self)
        self.notes.setPlaceholderText("Escreva suas notas aqui...")
        layout.addWidget(self.notes)

        # Caixa de marcações
        self.checklist = QCheckBox("Tarefa 1")
        layout.addWidget(self.checklist)

        # Filtro de tarefas
        self.filter_label = QLabel("Filtrar tarefas por:", self)
        layout.addWidget(self.filter_label)

        self.filter_box = QComboBox(self)
        self.filter_box.addItems(["Todas", "Trabalho", "Escola", "Estudos"])
        layout.addWidget(self.filter_box)

        # Lembrete
        self.reminder_label = QLabel("Defina um lembrete:", self)
        layout.addWidget(self.reminder_label)

        self.reminder_timer = QTimer(self)
        self.reminder_timer.timeout.connect(self.show_reminder)
        
        self.reminder_time = QDateTime.currentDateTime()
        layout.addWidget(QLabel(f"Lembrete definido para: {self.reminder_time.toString()}"))

        # Botão para mudar cor das notas
        self.color_button = QPushButton("Mudar Cor da Nota", self)
        self.color_button.clicked.connect(self.change_note_color)
        layout.addWidget(self.color_button)

        # Central Widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_reminder(self):
        # Lógica para mostrar o lembrete
        print("Lembrete! Chegou a hora!")

    def change_note_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.notes.setStyleSheet(f"background-color: {color.name()};")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManager()
    window.show()
    sys.exit(app.exec_())
