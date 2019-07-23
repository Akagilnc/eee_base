from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question
from random import randint

celebrities = {
    'Sheryl Sandberg': {
        'name': 'Sheryl Sandberg',
        'title': 'Facebook 首席运营官',
        'img': 'sandberg.jpg',
        'life': 5,
        'talent1': 4,
        'talent2': 1
    },
    'Gina Hope Rinehart': {
        'name': 'Gina Hope Rinehart',
        'title': '澳大利亚矿业大亨 - 汉考克探矿',
        'img': 'gina.jpg',
        'life': 3,
        'talent1': 3
    },
    'Abigail Johnson': {
        'name': 'Abigail Johnson',
        'title': '美国金融界最有实力的女性',
        'img': 'abigail.jpg',
        'life': 3,
        'talent1': 3
    },
    'Laurene Powell': {
        'name': 'Laurene Powell',
        'title': '爱默生基金会 创始人&主席',
        'img': 'laurene.jpg',
        'life': 9,
        'talent1': 2,
        'talent2': 7
    },
    'Susanne Klatten': {
        'name': 'Susanne Klatten',
        'title': '藏在幕后的女决策者 阿尔塔纳&宝马汽车',
        'img': 'susanne.jpg',
        'life': 5,
        'talent1': 3,
        'talent2': 2
    },
    'Jacqueline Mars': {
        'name': 'Jacqueline Mars',
        'title': '知名糖果巨头玛氏公司的女继承人',
        'img': 'jacqueline.jpg',
        'life': 6,
        'talent1': 2,
        'talent2': 4
    },
    '杨惠妍': {
        'name': '杨惠妍',
        'title': '碧桂园董事局 副主席',
        'img': 'yanghuiyan.jpg',
        'life': 1,
        'talent1': 2,
        'talent2': 8
    },
    'Alice Walton': {
        'name': 'Alice Walton',
        'title': '沃尔玛创始人山姆·沃尔顿长女',
        'img': 'alice.jpg',
        'life': 4,
        'talent1': 3,
        'talent2': 1
    },
    '张欣': {
        'name': '张欣',
        'title': 'SOHO中国首席执行官、联合创始人',
        'img': 'zhangxin.jpg',
        'life': 8,
        'talent1': 3,
        'talent2': 5
    },
    '史晓燕': {
        'name': '史晓燕',
        'title': '北京伊力诺依投资有限公司法人&董事长',
        'img': 'shixiaoyan.jpg',
        'life': 11,
        'talent1': 2,
        'talent2': 9
    },
    '林晓芸': {
        'name': '林晓芸',
        'title': '中鑫金业集团董事局主席&董事长',
        'img': 'linxiaoyun.jpg',
        'life': 5,
        'talent1': 4,
        'talent2': 1
    },
    '潘楚颖': {
        'name': '潘楚颖',
        'title': 'PYE品牌首席品牌官，溢达集团中国零售部',
        'img': 'panchuyin.jpg',
        'life': 7,
        'talent1': 4,
        'talent2': 3
    },
    '宗馥莉': {
        'name': '宗馥莉',
        'title': '宏胜饮料集团总裁、浙江省商会副会长',
        'img': 'zongfuli.jpg',
        'life': 9,
        'talent1': 2,
        'talent2': 7
    },
    '董明珠': {
        'name': '董明珠',
        'title': '珠海格力电器电器股份有限公司董事长',
        'img': 'dongmingzhu.jpg',
        'life': 3,
        'talent1': 3
    },
    '杨澜': {
        'name': '杨澜',
        'title': '阳光文化影视公司董事局主席',
        'img': 'yanglan.jpg',
        'life': 4,
        'talent1': 3,
        'talent2': 1
    },
    '翟美卿': {
        'name': '翟美卿',
        'title': '香港集团有限公司总裁',
        'img': 'cuimeiqin.jpg',
        'life': 9,
        'talent1': 2,
        'talent2': 7
    },
    '张玉珊': {
        'name': '张玉珊',
        'title': '修身堂控股有限公司主席',
        'img': 'zhangyushan.jpg',
        'life': 4,
        'talent1': 3,
        'talent2': 1
    },
    '陈金霞': {
        'name': '陈金霞',
        'title': '上海汇能投资管理公司执行董事',
        'img': 'chenjinxia.jpg',
        'life': 1,
        'talent1': 3,
        'talent2': 7
    },
    '尹索微': {
        'name': '尹索微',
        'title': '重庆力帆集团董事',
        'img': 'yisuowei.jpg',
        'life': 5,
        'talent1': 1,
        'talent2': 4
    },
    '董思阳': {
        'name': '董思阳',
        'title': '上海金柯天烨股权投资管理有限公司总裁',
        'img': 'dongsiyang.jpg',
        'life': 6,
        'talent1': 3,
        'talent2': 3
    },
    '张馨之': {
        'name': '张馨之',
        'title': '来福掌柜创始人',
        'img': 'zhangxinzhi.jpg',
        'life': 5,
        'talent1': 3,
        'talent2': 2
    },
    '尹峰': {
        'name': '尹峰',
        'title': '香港国际翼咖啡美食传播有限公司董事',
        'img': 'yifeng.jpg',
        'life': 5,
        'talent1': 3,
        'talent2': 2
    },
    '杨思维': {
        'name': '杨思维',
        'title': '壹心娱乐创始合伙人',
        'img': 'yangsiwei.jpg',
        'life': 9,
        'talent1': 2,
        'talent2': 7
    },
    '李静': {
        'name': '李静',
        'title': '乐蜂网创始人',
        'img': 'lijing.jpg',
        'life': 9,
        'talent1': 2,
        'talent2': 7
    },
    '张兰': {
        'name': '张兰',
        'title': '俏江南集团董事长',
        'img': 'zhanglan.jpg',
        'life': 7,
        'talent1': 3,
        'talent2': 4
    },
    '何超琼': {
        'name': '何超琼',
        'title': '美高梅中国主席、信德集团行政主席兼董事总经理',
        'img': 'hechaoqiong.jpg',
        'life': 7,
        'talent1': 3,
        'talent2': 4
    },
}


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'magic_number/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'magic_number/details.html', {'question': question})


