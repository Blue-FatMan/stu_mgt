import xadmin
from xadmin import views

from account.models import User


class BaseSetting(object):
    '''xadmin基本配置'''
    #开启主题切换功能
    enable_themes = True
    #支持切换主题
    use_bootswatch = True


class GlobalSettings(object):
    #设置头标题
    site_title = '学生成绩管理系统'
    #设置脚标题, 关于版权信息
    site_footer = '赣ICP备19003810'
    #设置菜单可导航栏折叠
    menu_style = 'accordion'


class UserAdmin(object):
    list_display = ['username', 'password', 'is_superuser']
    ordering = ['-create_time', 'username', 'is_superuser']
    search_fields = ['username', 'is_superuser', 'user_type']


xadmin.site.unregister(User)
xadmin.site.register(User, UserAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)