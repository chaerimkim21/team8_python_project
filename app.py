# 필수 라이브러리
'''
0. Flask : 웹서버를 시작할 수 있는 기능. app이라는 이름으로 플라스크를 시작한다
1. render_template : html파일을 가져와서 보여준다
2. request : 클라이언트로부터 HTTP 요청을 처리
3. jsonify :  JSON 응답을 생성하기 위해 사용
4. redirect : 클라이언트를 다른 URL로 리디렉션시키는 데 사용
5. url_for : URL 빌드를 돕는 함수로, 엔드포인트 이름을 기반으로 URL 생성
6. SQLAlchemy :  데이터베이스 모델 정의, 쿼리 실행
7. Migrate : 데이터베이스 스키마의 변경 추적, 관리
8. random : 랜덤한 값을 생성하기 위해 사용
'''
from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# DB 모델 정의
class GameRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_choice = db.Column(db.String(10), nullable=False)
    computer_choice = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String, nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    ties = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'사용자: {self.player_choice} 컴퓨터: {self.computer_choice} '

choices_map = {
    '가위': {'wins_against': '보', 'loses_to': '바위'},
    '바위': {'wins_against': '가위', 'loses_to': '보'},
    '보': {'wins_against': '바위', 'loses_to': '가위'}
}

def get_computer_choice():
    return random.choice(list(choices_map.keys()))

with app.app_context():
    db.create_all()

@app.route("/reset-data", methods=['POST'])
def reset_data():
    try:
        #GameRecord 테이블의 모든 행(rows) 삭제
        db.session.query(GameRecord).delete()
        db.session.commit()
        # 테이블의 데이터 삭제 후 홈페이지로 이동
        return redirect(url_for('index'))
    except Exception as e:
        db.session.rollback()
        #JSON 형식의 응답 보냄
        return jsonify({'message': f'Failed to reset data: {str(e)}'}), 500

@app.route("/")
def index():
    game_records = GameRecord.query.all()
    return render_template("index.html", game_records=game_records)

@app.route('/play', methods=['POST', 'GET'])
def play():
    if request.method == 'POST':
        player_choice = request.form['player_choice']
        computer_choice = get_computer_choice()

        if player_choice not in choices_map:
            return render_template('index.html', message='유효한 입력이 아닙니다.', game_records=GameRecord.query.all())
        
        # 이전 게임 기록의 승무패 횟수 저장하기
        last_record = GameRecord.query.order_by(GameRecord.id.desc()).first()
        wins = last_record.wins if last_record else 0 # 이전 게임 기록이 없으면 0으로
        losses = last_record.losses if last_record else 0
        ties = last_record.ties if last_record else 0

        # 게임 승부 판별
        if player_choice == computer_choice:
            result = '무승부입니다!'
            ties += 1
        elif computer_choice == choices_map[player_choice]['loses_to']:
            result = '졌습니다. 컴퓨터 승리!'
            losses += 1
        else:
            result = '이겼습니다! 사용자 승리!'
            wins += 1

        # 게임 기록 DB에 저장
        game_record = GameRecord(player_choice=player_choice, computer_choice=computer_choice, result=result, wins=wins, losses=losses, ties=ties)
        db.session.add(game_record)
        db.session.commit()

        return render_template('index.html', data={'player_choice': player_choice, 'computer_choice': computer_choice, 'result' : result, 'wins': wins, 'losses': losses, 'ties': ties}, game_records=GameRecord.query.all())
    
    # HTTP 요청이 GET일때 index.html에 GameRecord에 있는 데이터가 렌더링되도록 함
    return render_template('index.html', game_record=GameRecord.query.all())

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)
