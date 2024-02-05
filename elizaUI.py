import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextBrowser, QLineEdit, QPushButton
from eliza import Eliza
#add the ui for elia
class ElizaUI(QWidget):
    def __init__(self, eliza_instance):
        super().__init__()
        self.eliza = eliza_instance

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Eliza 3.0')
        self.setGeometry(100, 100, 600, 400)

        # Create widgets
        self.chat_display = QTextBrowser()
        self.user_input = QLineEdit()
        self.send_button = QPushButton('Send')

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.chat_display)
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.user_input)
        input_layout.addWidget(self.send_button)
        main_layout.addLayout(input_layout)
        self.setLayout(main_layout)

         # Set Stylesheet for custom colors
        self.setStyleSheet("""
            QWidget {
                background-color: #f2f2f2; /* Light gray background */
                color: #333333; /* Dark text color */
                font-family: Arial, sans-serif;
            }
            QPushButton {
                background-color: #4CAF50; /* Green button */
                color: white; /* White text */
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 5px;
            }
            QLineEdit {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QTextBrowser {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                background-color: #ffffff; /* White background */
            }
        """)

        # Connect button click event
        self.send_button.clicked.connect(self.on_send_button_clicked)
        self.user_input.returnPressed.connect(self.on_send_button_clicked)


        # Set initial greeting in chat display
        initial_greeting = self.eliza.initial()
        self.chat_display.append(f"Eliza: {initial_greeting}")

        self.show()

    def on_send_button_clicked(self):
        user_message = self.user_input.text()
        self.chat_display.append(f"User: {user_message}")

        # Get Eliza's response
        eliza_response = self.eliza.respond(user_message)
        self.chat_display.append(f"Eliza: {eliza_response}")

        self.user_input.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    eliza_instance = Eliza()
    eliza_instance.load('doctor.txt')
    window = ElizaUI(eliza_instance)
    sys.exit(app.exec_())
