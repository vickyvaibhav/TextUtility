#file created by Vaibhav

from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render


def personalNavigator(request):
    return HttpResponse('''
        <h1>Personal Navigator</h1>
        <br><br>
        <a href="https://vickyvaibhav.github.io"> Know Me</a>
        <br><br>
        <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">
                Django Playlist</a>
        <br><br>
        <a href="https://www.youtube.com/channel/UCeC088dyJsXK_L1bCHZDcjA"> Visit My Youtube Channel</a>
        <br><br>
        <h2>Thanks For Visiting...</h2>    
    ''')


#this method will check the index.html in the templates folder, called from urls.py

def index(request):  
    params = {'title':'This is Text Utility Site','name':'Vaibhav Agrawal'}
    return render(request,'index.html',params)

#this method is to analyse the text
def analysetext(request):
    
    getText = request.POST.get('textarea','no text written')
    removepunc = request.POST.get('removepunc','off') 
    allcapitalize = request.POST.get('allcapitalize','off') 
    extraspaceremover = request.POST.get('extraspaceremover','off') 
    charcount = request.POST.get('charcount','off') 
    newlineremover = request.POST.get('newlineremover','off') 

    analyzedText = ""
    count = 0
    if(removepunc == "on"):
        count+=1
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in getText:
            if char not in punctuations:
                analyzedText = analyzedText+char

        params = {'operation':'Remove Punctuation','analyzed_text':analyzedText}       
        getText = analyzedText

    if(allcapitalize == "on"):
        count+=1
        analyzedText = ""
        for char in getText:
            analyzedText = analyzedText+char.upper()
        params = {'operation':'Capitalize all characters','analyzed_text':analyzedText}        
        getText = analyzedText
   
    if(extraspaceremover == "on"):
        count+=1
        analyzedText = ""
        for index, char in enumerate(getText):
            if not(getText[index]==" " and getText[index+1]==" "):
                analyzedText = analyzedText+char    
        params = {'operation':'Remove Extra Spaces','analyzed_text':analyzedText}        
        getText = analyzedText

    if(newlineremover == "on"):
        count+=1
        analyzedText = ""
        for char in getText:
            if char != "\n" and char != "\r":
                analyzedText = analyzedText+char  
        params = {'operation':'Remove New Lines','analyzed_text':analyzedText}        
        getText = analyzedText
        
    if(charcount == "on"):
        count+=1
        analyzedText = ""
        analyzedText = len(getText)    
        params = {'operation':'Count the characters','analyzed_text':analyzedText}        
        getText = analyzedText
       
    if(removepunc != "on" and allcapitalize != "on" and extraspaceremover != "on" and 
    charcount != "on" and newlineremover != "on"):
        analyzedText = getText
        params = {'operation':'Nothing','checkboxSelection':'You have not selected any operation','analyzed_text':analyzedText}
        return render(request,'analyse.html',params)
    if(count>1):
        params = {'operation':'Multiple Operations Performed','analyzed_text':analyzedText}        
        return render(request,'analyse.html',params)
    else:
        return render(request,'analyse.html',params)
        