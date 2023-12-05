import requests
from PyQt5 import QtWidgets
import json

secrets = json.load(open("secrets.json"))
API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/" +secrets.get("user")+"/ai/run/"
headers = {"Authorization": "Bearer "+secrets.get("token")}

def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()

def ask_question():
    question = question_entry.text()
    inputs = [
        { "role": "system", "content": "You are a friendly assistant that helps write stories" },
        { "role": "user", "content": question }
    ]
    output = run("@cf/meta/llama-2-7b-chat-int8", inputs)
    answer = output.get('result').get('response')
    answer_textbox.setText(answer)

# Create GUI
app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setWindowTitle("AI Assistant")
window.setGeometry(100, 100, 600, 350)

question_label = QtWidgets.QLabel(window)
question_label.setText("Ask a question:")
question_label.move(20, 20)

question_entry = QtWidgets.QLineEdit(window)
question_entry.move(20, 50)
question_entry.setFixedWidth(560)

ask_button = QtWidgets.QPushButton(window)
ask_button.setText("Ask")
ask_button.move(20, 80)
ask_button.clicked.connect(ask_question)

answer_textbox = QtWidgets.QTextEdit(window)
answer_textbox.move(20, 120)
answer_textbox.setFixedWidth(560)

window.show()
app.exec_()
