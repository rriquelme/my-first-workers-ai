import requests
from PyQt5 import QtWidgets, QtGui
import json
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageQt
from io import StringIO
import io
import shutil
# Documentation to do this was obtained from https://developers.cloudflare.com/workers-ai/
secrets = json.load(open("secrets.json"))
API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/" +secrets.get("user")+"/ai/run/"
headers = {"Authorization": "Bearer "+secrets.get("token"), "-X": "POST"}



def run(model, inputs):
    #input = { "prompt": "cat" }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=inputs)

    # Convert the response content to an image
    img = Image.open(io.BytesIO(response.content))
    img.save("temp.png")
    #image_label.move(20, 160)
    pixmap_ = QtGui.QPixmap("temp.png").scaledToWidth(560)
    image_label.setPixmap(pixmap_)
    return img

def ask_question():
    question = question_entry.text()
    inputs = { "prompt": question }
    img = run("@cf/stabilityai/stable-diffusion-xl-base-1.0", inputs)
    #print(output)


# Create GUI
app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setWindowTitle("AI Assistant")
window.setGeometry(100, 100, 600, 800)

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

#create a widget to display the image
image_label = QtWidgets.QLabel(window)
image_label.move(20, 160)
image_label.setFixedWidth(560)
image_label.setFixedHeight(560)


window.show()
app.exec_()
