from flask import Flask, Blueprint, jsonify
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json, enum, random

app = Flask(__name__)

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emo_sys.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

music = Blueprint("music", url_prefix="/api/music", import_name=__name__)
feeling = Blueprint("feeling", url_prefix="/api/feeling", import_name=__name__)


class PressureLevel(enum.Enum):
    LOW = 1
    MIDDLE = 2
    HIGH = 3

class FeelingEmoji(enum.Enum):
    HAPPY = '🥰'
    FINE = '😊'
    BORING = '😐'
    UNHAPPY = '😟'
    COLLAPSE = '🥹'

def evalPressureLevelByPressure(pressure):
    if pressure < 30:
        return PressureLevel.LOW
    elif pressure < 60:
        return PressureLevel.MIDDLE
    else:
        return PressureLevel.HIGH

"模型"
class Feeling(db.Model):
    __tablename__ = "feeling"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(256))
    tag = db.Column(db.String(64))

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    avatar = db.Column(db.String(64))

@music.route("/get_info")
def getMusicInfo():
    with open("../public/music/music-info.json", "r", encoding="utf-8") as f:
        return json.loads(f.read())


@feeling.route("/get_info")
def getFeelingInfo():
    return jsonify({
        "data": {
            # 心率, 血氧, 压力, 元气, 压力等级
            "heartRate": random.randint(80, 120),
            "bloodOxygen": random.randint(94, 100),
            "pressure": random.randint(50, 70),
            "feeling": random.randint(30, 100),
            "pressureLevel": evalPressureLevelByPressure(random.randint(50, 70)).value,
            "emoji": FeelingEmoji.FINE.value
        },
    })


app.register_blueprint(music)
app.register_blueprint(feeling)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=9999, host='0.0.0.0')