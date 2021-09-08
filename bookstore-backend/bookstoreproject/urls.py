"""bookstoreproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

import xadmin
from books.views import CategoryViewSet, BooksViewSet, CommentViewSet
from bookstoreproject.settings import MEDIA_ROOT
from users.views import UserViewSet, LoginViewSet

router = DefaultRouter()

router.register('category', CategoryViewSet)
router.register('book', BooksViewSet)
# router.register('user', UserViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),

    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    
    path('api-auth/', include('rest_framework.urls')),

    # drf文档
    path('docs/', include_docs_urls(title='图书后台管理')),

    # 复杂查询路由
    # 根据分类查询书籍列表
    path('api/book/category/<int:pk>/page', BooksViewSet.as_view({'get': 'category'})),

    # 搜索（书名关键字）
    path('api/search', BooksViewSet.as_view({'get': 'search'})),

    # 评论
    path('api/book/<int:pk>/comment', CommentViewSet.as_view({'get': 'commentlist'})),

    # 注册
    path('api/user/register', UserViewSet.as_view({'post': 'register'})),

    # 登录
    path('api/user/login', LoginViewSet.as_view({'post': 'login'})),

    # 检查用户名是否已存在
    path('api/user/<str:username>', UserViewSet.as_view({'get': 'existed'})),

    # 增加公共前缀/api，后端api的入口
    re_path(r'^api/', include(router.urls)),
]
