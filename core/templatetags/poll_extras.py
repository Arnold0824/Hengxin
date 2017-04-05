from django import template
from core.models import *
from core.views import my_custom_sql
import re
register = template.Library()
@register.inclusion_tag('backend/inclusion_tag_carousel.html')
def table_carousels(**kwargs):
    context={
        'title':kwargs['title'],
        'img': kwargs['img'],
        'caption': kwargs['caption'],
        'link': kwargs['link'],
        'dimdate': kwargs['dimdate'],

    }
    # cs = carousel.objects.all()
    return context
# @register.filter(name="isActive")
# def ClassActive(value):
#     prefix=value.split('/')
#     if len(prefix)>2:
#         if len(prefix) > 3:
#             if prefix[3] == 'group':
#                 return 'groups'
#             if prefix[3] == 'sys':
#                 return 'sysgroups'
#         else:
#             if prefix[2]=='mdl' or prefix[2]=='mdlfuncs':
#                 return 'app'
#             if prefix[2]=='content1':
#                 return 'content'
#         return prefix[2]
#     else:
#         return prefix[-1]
#     # return 'active'
#
@register.filter(name="carousel_imgs")
def Brflen(value):
    try:
        temp=value.all()[0]
        return temp.filepath+"|"+temp.title
    except:
        return '暂无'

@register.filter(name="user_avt")
def Brflen(value):
    try:
        temp = value.all()[0]
        return temp.filepath + "|" + temp.title
    except:
        return '暂无'

@register.filter(name ="spiltcontent")
def spiltcontent(value, arg):
    pattern = re.compile('<.+?>')
    value = pattern.sub('', value)
    p = re.compile('&.+?;')
    l = p.findall(value)
    for x in l:
        value = value.replace(x, ' ')
    return value[:arg] + '...' if len(value) > arg else value[:arg]

@register.filter(name="findstep")
def Brflen(value,arg):
    """

    :param value: flow
    :param arg: user
    :return:
    """
    try:
        allflow = arg.flow_set.all()
        if value in allflow:
            return True
        else:
            return False
    except:
        return False



