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
        #对象id
    except Exception as e:
        response['status'] = False
        response['message'] = '用户输入错误'
        print(response['message'])
    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)

def del_student(request):
    ret = {'status':True}
    try:
        nid = request.GET.get('nid')
        models.Student.objects.filter(id=nid).delete()
    except Exception as e:
        ret['status'] = False
    return HttpResponse(json.dumps(ret))

def edit_student(request):
    response={'code':1000,'message':None}
    try:
        nid= request.POST.get('nid')
        user = request.POST.get('user')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cls_id = request.POST.get('cls_id')
        models.Student.objects.filter(id=nid).update(
            username=user,
            age=age,
            gender=gender,
            cs_id=cls_id
        )
    except Exception as e:
        response['code']=10001
        response['message']=str(e)
    return HttpResponse(json.dumps(response))

def test_ajax_list(request):
    print(request.POST.getlist('k2')) #获取字典中k2的值
    return HttpResponse('000000')