import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        m = hashlib.sha256()
        m.update(password.encode('utf-8'))
        self.password_hash = m.hexdigest()

    def display(self):
        print(f"회원이름: {self.name}, 아이디: {self.username}")

    def __repr__(self):
        return f"{self.name}님의 회원정보 아이디: {self.username}"


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(f"제목: {self.title}, 내용: {self.content}, 작성자: {self.author}")

# 회원 생성
members = [
    Member("Bruce Wayne", "bwayne", "1234"),
    Member("Jane Austen", "jausten", "2345"),
    Member("Donna Tartt", "dtartt", "5678")
]

# 각 회원별 포스트 딕셔너리
posts = []

bruce_posts = [
    {"title": "안녕", "content": "hello, 잘 지내세요"},
    {"title": "hi", "content": "아니요, 잘 못 지냅니다"},
    {"title": "how_Are_you", "content": "그런가봐요, 아닌가봐요"}
]

jane_posts = [
    {"title": "hello", "content": "오늘은 어떤 책을 읽을까요?"},
    {"title": "안녕하세요", "content": "하루가 참 짧네요"},
    {"title": "반갑습니다", "content": "여러분들도 좋아하는 책 추천해주세요!"}
]

donna_posts = [
    {"title": "당신은", "content": "우리 모두 책을 사랑합시다!"},
    {"title": "누구입니까", "content": "책을 읽는 건 마음을 풍부하게 합니다"},
    {"title": "나는당근입니다", "content": "책 읽고 나서 무엇을 느꼈나요?"}
]

# 각 회원별 포스트를 전체 포스트 리스트에 추가
for post_data in bruce_posts:
    posts.append(Post(post_data["title"], post_data["content"], members[0].username))

for post_data in jane_posts:
    posts.append(Post(post_data["title"], post_data["content"], members[1].username))

for post_data in donna_posts:
    posts.append(Post(post_data["title"], post_data["content"], members[2].username))

# 실행 코드

num_members = int(input("추가할 멤버 수를 입력하세요: "))
input_members = []
for i in range(num_members):
    input_name = input(f"{i+1}번째 멤버의 이름을 입력하세요: ")
    input_username = input(f"{input_name}님의 사용자 아이디를 입력하세요: ")
    input_password = input("비밀번호를 입력하세요: ")
    members.append(Member(input_name, input_username, input_password))
    input_members.append(Member(input_name, input_username, input_password))

for member in input_members:
    for i in range(1, 4):
        input_title = input(f"{member.name}님, 포스트 {i}의 제목을 입력하세요: ")
        input_content = input(f"포스트 {i}의 내용을 입력하세요: ")
        posts.append(Post(input_title, input_content, member.username))

# 결과 출력
print("\n=== 회원 목록 ===")
for member in members:
    member.display()

print("\n=== 포스트 목록 ===")
for post in posts:
    post.display()

print("\n=== Bruce Wayne 님의 포스트 ===")
for post in posts:
    if post.author == "bwayne":
        print(f"{post.title}")

print("\n=== 포스트 내용에 'hello' 포함된 제목 ===")
for post in posts:
    if "hello" in post.content:
        print(f"{post.title}")