#
# @register.filter(name="UserBanned")
# def Brflen(value):
#     return '禁用' if value==-1 else '正常'
#
#
# @register.filter(name="Brflen")
# def Brflen(value, arg):
#     return value[:arg] + '...' if len(value) > 10 else value[:arg]
#
# #分离组内组外用户
# @register.filter(name="groupusers")
# def groupusers(value,arg):
#     html=r"""
#     <table class="table table-bordered"><tr>
#     <td class="col-xs-2">组内用户:</td><td>
#
#     """
#
#     table1=my_custom_sql('SELECT id,usrflg FROM WUBI.core_user where core_user.id in (select usrid from core_usergrp where Cpngrpid =%s)',str(value))
#     for row in table1:
#         html+=r'<div class="col-xs-2" ><input id="user'+str(row[0])+'" type="checkbox"  value="'+str(row[0])+'" name="'+str(row[0])+'" checked="checked" ><span>'+str(row[1])+'</span></div> '
#
#     html += r'</td></tr><tr><td class="col-xs-2">组外用户:</td><td>'
#     if arg == 'SYS':
#         table2 = my_custom_sql('SELECT id,usrflg FROM WUBI.core_user where core_user.id not in (select usrid from core_usergrp where Cpngrpid =%s)',str(value))
#     else:
#         table2 = my_custom_sql(
#             'SELECT id,usrflg FROM WUBI.core_user where core_user.id not in (select usrid from core_usergrp where Cpngrpid =%s) and core_user.Cpnid =%s',
#             (str(value), str(arg)))
#     for row in table2:
#         html+=r'<div class="col-xs-2" ><input id="user'+str(row[0])+'" type="checkbox" name="'+str(row[0])+'"  value="'+str(row[0])+'"  ><span>'+str(row[1])+'</span></div>'
#     html+=r'</td></tr></table>'
#
#     return html
# #分离企业在系统组之下拥有的权限
# @register.filter(name="cpngroupauths")
# def groupusers(value,arg):
#     html=r"""
#     <table class="table table-bordered"><tr>
#     <td class="col-xs-2">已有权限:</td><td>
#
#     """
#     if arg=='SYS':
#         table1 = my_custom_sql(
#             'SELECT id,Name,(select Name from core_app where core_app.id=core_mdl.appid_id) as appname FROM WUBI.core_mdl where core_mdl.id  in ( select mdlid from core_cpngrppwr where core_cpngrppwr.Cpngrpid=%s)',value)
#     else:
#         table1=my_custom_sql('SELECT id,Name,(select Name from core_app where core_app.id=core_mdl.appid_id) as appname FROM WUBI.core_mdl where core_mdl.id in (select mdlid from core_sysgrppwr where grpid in ( select appgrp from core_apprgst where Cpnid_id = %s ) ) and core_mdl.id  in ( select mdlid from core_cpngrppwr where core_cpngrppwr.Cpngrpid=%s)',(str(arg),str(value)))
#     for row in table1:
#         html+=r'<div class="col-xs-2" ><input id="user'+str(row[0])+'" type="checkbox"  value="'+str(row[0])+'" name="mdl" checked="checked" ><span>'+row[2]+"--"+str(row[1])+'</span></div> '
#
#     html += r'</td></tr><tr><td class="col-xs-2">未有权限:</td><td>'
#     if arg == 'SYS':
#         table2 = my_custom_sql(
#             'SELECT id,Name,(select Name from core_app where core_app.id=core_mdl.appid_id) as appname FROM WUBI.core_mdl where core_mdl.id  not in ( select mdlid from core_cpngrppwr where core_cpngrppwr.Cpngrpid=%s)',
#             value)
#     else:
#         table2 = my_custom_sql('SELECT id,Name,(select Name from core_app where core_app.id=core_mdl.appid_id) as appname FROM WUBI.core_mdl where core_mdl.id in (select mdlid from core_sysgrppwr where grpid in ( select appgrp from core_apprgst where Cpnid_id = %s ) ) and core_mdl.id  not in ( select mdlid from core_cpngrppwr where core_cpngrppwr.Cpngrpid=%s)',(str(arg),str(value)))
#     for row in table2:
#         html+=r'<div class="col-xs-2" ><input id="user'+str(row[0])+'" type="checkbox" name="mdl"  value="'+str(row[0])+'"  ><span>'+row[2]+"--"+str(row[1])+'</span></div>'
#     html+=r'</td></tr></table>'
#
#     return html
#
# #分离组内企业,组外企业
# @register.filter(name="sysgroupusers")
# def groupusers(value):
#     html=r"""
#     <table class="table table-bordered"><tr>
#     <td class="col-xs-2">组内用户:</td><td>
#
#     """
#     table1=my_custom_sql('SELECT id,Name FROM WUBI.core_cpn where core_cpn.id in (select Cpnid_id from core_apprgst where appgrp =%s)',str(value))
#     for row in table1:
#         html+=r'<div class="col-xs-2" ><input id="user'+str(row[0])+'" type="checkbox"  value="'+str(row[0])+'" name="cpn" checked="checked" ><span>'+str(row[1])+'</span></div> '
#
#     html += r'</td></tr><tr><td class="col-xs-2">组外用户:</td><td>'
#
#     table2 = my_custom_sql(
#         'SELECT id,Name FROM WUBI.core_cpn where core_cpn.id not in (select Cpnid_id from  core_apprgst where appgrp =%s)',
#         str(value))
#     for row in table2:
#         html+=r'<div class="col-xs-2" ><input id="user'+str(row[0])+'" type="checkbox" name="cpn"  value="'+str(row[0])+'"  ><span>'+str(row[1])+'</span></div>'
#     html+=r'</td></tr></table>'
#
#     return html
#
#
# @register.filter(name="sysgroupauths")
# def groupusers(value,arg):
#     html=r"""
#     <table class="table table-bordered"><tr>
#     <td class="col-xs-2">已有权限:</td><td>
#
#     """
#     table1=my_custom_sql('SELECT id,Name FROM WUBI.core_mdl where core_mdl.id in (select mdlid from core_sysgrppwr where grpid =%s) and core_mdl.appid_id=%s',(str(value),arg))
#     for row in table1:
#         html+=r'<div class="col-xs-2" ><input id="user'+str(row[0])+'" type="checkbox"  value="'+str(row[0])+'" name="mdl" checked="checked" ><span>'+str(row[1])+'</span></div> '
#
#     html += r'</td></tr><tr><td class="col-xs-2">未有权限:</td><td>'
#
#     table2 = my_custom_sql(
#         'SELECT id,Name FROM WUBI.core_mdl where core_mdl.id not in (select mdlid from core_sysgrppwr where grpid =%s) and core_mdl.appid_id=%s',(str(value),arg))
#     for row in table2:
#         html+=r'<div class="col-xs-2" ><input id="user'+str(row[0])+'" type="checkbox" name="mdl"  value="'+str(row[0])+'"  ><span>'+str(row[1])+'</span></div>'
#     html+=r'</td></tr></table>'
#
#     return html
#
#
