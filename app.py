# Flask backend

from flask import Flask, send_file
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
import io

app = Flask(__name__)
generator = load_model("generator_model.h5")

@app.route('/generate', methods=['GET'])
def generate_face():
    noise = np.random.normal(0, 1, (1, 100))  # Adjust shape based on your model
    generated = generator.predict(noise)[0]
    generated = (generated + 1) / 2.0  # Rescale [-1,1] to [0,1]

    buf = io.BytesIO()
    plt.imsave(buf, generated, format='png')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')