def results(request, question_id):
    birthday, name = request.POST['birthday'], request.POST['name']
    birthday = birthday.replace('-', '')
    life_number, talent_number1, talent_number2 = get_magic_number_sum(birthday)
    celebrity = get_right_celebrity(life_number)
    if not celebrity:
        celebrity = celebrities["张欣"]

    cele_talent_1, cele_talent_2 = get_cele_talent(celebrity)
    talent_number1, talent_number2 = get_talent_numbers(cele_talent_1, cele_talent_2,
                                                        talent_number1, talent_number2)
    similarity = get_similarity(talent_number1, talent_number2)
    context = {
        'life_number': life_number,
        'talent_number1': talent_number1,
        'talent_number2': talent_number2,
        'name': name,
        'cele_name': celebrity['name'],
        'pic_name': celebrity['img'],
        'desc': celebrity['title'],
        'similarity': similarity}
    return render(request, 'magic_number/result.html', context)


def get_cele_talent(celebrity):
    cele_talent_1 = celebrity['talent1']
    cele_talent_2 = celebrity['talent2'] if 'talent2' in celebrity.keys() else -1
    return cele_talent_1, cele_talent_2


def get_talent_numbers(cele_talent_1, cele_talent_2, talent_number1, talent_number2):
    if talent_number1 != cele_talent_1 and talent_number1 != cele_talent_2:
        talent_number1 = None
    if talent_number2 != cele_talent_1 and talent_number2 != cele_talent_2:
        talent_number2 = None
    if talent_number2 and not talent_number1:
        talent_number1, talent_number2 = talent_number2, None
    return talent_number1, talent_number2


def get_similarity(talent_number1, talent_number2):
    similarity = 50
    if talent_number1:
        similarity += 25
    if talent_number2:
        similarity += 25
    return similarity


def get_magic_number_sum(input_birthday):
    temp_sum = sum(int(i) for i in input_birthday)
    if temp_sum in [11, 22, 33]:
        return temp_sum, str(temp_sum)[0], str(temp_sum)[1]
    talent_number1, talent_number2 = str(temp_sum)[0], str(temp_sum)[1]
    return sum(int(i) for i in str(temp_sum)), int(talent_number1), int(talent_number2)


def get_right_celebrity(life_number, talent_number1=-1, talent_number2=-1):
    cele_temp_list = []
    for key, item in celebrities.items():
        if item['life'] == life_number:
            cele_temp_list.append(item)

    length = len(cele_temp_list)
    return cele_temp_list[randint(0, length - 1)] if length > 0 else None
