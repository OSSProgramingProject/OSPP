from django.urls import path
from IBK_ossproject import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os
urlpatterns = [
    path('', views.home, name='home'),  # 홈 페이지
    path('login/', views.user_login, name='login'),  # 로그인 페이지
    path('logout/', views.user_logout, name='logout'), # 로그아웃
    path('update-profile-image/', views.update_profile_image, name='update_profile_image'),
    path('question-bank/', views.question_bank, name='question_bank'),
    path('community/', views.community, name='community'),  # 커뮤니티 페이지
    path('blog-post/', views.blog_post, name='blog_post'),  # 블로그 페이지
    path('signup/', views.signup, name='signup'),  # 회원가입 페이지
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # 포스트 상세 페이지
    path('find-id/', views.find_id, name='find_id'),  # ID 찾기 페이지
    path('find-id-result/', views.find_id_result, name='findid_result'),  # 아이디 찾기 결과
    path('findpassword/', views.findpassword, name='findpassword'),  # 비밀번호 찾기 페이지
    path('findpassword-result/', views.findpassword_result, name='findpassword_result'),  # 비밀번호 찾기 결과 페이지
    path('profile/', views.profile_management, name='profile_management'),  # 프로필 관리 페이지
    path('admin/', admin.site.urls), #관리자 페이지 경로 설정
    path('qa-board/', views.qa_board, name='qa_board'), # QnA 게시판
    path('resources-board/', views.resources_board, name='resources_board'), # 자료 게시판
    path('follow/', views.follow_user, name='follow_user'),
    path('send_message/', views.send_message, name='send_message'),
    path('add_friend/', views.add_friend, name='add_friend'),
    path('problem-creation/', views.create_problem, name='problem_creation'),
    path('user_problem/', views.user_problem, name='user_problem'),
    path('problem/<int:pk>/', views.problem_detail, name='problem_detail'),
    path('problem/<int:pk>/edit/', views.edit_problem, name='edit_problem'),
    path('problem/delete/<int:pk>/', views.delete_problem, name='delete_problem'),  # 삭제 URL 추가
    path('qa/create/', views.qa_creation, name='qa_creation'),  # 질문 작성 페이지
    path('qa/<int:question_id>/', views.question_detail, name='question_detail'),  # 질문 상세 페이지
    path('qa/<int:question_id>/edit/', views.qa_edit, name='qa_edit'),  # 질문 수정 페이지 추가
    path('qa/delete/<int:question_id>/', views.delete_question, name='qa_delete'),
    path('data/upload/', views.data_upload, name='data_upload'),  # 자료 업로드
    path('data/<int:data_id>/', views.data_detail, name='data_detail'),  # 자료 상세 보기
    path('data/<int:data_id>/edit/', views.data_edit, name='data_edit'),  # 자료 수정
    path('data/delete/<int:id>/', views.data_delete, name='data_delete'), # 자료 삭제
    path('blog_creat/', views.blog_create, name='blog_creation'),  # 블로그 작성 페이지
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/edit/<int:pk>/', views.blog_edit, name='blog_edit'),
    path('blog/search/', views.blog_search, name='blog_search'),
    path('blog/delete/<int:pk>/', views.blog_delete, name='blog_delete'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('delete_received_message/<int:message_id>/', views.delete_received_message, name='delete_received_message'),
    path('question/<int:question_id>/add_comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('blog/category-search/', views.blog_category_search, name='blog_category_search'),
    path('blog/category-search/', views.blog_category_search, name='blog_category_search'),
    path('user_generated_question_bank/', views.user_generated_question_bank, name='user_generated_question_bank'),
    path('user_problem_solving/<int:problem_id>/', views.user_problem_solving_creation, name='user_problem_solving_creation'),
    path('study-groups/', views.study_groups, name='study_groups'),
    path('create-study-group/', views.create_study_group, name='create_study_group'),
    path('join-study-group/<int:group_id>/', views.join_study_group, name='join_study_group'),
    path('leave-study-group/<int:group_id>/', views.leave_study_group, name='leave_study_group'),
    path('kick-member/<int:group_id>/<int:user_id>/', views.kick_member, name='kick_member'),
    path('study-group/<int:group_id>/', views.study_group_detail, name='study_group_detail'),
    path('study-group/<int:group_id>/create-mission/', views.create_mission, name='create_mission'),
    path('mission/<int:mission_id>/upload-progress/', views.upload_progress, name='upload_progress'),
    path('mission/<int:mission_id>/delete/', views.delete_mission, name='delete_mission'),
    path('study-group/<int:group_id>/delete/', views.delete_study_group, name='delete_study_group'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)