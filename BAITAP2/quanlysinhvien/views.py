# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import SinhVien
from django.http import JsonResponse
from .forms import RegisterForm
# Create your views here.


def index(request):
    template = loader.get_template('quanlysinhvien/index.html')
    return HttpResponse(template.render())


def register(request):
    if request.method == "POST":
        hoten = request.POST.get('hoten',False)
        masv = request.POST.get('masv',False)
        nganhhoc = request.POST.get('nganhhoc',False)
        sv = SinhVien(hoten=hoten,masv=masv,nganhhoc=nganhhoc)
        sv.save()
        all_sv = SinhVien.objects.all()
        return render(request, 'quanlysinhvien/showlist.html', {'all_sv': all_sv})
    registerForm = RegisterForm()
    return render(request,'quanlysinhvien/register.html',{'form':registerForm})



def showlist(request):
    if request.method == 'POST':
        if request.POST.get('submit',False) == 'tositeADD':
            registerForm = RegisterForm()
            return render(request,'quanlysinhvien/register.html',{'form':registerForm})
        elif request.POST.get('submit',False) == 'Submit':
            register(request)
            print 'vao'
        else:
            masv =  request.POST.get('masv',False)  
            print  masv
            SinhVien.objects.filter(masv=masv).delete()
            response = HttpResponse()
            response.write('thanhcong')
            return response
    all_sv = SinhVien.objects.all()
    return render(request, 'quanlysinhvien/showlist.html', {'all_sv': all_sv})
