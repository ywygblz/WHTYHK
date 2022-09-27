from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from index.models import AirlineUser
from django.core.paginator import Paginator, Page


def paging(data_list, num: int, per_page=20):
    """分页"""
    paginator = Paginator(data_list, per_page)
    data_count = paginator.count  # 数据总数
    num_pages = paginator.num_pages  # 总页数
    # page_ls = paginator.page_range  # 页码的列表
    data = paginator.page(num)
    data_ls = []
    for item in data:
        print(dir(item))
        Id = item.id
        name = item.name
        password = item.password
        create_time = item.create_time
        update_time = item.update_time
        state = item.state
        remark = item.remark
        proxy = item.proxy
        source = item.source
        admin = item.admin
        data_ls.append([Id,name, password, create_time, update_time, state, remark,proxy,source,admin])
    return data_count ,num_pages ,data_ls


def index(request):
    return render(request, "index.html")


def base(request):
    return render(request, "base.html")

class Airline_User(View):
    """航司帐号"""

    def get(self, request, *args, **kwargs):
        params = request.GET.dict()
        page = params.get("page") or 1
        user = AirlineUser.objects.filter().all()
        data_count, num_pages, data_ls = paging(user,page)
        re_dt = {'user_ls': data_ls}
        return render(request, 'airline_user.html', re_dt)

    def post(self, request):
        mode = request.POST.get('mode')
        print(mode)
        mode_func = {
            'add': self.add,
            'delete': self.delete,
            'alter': self.alter,
            'query': self.query
        }
        return mode_func[mode](request)

    def add(self, request, *args, **kwargs):
        """增"""
        data = request.POST.dict()
        print(data)

        au = AirlineUser(
            name=data['name'],
            password=data['password'],
            proxy=data['proxy'],
            state=data['state'],
            source=data['source'],
            remark=data['remark'],
            admin='武汉天宇'
        )
        au.save()
        result = {"message": "200", 'type': 'add', 'data': '成功添加'}
        return JsonResponse(result)

    def delete(self, request, *args, **kwargs):
        """删"""
        data = request.POST.dict()
        del data['mode']
        name_pwd_ls = data.values()
        for item in name_pwd_ls:
            name_pwd_source = item.split('--')
            AirlineUser.objects.filter(name=name_pwd_source[0], password=name_pwd_source[1],
                                       source=name_pwd_source[2]).delete()
        result = {"message": "200", 'type': 'delete', 'data': '删除成功'}
        return JsonResponse(result)

    def alter(self, request, *args, **kwargs):
        """改"""
        data = request.POST.dict()
        state_key = data['key']
        state = {'open': '正在使用', 'close': '停止使用'}
        del data['mode'], data['key']
        name_pwd_ls = data.values()
        print(name_pwd_ls)
        for item in name_pwd_ls:
            name_pwd_source = item.split('--')
            AirlineUser.objects.filter(name=name_pwd_source[0], password=name_pwd_source[1],
                                       source=name_pwd_source[2]).update(state=state[state_key])
            print(state[state_key], state, name_pwd_source)
        result = {"message": "200", 'type': 'alter', 'data': '修改成功'}
        return JsonResponse(result)

    def query(self, request, *args, **kwargs):
        """查"""
        data = request.POST.dict()
        del data['mode']
        # {'mode': 'query', 'user': '', 'password': '', 'admin': '', 'start': '', 'source': ''}.keys()
        # keys = ['user', 'password', 'admin', 'start', 'source']
        q_dt = {}
        [q_dt.update({key: data[key]}) if data[key] != '' else ... for key in data]
        info = AirlineUser.objects.filter(**q_dt)  # 过滤字典中的查询条件
        info_data = list(info.values_list())
        result = {"message": "200", 'type': 'query', "data": info_data}
        return JsonResponse(result)
