import hashlib

#----- 클래스 정의 ------

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

#----- 샘플 멤버 및 포스트 생성 함수 ------

def create_sample_members():
    members = []
    members.append(Member("Bruce Wayne", "bwayne", "1234"))
    members.append(Member("Jane Austen", "jausten", "2345"))
    members.append(Member("Donna Tartt", "dtartt", "5678"))
    return members

def create_sample_posts(members):
    posts = []
    for member in members:
        for i in range(1, 4):
            posts.append(Post(f"{member.username}_post{i}", "hello", member.username))
    return posts

#----- 실행 코드 ------

members = create_sample_members()
posts = create_sample_posts(members)

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

#----- 결과 출력 ------

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
