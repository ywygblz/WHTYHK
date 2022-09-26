import os


# 静态文件加载
def load_static():
    path = r'D:\0_BY_HUI_object\django_object\自用模版\链家项目\LJ\index\static'
    for i in os.walk(path):
        for j in i[2]:
            if '.js' in j or '.css' in j or '.jpg' in j or '.svg' in j:
                file = os.path.join(i[0], j)[59:]
                if '.js' in file:
                    text = '<script src="{% static \'' + file + '\' %}" type="text/javascript"></script>'.replace('\\','/')
                elif '.jpg' in file or '.svg' in file:
                    text = 'src="{% static \'' + file + '\' %}"'.replace('\\', '/')
                else:
                    text = '<link rel="stylesheet" href="{% static \'' + file + '\' %}">'.replace('\\', '/')
                print(text)


def load_index():
    html_demo = '''
        <li class="nav-item">
            <a class="nav-link collapsed" data-bs-toggle="collapse" href="#ui-basic" aria-expanded="false" aria-controls="ui-basic">
                <i class="mdi mdi-circle-outline menu-icon"></i>
                <span class="menu-title">UI Elements</span>
                <i class="menu-arrow"></i>
            </a>
            <div class="collapse" id="ui-basic" style="">
                <ul class="nav flex-column sub-menu">
                    <li class="nav-item"><a class="nav-link" href="pages/ui-features/buttons.html">Buttons</a></li>
                    <li class="nav-item"><a class="nav-link" href="pages/ui-features/typography.html">Typography</a></li>
                </ul>
            </div>
        </li>
    '''
    index_ls = {
        '公告': ['公告管理'],
        '航司账号': ['航司账号'],
        '订单管理': ["订单待处理", "订单列表", "刷单列表"],
        '退票与改期': ["退票待处理", "退票列表", "改期待处理", "改期列表", "改期管理"],
        '航变推送': ['QT数据', '航变原始数据', '航变数据'],
        '优惠卷管理': ['优惠卷-国航'],
        "数据管理": ["航管分销", "八千翼", "今通国际", "蜗牛商旅", "易旅行", "易旅行列表", '京东'],
        '联系方式管理': ['联系方式'],
        '个人信息': ['个人信息', '修改密码']
    }
    index_dt = {
        '主页': [{'mdi mdi-home menu-icon': []}, '#'],
        '公告': [{'mdi mdi-home menu-icon': []}, '#'],
        '航司账号': [{'mdi mdi-view-headline menu-icon': [{'航司账号': 'airline_user'}]}, 'airline_user'],
        '订单管理': [{'mdi mdi-view-headline menu-icon': [{'订单待处理': '#'}, {'订单列表': '#'},{'刷单列表': '#'}]}, 'bench-2'],
        '退票与改期': [{'mdi mdi-view-headline menu-icon': [{'退票待处理': '#'}, {'退票列表': '#'}, {'改期待处理': '#'}, {'改期列表': '#'}, {'改期管理': '#'}]}, 'bench-3'],
        '航变推送': [{'mdi mdi-view-headline menu-icon': [{'QT数据': '#'}, {'航变原始数据': '#'}, {'航变数据': '#'}]}, 'bench-4'],
        '优惠卷管理': [{'mdi mdi-view-headline menu-icon': [{'优惠卷-国航': '#'}]}, 'bench-5'],
        '数据管理': [{'mdi mdi-view-headline menu-icon': [{'航管分销': '#'}, {'八千翼': '#'}, {'今通国际': '#'}, {'蜗牛商旅': '#'},
                                                       {'易旅行': '#'}, {'易旅行列表': '#'}, {'京东': '#'}]}, 'bench-6'],
        '联系方式管理': [{'mdi mdi-view-headline menu-icon': [{'联系方式': '#'}]}, 'bench-7'],
        '个人信息': [{'mdi mdi-account menu-icon': [{'基本信息': 'index'},{'基本信息': '修改密码'}]}, 'user'],
    }
    html = ''
    for index in index_dt.keys():
        Id = index_dt[index][1]
        # print(index, Id)
        html += f'<li class="nav-item"> <a class="nav-link collapsed" data-bs-toggle="collapse" href="#{Id}" aria-expanded="false" aria-controls="{Id}">'
        for class_name in index_dt[index][0]:
            # print(class_name)
            html += f'''
            <i class="{class_name}"></i>
                <span class="menu-title">{index}</span>
                <i class="menu-arrow"></i>
            </a>
            <div class="collapse" id="{Id}" style="">
                <ul class="nav flex-column sub-menu">
            '''
            for item in index_dt[index][0][class_name]:
                item_name, href = list(item.items())[0]
                html += f'''
                <li class="nav-item" name="{href}"><a class="nav-link" href="#">{item_name}</a></li>
                '''
                # print(item_name, href)
            html += '''</ul></div>'''
        # break
        html += '</li>'
    print(html)



