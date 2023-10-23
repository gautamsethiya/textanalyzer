
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyse(request):
    djtext =request.POST.get('text','default')
    removepunc =request.POST.get('removepunc','off')
    fullcase =request.POST.get('fullcase','off')
    new_line_remover =request.POST.get('new_line_remover','off')
    space_remover =request.POST.get('space_remover','off')
    characterCounter =request.POST.get('characterCounter','off')
    print(removepunc)
    print(djtext)

    if removepunc =="on":
        puctuations ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in puctuations:
                analyzed = analyzed+char
        djtext=analyzed
        params ={'purpose':'remove punctuations','analyszed_text':analyzed}
        
    if fullcase=="on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed+char.upper()
        djtext=analyzed
        params ={'purpose':'To uppercase','analyszed_text':analyzed}
        
    if new_line_remover =="on":
        analyzed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed =analyzed+char
        djtext=analyzed
        params ={'purpose':'remove new line','analyszed_text':analyzed}
        
    if space_remover =="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]==' ' and djtext[index+1]==' ':
                pass
            else:
                analyzed =analyzed+char
        params ={'purpose':'space remove','analyszed_text':analyzed}
        
    if characterCounter =="on":
        count =0
    
        for char in djtext:
            if char >= 'a' and char<='z'  or char>='A' and char<='z':
                count = count+1 
        analyzed = analyzed+" "+str(count)
        params ={'purpose':'character count','analyszed_text':analyzed}
        
    if djtext=="":
        return HttpResponse("Select what to do")
    return render(request,'analyse.html',params)
  