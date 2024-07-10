<img src="https://capsule-render.vercel.app/api?type=waving&color=BDBDC8&height=150&section=header" />
<div align=center>:satisfied:<h3>이 저장공간은 팀스파르타 파이썬 8조 팀과제를 위한 공간입니다.</h3>:pray:

![rsp_web_screen](https://github.com/chaerimkim21/team8_python_project/assets/90311848/4c240cdf-2ca3-48de-b694-403159804a1d)

<h2>:clock130:작업소요기간:2024-07-03~2024-07-09:ok_hand:</h2>

<h3>:open_file_folder:프로젝트 구조</h3>:v:
├── README.md
├── __pycache__
├── .venv
├── migrations
├── templates
│   └── index.html
├── app.py
├── database.db
└── members.py

<h3>:book:Explanation
:one: 회원 관리 프로그램
### 회원 관리 (Member Management)

- **회원 등록 (Member Registration)**
    - 사용자로부터 이름, 사용자 아이디, 비밀번호를 입력받아 새로운 회원을 등록합니다.
    - 비밀번호는 SHA-256 해시를 이용해 암호화하여 저장합니다.
    - `Member` 클래스를 사용하여 회원 정보를 관리합니다.
- **회원 정보 출력 (Display Member Information)**
    - 등록된 회원의 이름과 사용자 아이디를 출력합니다.
    - `display` 메소드를 사용하여 회원 정보를 출력합니다.
- **회원 리스트 관리 (Manage List of Members)**
    - 모든 등록된 회원의 정보를 리스트 형식으로 관리합니다.

#### 게시물 관리 (Post Management)

- **게시물 작성 (Create Post)**
    - 회원은 제목과 내용을 입력하여 게시물을 작성할 수 있습니다.
    - 게시물은 `Post` 클래스를 사용하여 관리되며, 작성자는 회원의 사용자 아이디로 저장됩니다.
- **게시물 출력 (Display Post)**
    - 작성된 게시물의 제목, 내용, 작성자를 출력합니다.
    - `display` 메소드를 사용하여 게시물 정보를 출력합니다.
- **회원별 게시물 관리 (Manage Posts by Member)**
    - 각 회원은 자신의 게시물을 작성하고 관리할 수 있습니다.
    - 각 회원별로 게시물을 저장하여 관리합니다.

#### 실행 코드 (Execution Code)

- **회원 추가 (Add Members)**
    - 사용자로부터 추가할 회원의 수와 각 회원의 이름, 사용자 아이디, 비밀번호를 입력받아 회원을 추가합니다.
    - 입력받은 정보를 바탕으로 새로운 `Member` 객체를 생성하고, 리스트에 추가합니다.
- **게시물 추가 (Add Posts)**
    - 사용자로부터 각 회원별 게시물의 제목과 내용을 입력받아 게시물을 추가합니다.
    - 입력받은 정보를 바탕으로 새로운 `Post` 객체를 생성하고, 리스트에 추가합니다.
- **회원 목록 출력 (Display Member List)**
    - 모든 회원의 정보를 출력합니다.
    - `display` 메소드를 사용하여 각 회원의 정보를 출력합니다.
- **게시물 목록 출력 (Display Post List)**
    - 모든 게시물의 정보를 출력합니다.
    - `display` 메소드를 사용하여 각 게시물의 정보를 출력합니다.
- **특정 회원의 게시물 출력 (Display Posts of Specific Member)**
    - 특정 회원이 작성한 게시물의 제목을 출력합니다.
    - 게시물 리스트를 순회하며 작성자가 해당 회원인 경우 제목을 출력합니다.
- **특정 키워드가 포함된 게시물 검색 (Search Posts by Keyword)**
    - 게시물 내용에 특정 키워드가 포함된 게시물의 제목을 출력합니다.
    - 게시물 리스트를 순회하며 내용에 키워드가 포함된 경우 제목을 출력합니다.


:two: 가위바위보 웹 게임
#### 웹 애플리케이션 설정 및 구성 (Web Application Setup and Configuration)

- **Flask 애플리케이션 설정 (Flask Application Configuration)**
    - Flask를 사용하여 웹 애플리케이션을 설정하고 시작합니다.
    - 데이터베이스는 SQLite를 사용하며, SQLAlchemy와 Flask-Migrate를 통해 데이터베이스 관리 및 마이그레이션을 수행합니다.

#### 데이터베이스 모델 (Database Model)

- **GameRecord 모델 (GameRecord Model)**
    - 게임 기록을 저장하기 위한 데이터베이스 모델입니다.
    - 필드: `id` (게임 ID), `player_choice` (사용자가 선택한 가위, 바위, 보), `computer_choice` (컴퓨터가 선택한 가위, 바위, 보), `result` (게임 결과), `wins` (승리 횟수), `losses` (패배 횟수), `ties` (무승부 횟수).

#### 라우팅 및 핸들러 (Routing and Handlers)

- **홈페이지 라우트 (Home Route)**
    - "/" 경로로 접속 시 게임 기록을 조회하여 홈페이지(index.html)를 렌더링합니다.
    - 데이터베이스에서 모든 게임 기록을 가져와 템플릿에 전달합니다.
- **게임 플레이 라우트 (Game Play Route)**
    - "/play" 경로로 POST 요청이 들어오면 사용자의 선택을 받아 가위, 바위, 보 게임을 진행합니다.
    - 컴퓨터의 선택은 랜덤으로 결정됩니다.
    - 게임 결과를 판별하고, 결과에 따라 승리, 패배, 무승부 횟수를 업데이트합니다.
    - 게임 기록을 데이터베이스에 저장하고, 결과를 포함한 페이지를 렌더링합니다.
    - 사용자가 유효하지 않은 입력을 하면 에러 메시지를 표시합니다.
- **데이터 초기화 라우트 (Data Reset Route)**
    - "/reset-data" 경로로 POST 요청이 들어오면 데이터베이스의 모든 게임 기록을 삭제합니다.
    - 데이터 초기화 후 홈페이지로 리디렉션합니다.


<h2>:round_pushpin: Stack</h2>
- Backend: <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">#3776AB</font></font>Python, <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">#000000</font></font>Flask, <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">#003B57</font></font>SQLite
- Frontend: <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">#E34F26</font></font>HTML, <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">#1572B6</font></font>CSS, <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">#7952B3</font></font>Bootstrap

<h2>:family: Developer </h2>
- :angel: 김채림(조장)
- :raising_hand: 임성혁(조원)
- :massage: 임선오(조원)
- :boy: 조도흠(조원)
- :man: 박준희(조원)

</div>
