from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BlogPost
from .models import Problem
from .models import Question
from .models import Comment
from .models import Data
from .models import StudyGroup
from .models import Mission



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FollowForm(forms.Form):
    user_to_follow = forms.CharField(max_length=150)

class MessageForm(forms.Form):
    receiver = forms.CharField(max_length=150)
    content = forms.CharField(widget=forms.Textarea)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'category', 'content', 'image', 'visibility']
        
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # user를 kwargs에서 꺼내옵니다.
        super(BlogPostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(BlogPostForm, self).save(commit=False)
        if self.user:
            instance.author = self.user  # author를 현재 사용자로 설정합니다.
        if commit:
            instance.save()
        return instance
    

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'description', 'image', 'category', 'difficulty', 'example_input', 'example_output']
        


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        # 모델에 실제 존재하는 필드만 사용합니다.
        fields = ['title', 'category', 'difficulty', 'content']  # 'content' 필드 추가

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '질문의 제목을 입력하세요'}),
            'category': forms.Select(),
            'difficulty': forms.Select(),
            'content': forms.Textarea(attrs={'placeholder': '질문 내용을 입력하세요', 'rows': 10}),  # 'content' 필드에 위젯 추가
        }

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['title', 'category', 'content']
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '질문의 제목을 입력하세요'}),
            'category': forms.Select(),
            'content': forms.Textarea(attrs={'placeholder': '질문 내용을 입력하세요', 'rows': 10}),  # 'content' 필드에 위젯 추가
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': '댓글을 작성하세요...', 'rows': 3}),
        }

class StudyGroupForm(forms.ModelForm):
    class Meta:
        model = StudyGroup
        fields = ['name', 'topic', 'description', 'capacity']

class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['title', 'description', 'deadline']