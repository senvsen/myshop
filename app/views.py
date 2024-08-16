from django.shortcuts import render

from django.http import HttpResponse      # 倒入HttpResponse模块
# Create your views here.
def index(request):                       # 定义视图函数
    return render(request,'1/index.html') # 将渲染结果输出到index,html模板中
