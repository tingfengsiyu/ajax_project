from django.shortcuts import render,HttpResponse
from app01 import models
import json
# Create your views here.
def students(request):
    stu_list= models.Student.objects.all()
    cls_list = models.Classes.objects.all()
    return  render(request,'students.html',{'stu_list':stu_list,'cls_list':cls_list})


def add_students(request):
    print(request.POST)
    response = {'status':True,'message': None,'data':None}
    try:
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cls_id')
        obj = models.Student.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
        response['data'] = obj.id
    except Exception as e:
        response['status'] = False
        response['message'] = '用户输入错误'
        print(response['message'])
    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)

