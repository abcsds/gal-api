from flask import Flask, request
import galai as gal

app = Flask(__name__)

@app.before_first_request
def load_model():
    global model
    model = gal.load_model(name="base", num_gpus=1)

@app.route("/", methods=["POST"])
def generate_text():
    input_text = request.form.get("prompt")
    generated_text = model.generate(input_text, max_length=400)
    return generated_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)