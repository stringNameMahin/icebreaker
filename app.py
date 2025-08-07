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
    summary_obj, profile_pic_url = icebreak_with(name=name)
    
    return jsonify({
        "picture_url": profile_pic_url,
        "summary_and_facts": {
            "summary": summary_obj.Summary,
            "facts": summary_obj.facts
        },
        "ice_breakers": {
            "ice_breakers": [
                "Ask about their recent projects",
                "Discuss their professional interests"
            ]
        },
        "interests": {
            "topics_of_interest": [
                "Technology trends",
                "Professional development"
            ]
        }
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

