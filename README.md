# 百度百科风格项目

这是一个基于Django框架开发的百度百科风格的简易百科系统，实现了词条的创建、编辑、删除和分类管理等功能。

## 项目结构

```
20231201071/
├── hello/             # 主应用
│   ├── templates/hello/  # 模板文件
│   ├── __init__.py
│   ├── admin.py       # 后台管理配置
│   ├── apps.py
│   ├── forms.py       # 表单定义
│   ├── models.py      # 数据模型
│   ├── urls.py        # URL路由配置
│   └── views.py       # 视图函数
├── mysite/            # 项目配置
│   ├── __init__.py
│   ├── settings.py    # 项目设置
│   ├── urls.py        # 主URL配置
│   └── wsgi.py
├── manage.py          # Django管理脚本
└── README.md          # 项目说明
```

## 核心功能

1. **词条管理**
   - 查看词条列表
   - 查看词条详情
   - 创建新词条
   - 编辑词条
   - 删除词条

2. **分类管理**
   - 创建分类
   - 按分类筛选词条

3. **用户权限**
   - 仅登录用户可进行创建、编辑和删除操作
   - 使用Django内置的管理后台

## 数据模型

### Category（分类）
- name: 分类名称
- description: 分类描述
- created_at: 创建时间

### Entry（词条）
- title: 词条标题
- content: 词条内容
- category: 所属分类（外键）
- created_at: 创建时间
- updated_at: 更新时间
- view_count: 浏览次数

## 技术栈

- **后端**: Django 3.2+
- **前端**: HTML, CSS, JavaScript
- **UI框架**: Bootstrap 5
- **数据库**: SQLite

## 使用说明

### 安装依赖

```bash
pip install django
```

### 数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

### 创建超级用户

```bash
python manage.py createsuperuser
```

### 运行服务器

```bash
python manage.py runserver
```

### 访问项目

- 前台页面: http://127.0.0.1:8000/
- 管理后台: http://127.0.0.1:8000/admin/

## 实现细节

1. **模板继承**：使用base.html作为基础模板，其他页面继承并扩展
2. **表单处理**：使用Django的ModelForm简化表单创建和验证
3. **权限控制**：使用@login_required装饰器限制需要登录的操作
4. **响应式设计**：使用Bootstrap实现响应式布局，适应不同设备

## 项目特点

1. **简洁清晰的界面**：模仿百度百科的基本布局和风格
2. **完整的CRUD操作**：支持词条的增删改查
3. **分类管理**：支持词条分类和按分类筛选
4. **统计功能**：记录并显示词条的浏览次数
5. **用户友好**：提供适当的提示信息和操作反馈