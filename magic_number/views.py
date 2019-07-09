from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question

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
        'talent1': 3,
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
    }
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
    life_number, talent_number = get_magic_number_sum(birthday)
    celebrity = get_right_celebrity(life_number)
    if not celebrity:
        celebrity = celebrities["张欣"]
    context = {
        'life_number': life_number,
        'talent_number1': str(talent_number)[0],
        'talent_number2': str(talent_number)[1],
        'name': name,
        'cele_name': celebrity['name'],
        'pic_name': celebrity['img'],
        'desc': celebrity['title']}
    return render(request, 'magic_number/result.html', context)


def get_magic_number_sum(input_birthday):
    temp_sum = sum(int(i) for i in input_birthday)
    if temp_sum in [11, 22, 33]:
        return temp_sum, temp_sum
    return sum(int(i) for i in str(temp_sum)), temp_sum


def get_right_celebrity(life_number, talent_number1=-1, talent_number2=-1):
    for key, item in celebrities.items():
        print(item)
        if item['life'] == life_number:
            return item


