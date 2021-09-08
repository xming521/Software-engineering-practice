from django.contrib import admin

# Register your models here.

import xadmin
from xadmin import views


class BaseSetting(object):
    #添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    #全局配置，后台管理标题和页脚
    site_title = "图书商城后台管理"
    site_footer = "http://127.0.0.1:8000/xadmin/"
    #菜单收缩
    menu_style = "accordion"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
