from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  # null=True로 설정
    image = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    

    @property
    def solved_problem_count(self):
        # 문제와 연관된 블로그 게시글 수를 반환
        return BlogPost.objects.filter(author=self.user, contest_id__isnull=False, index__isnull=False).count()
    
    @property
    def created_problem_count(self):
        # 사용자가 작성한 Problem 모델의 개수를 반환
        return Problem.objects.filter(author=self.user).count()
    
    @property
    def account_created_date(self):
        # 계정 생성 날짜 반환
        return self.user.date_joined

    def __str__(self):
        return self.user.username if self.user else "No User"

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Friendship(models.Model):
    user1 = models.ForeignKey(User, related_name='friends1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='friends2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class BlogPost(models.Model):
    VISIBILITY_CHOICES = [
        ('public', '전체공개'),
        ('private', '나만 보기'),
    ]
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='public')  # 공개 여부 추가
    # 문제 관련 필드 추가
    contest_id = models.CharField(max_length=20, blank=True, null=True)
    index = models.CharField(max_length=10, blank=True, null=True)
    problem_name = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    

    def __str__(self):
        return self.title
    

class Problem(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', '쉬움'),
        ('Medium', '중간'),
        ('Hard', '어려움'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    example_input = models.TextField(blank=True, null=True)
    example_output = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='problems/', blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='problems')

    def __str__(self):
        return self.title
    


class Question(models.Model):
    CATEGORY_CHOICES = [
        ('알고리즘', '알고리즘'),
        ('자료구조', '자료구조'),
        ('프로그래밍 언어', '프로그래밍 언어'),
        ('기타', '기타'),
    ]
    DIFFICULTY_CHOICES = [
        ('쉬움', '쉬움'),
        ('보통', '보통'),
        ('어려움', '어려움'),
    ]

    title = models.CharField(max_length=255)  # 질문 제목
    content = models.TextField()  # 질문 내용
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=True, null=True)  # 카테고리
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, blank=True, null=True)  # 난이도
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions_created')  # 작성자
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일

    def __str__(self):
        return self.title

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.question.title}'


class Data(models.Model):
    CATEGORY_CHOICES = [
        ('알고리즘', '알고리즘'),
        ('자료구조', '자료구조'),
        ('프로그래밍 언어', '프로그래밍 언어'),
        ('기타', '기타'),
    ]

    title = models.CharField(max_length=255)  # 질문 제목
    content = models.TextField(default="기본 내용 없음")  # 질문 내용, 기본값 설정
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=True, null=True)  # 카테고리
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='data_posts')  # 작성자
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일

    def __str__(self):
        return self.title

class StudyGroup(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='study_groups', blank=True)

    def __str__(self):
        return self.name

class Mission(models.Model):
    group = models.ForeignKey('StudyGroup', on_delete=models.CASCADE, related_name='missions')
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    is_deleted = models.BooleanField(default=False)  # 삭제 여부

    def __str__(self):
        return self.title
    
class Progress(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='progress_set')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    attachment = models.FileField(upload_to='progress_attachments/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mission.title} 진행사항"