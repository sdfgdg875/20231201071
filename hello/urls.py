from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_list, name='entry_list'),  # 首页显示词条列表
    path('entry/<int:entry_id>/', views.entry_detail, name='entry_detail'),  # 词条详情
    path('entry/create/', views.entry_create, name='entry_create'),  # 创建词条
    path('entry/<int:entry_id>/edit/', views.entry_edit, name='entry_edit'),  # 编辑词条
    path('entry/<int:entry_id>/delete/', views.entry_delete, name='entry_delete'),  # 删除词条
    path('category/<int:category_id>/', views.category_entries, name='category_entries'),  # 按分类查看词条
    path('category/create/', views.category_create, name='category_create'),  # 创建分类
]