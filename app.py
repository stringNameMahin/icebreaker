from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from icebreaker import icebreak_with

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    Summary, profile_pic_url = icebreak_with(name=name)
    return jsonify(
        {
            "Summary and facts": Summary.to_dict(),
            "photoUrl": profile_pic_url
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