def from_input():
    html_demo = ''

def demo3():
    ls_1 = {
    "1": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18017768588\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t19830807\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-15 16:23:44\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-28 10:35:30\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(APP)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "2": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18607101006\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t00781208\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-15 16:23:21\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-30 11:29:27\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(APP)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "3": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t660280287991\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t19781208\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-11 15:58:45\n\t\t\t\t",
        "\n\t\t\t\t\t2021-03-09 12:35:00\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "4": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18602750005\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t11223344\n\t\t\t\t",
        "\n\t\t\t\t\t2021-03-25 10:48:48\n\t\t\t\t",
        "\n\t\t\t\t\t2021-03-25 10:48:48\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "5": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18607101006\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tTY781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-03-29 12:24:38\n\t\t\t\t",
        "\n\t\t\t\t\t2021-04-24 18:40:44\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t厦门航空MF(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "6": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18607139000\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t781208\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-22 14:38:16\n\t\t\t\t",
        "\n\t\t\t\t\t2021-05-26 17:08:58\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(APP)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "7": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t13387554248\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-22 14:39:25\n\t\t\t\t",
        "\n\t\t\t\t\t2021-07-30 10:43:17\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(APP)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "8": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tm18672947998\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-07-30 16:49:46\n\t\t\t\t",
        "\n\t\t\t\t\t2021-07-30 16:49:46\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(APP)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "9": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t13972724553\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-22 14:39:45\n\t\t\t\t",
        "\n\t\t\t\t\t2021-07-30 16:57:12\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(APP)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "10": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t604010265138\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t19781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-01-15 13:54:41\n\t\t\t\t",
        "\n\t\t\t\t\t2021-07-31 11:33:41\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "11": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18017768588\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-04-26 09:40:07\n\t\t\t\t",
        "\n\t\t\t\t\t2021-08-17 16:00:35\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t厦门航空MF(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "12": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t15927367719\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-04-26 09:34:29\n\t\t\t\t",
        "\n\t\t\t\t\t2021-08-17 16:43:11\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t厦门航空MF(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "13": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t13972724553\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tyl199333\n\t\t\t\t",
        "\n\t\t\t\t\t2021-03-29 12:24:15\n\t\t\t\t",
        "\n\t\t\t\t\t2021-08-23 09:29:30\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t厦门航空MF(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "14": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18672947998\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-03-29 12:19:03\n\t\t\t\t",
        "\n\t\t\t\t\t2021-08-31 10:35:11\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t厦门航空MF(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "15": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18507147025\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-04-02 17:25:45\n\t\t\t\t",
        "\n\t\t\t\t\t2021-09-01 19:06:01\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t厦门航空MF(官网)\n\t\t\t\t",
        "\n\t\t\t\t\twhty001\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "16": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18507147025\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-07-30 17:15:36\n\t\t\t\t",
        "\n\t\t\t\t\t2021-09-04 12:20:35\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(APP)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "17": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t15827571663\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-08-01 11:50:26\n\t\t\t\t",
        "\n\t\t\t\t\t2021-09-04 16:18:54\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(APP)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "18": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18607101006\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-22 11:25:22\n\t\t\t\t",
        "\n\t\t\t\t\t2021-09-05 10:19:42\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(APP)\n\t\t\t\t",
        "\n\t\t\t\t\tsystem\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "19": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18672947998\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-07-30 16:55:44\n\t\t\t\t",
        "\n\t\t\t\t\t2021-09-05 14:09:30\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(APP)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "20": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\txl18017768588\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-09-06 16:04:10\n\t\t\t\t",
        "\n\t\t\t\t\t2021-09-06 16:04:10\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "21": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\twhtyjt\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tba88834f2dbd84bf4a18dbacf962b749\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-07 17:47:11\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-07 17:47:11\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t今通国际接口\n\t\t\t\t",
        "\n\t\t\t\t\tadmin\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "22": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\twhtyjt\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!Ty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-07 17:07:07\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-10 11:37:50\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t今通国际\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "23": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18507141025\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-21 11:06:00\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-21 11:06:00\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t国航CA(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t杨丽\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "24": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t13972724553\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-21 11:06:23\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-21 11:06:23\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t国航CA(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t杨丽\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "25": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18672947998\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-21 11:06:39\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-21 11:06:39\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t国航CA(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t杨丽\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "26": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18607139000\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-21 11:12:49\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-21 11:12:49\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t国航CA(APP)\n\t\t\t\t",
        "\n\t\t\t\t\twhty001\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "27": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18602750009\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t11223344\n\t\t\t\t",
        "\n\t\t\t\t\t2021-03-25 10:48:29\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-21 11:13:04\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\twhty001\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "28": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18607139000\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-21 11:06:59\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-22 09:46:56\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t国航CA(APP)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "29": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18672947998\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-21 11:24:40\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-22 09:59:48\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t国航CA(APP)\n\t\t\t\t",
        "\n\t\t\t\t\twhty001\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "30": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t13972724553\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-21 11:24:57\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-22 10:06:01\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t国航CA(APP)\n\t\t\t\t",
        "\n\t\t\t\t\twhty001\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ]
}
    ls_2 = {
    "1": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18507147025\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-21 11:25:14\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-23 09:50:36\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t国航CA(APP)\n\t\t\t\t",
        "\n\t\t\t\t\twhty001\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "2": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tbj9003\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t@TYty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-29 11:45:55\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-29 11:45:55\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(B2T)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "3": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tbj9002\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t@TYty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-29 11:46:09\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-29 11:46:09\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(B2T)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "4": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18507147025\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t781208\n\t\t\t\t",
        "\n\t\t\t\t\t2022-02-08 13:50:08\n\t\t\t\t",
        "\n\t\t\t\t\t2022-02-08 13:50:08\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t海南航空HU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\ttestwu\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "5": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18607101006\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t781208\n\t\t\t\t",
        "\n\t\t\t\t\t2022-02-08 13:50:54\n\t\t\t\t",
        "\n\t\t\t\t\t2022-02-08 13:50:54\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t海南航空HU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\ttestwu\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "6": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t9BA51E10800D4E1995E5B20A1566C2DD\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tfa708b7252c0c2bf\n\t\t\t\t",
        "\n\t\t\t\t\t2022-02-11 10:19:13\n\t\t\t\t",
        "\n\t\t\t\t\t2022-02-11 10:19:13\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t易旅行\n\t\t\t\t",
        "\n\t\t\t\t\tadmin\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "7": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWUH28802\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@ty781208@@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-02-14 15:06:09\n\t\t\t\t",
        "\n\t\t\t\t\t2022-02-14 15:06:09\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t易旅行\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "8": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t15827571663\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty802525\n\t\t\t\t",
        "\n\t\t\t\t\t2021-04-02 17:26:09\n\t\t\t\t",
        "\n\t\t\t\t\t2022-02-25 09:22:01\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t厦门航空MF(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "9": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\twuh288\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@ty781208@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-03-24 15:46:48\n\t\t\t\t",
        "\n\t\t\t\t\t2022-03-24 15:46:48\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t海南航空HU(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "10": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tYP10011424375\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t44BD4BD159AC496595390A3BF2A603D6\n\t\t\t\t",
        "\n\t\t\t\t\t2022-03-30 16:17:56\n\t\t\t\t",
        "\n\t\t\t\t\t2022-03-30 16:17:56\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tNDC\n\t\t\t\t",
        "\n\t\t\t\t\tadmin\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "11": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWHTY005\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@#Ty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2022-04-11 16:33:26\n\t\t\t\t",
        "\n\t\t\t\t\t2022-04-11 18:31:47\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t深圳航空ZH(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "12": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWUHTY\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t0cbc4b11-5a8f-42b9-a2a6-8008fc80bb10\n\t\t\t\t",
        "\n\t\t\t\t\t2022-05-18 15:30:16\n\t\t\t\t",
        "\n\t\t\t\t\t2022-05-18 15:30:16\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t胤之旅\n\t\t\t\t",
        "\n\t\t\t\t\t管理员\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "13": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWUH_TY\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@ty781208@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-03-29 16:01:48\n\t\t\t\t",
        "\n\t\t\t\t\t2022-06-18 19:31:45\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t厦门航空MF(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "14": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tTY001\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@ty781208@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-03-29 17:11:34\n\t\t\t\t",
        "\n\t\t\t\t\t2022-07-04 09:07:47\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t成都航空EU(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "15": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\twuh288\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@ty781208@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-04-07 16:41:23\n\t\t\t\t",
        "\n\t\t\t\t\t2022-07-13 09:27:21\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t河北航空NS(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "16": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tty7001\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t@TYty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-29 11:46:47\n\t\t\t\t",
        "\n\t\t\t\t\t2022-07-19 20:09:50\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(B2T)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "17": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tbj9005\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t@TYty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-29 11:44:04\n\t\t\t\t",
        "\n\t\t\t\t\t2022-07-19 20:09:53\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(B2T)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "18": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWUH0017\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tcz781208!@#\n\t\t\t\t",
        "\n\t\t\t\t\t2022-03-28 16:01:41\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-01 19:20:50\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t南方航空CZ(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "19": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tm18607101006\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-09-01 17:30:57\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-04 12:26:23\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t赵梅枝\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "20": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tTY200528\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@ty781208@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-03-24 14:41:50\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-07 17:31:55\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t吉祥航空HO(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "21": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tf0edcef6877c4c62799b7a4a1a778711\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tc3b63850214f3bd031566e2b1d2c8595\n\t\t\t\t",
        "\n\t\t\t\t\t2022-03-25 15:16:31\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-17 10:01:37\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t蜗牛商旅\n\t\t\t\t",
        "\n\t\t\t\t\tadmin\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "22": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\txl18017768588\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-09-06 16:04:54\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-22 13:42:40\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t赵梅枝\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "23": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18607101006\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t00781208\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-11 15:59:02\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-23 12:25:40\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t罗慕莹\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "24": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18668202068\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t75825812\n\t\t\t\t",
        "\n\t\t\t\t\t2021-01-09 00:48:27\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-23 14:29:22\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t罗慕莹\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "25": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18017768588\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t00830807\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-11 15:59:20\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-23 16:56:14\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t罗慕莹\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "26": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tm18672947998\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-09-06 16:07:26\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-25 11:10:30\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t赵梅枝\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "27": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t18672947998\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t12332112\n\t\t\t\t",
        "\n\t\t\t\t\t2021-03-09 00:59:16\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-26 11:39:41\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t罗慕莹\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "28": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tm18607139000\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-09-06 16:00:31\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-26 14:20:05\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t赵梅枝\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "29": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t13419601197\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t19781208\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-22 16:18:56\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-26 16:27:45\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t罗慕莹\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "30": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t663011981375\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t00781208\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-22 16:19:28\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-27 08:45:10\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t罗慕莹\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ]
}
    ls_3 = {
    "1": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWUH288\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@ty781208@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-02-14 16:22:13\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-29 13:02:31\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t四川航空3U(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "2": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t15827571663\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t80258025\n\t\t\t\t",
        "\n\t\t\t\t\t2021-01-15 13:53:57\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-29 13:05:43\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t罗慕莹\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "3": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\t13972724553\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t70017001\n\t\t\t\t",
        "\n\t\t\t\t\t2020-12-22 16:19:41\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-09 09:13:44\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(官网)\n\t\t\t\t",
        "\n\t\t\t\t\t罗慕莹\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "4": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWUH288\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@ty781208@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-14 14:52:01\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-16 18:06:06\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t长龙航空GJ(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "5": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWHTY05\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!ty781208@@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-15 12:24:06\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-16 18:37:29\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t账户未开通\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "6": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\twuh288\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@ty781208@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-03-24 15:48:28\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-17 10:42:46\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "7": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWHTY01\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!ty781208@@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-08-03 16:45:22\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-17 12:01:29\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t赵梅枝\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "8": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWHTY04\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!ty781208@@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-15 12:23:46\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-17 12:05:14\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t赵梅枝\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "9": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tYP10011424375\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t44BD4BD159AC496595390A3BF2A603D6\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-14 16:37:08\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-19 12:26:07\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t易宝B2B\n\t\t\t\t",
        "\n\t\t\t\t\t管理员\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "10": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWHTY03\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!ty781208@@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-08 16:08:06\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-19 13:05:16\n\t\t\t\t",
        "\n\t\t\t\t\t停止使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t赵梅枝\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "11": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tbj9004\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t@TYty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-29 11:45:23\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-19 20:18:19\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(B2T)\n\t\t\t\t",
        "\n\t\t\t\t\twhty001\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "12": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWUH288G5\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@ty781208@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-05-30 15:52:30\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-19 21:59:17\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t华夏航空G5(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "13": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWUH288001\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\tWUH288001\n\t\t\t\t",
        "\n\t\t\t\t\t2022-07-25 11:02:02\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-19 22:54:17\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t管理员\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "14": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tbj9001\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t@TYty781208\n\t\t\t\t",
        "\n\t\t\t\t\t2021-12-29 11:46:28\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-20 18:02:32\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t东方航空MU(B2T)\n\t\t\t\t",
        "\n\t\t\t\t\twhty001\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "15": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWHTY1\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@ty781208@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-14 14:52:30\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-21 11:18:47\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t长龙航空GJ(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "16": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWHTY3\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@ty781208@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-03-30 14:02:28\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-21 11:18:47\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t长龙航空GJ(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "17": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWHTY04\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!ty781208@@\n\t\t\t\t",
        "\n\t\t\t\t\t2022-06-17 13:52:17\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-21 13:15:40\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t青岛航空QW(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t武汉天宇\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "18": [
        "\n\t\t\t\t\t\n\t\t\t\t\t\tWHTYHK\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t!@#ty333666\n\t\t\t\t",
        "\n\t\t\t\t\t2022-07-25 09:51:03\n\t\t\t\t",
        "\n\t\t\t\t\t2022-09-21 16:19:15\n\t\t\t\t",
        "\n\t\t\t\t\t未使用\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t\n\t\t\t\t",
        "\n\t\t\t\t\t山东航空SC(B2B)\n\t\t\t\t",
        "\n\t\t\t\t\t赵梅枝\n\t\t\t\t",
        "\n    \t\t\t\t启用\n    \t\t\t\t停用\n\t\t\t\t"
    ],
    "19": [],
    "20": [],
    "21": [],
    "22": [],
    "23": [],
    "24": [],
    "25": [],
    "26": [],
    "27": [],
    "28": [],
    "29": [],
    "30": []
}
    new_ls = []
    for ls in [ls_1,ls_2,ls_3]:
        for item in ls.values():
            temp_ls = []
            for i in item:
                temp_ls.append(i.replace('\n','').replace('\t',''))
            if temp_ls:
                j = temp_ls[:9]
                # print(j)
                sql = f'''insert into index_airlineuser values (0,'{j[0]}','{j[1]}','{j[2]}','{j[3]}','{j[4]}','{j[5]}','{j[6]}','{j[7]}','{j[8]}');'''
                print(sql)
                new_ls.append(j)
    # print(new_ls)


if __name__ == '__main__':
    # load_index()
    # load_static()
    demo3()
