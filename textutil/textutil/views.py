# I Have created this File - Neelesh

from django.http import HttpResponse
from django.shortcuts import render


# In home page , it contains links to all pipelines in buttons123 file
def index(request):
    # f = open(r"C:\Users\NEELESH AGGARWAL\PycharmProjects\DjangoProjects\textutil\textutil\textutil\buttons123")
    # content = f.read()
    # f.close()
    # return HttpResponse(content)
    # return render(request, 'index.html')
    dic = {'name': 'Neelesh', 'status': 'King'}
    return render(request, 'index.html', dic)


# Displaying a message
def about(request):
    return HttpResponse("<h1>About Hello Neelesh</h1>\n<h1>How are you dear...</h1>")


# Displaying content of fun.txt file
def fun(request):
    f = open(r"C:\Users\NEELESH AGGARWAL\PycharmProjects\DjangoProjects\textutil\textutil\textutil\fun.txt", 'r')
    content = f.read()
    f.close()
    return HttpResponse(content)


# Opening Linkedin website
def lin(request):
    return HttpResponse(
        '''<h1>Linkedin</h1><a href="https://www.linkedin.com/in/neelesh-aggarwal-b939a5214/">Linked Link</a>''')


# Pipelining Functions
# Displaying messages along with link to home page
# href will be '/' :- Its link to home page
def removepunc(request):
    # return HttpResponse('''Remove Punctuation<a href='/' target="_blank"><h2>Home</h2></a>''')
    # Text that was written on text area
    s = request.POST.get('text', 'default')
    # CheckBox (punc = on ,if checkbox was clicked)
    punc = request.POST.get('removepunc', 'off')
    capi = request.POST.get('capitalize', 'off')
    exspace = request.POST.get('extraspace', 'off')
    chcount = request.POST.get('charcount', 'off')
    # print(s, punc)
    if punc == 'on' or capi == 'on' or exspace == 'on':
        purpose = ''
        if punc == 'on':
            purpose = 'Removing Punctuations'
            punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
            analyzed = ''
            for ind, char in enumerate(s):
                if char not in punctuations:
                    analyzed += char
            s = analyzed
        if capi == 'on':
            purpose += ' Complete Capitalizing'
            a = s.upper()
            s = a
        if exspace == 'on':
            purpose = ' Removing Extra Space'
            analyzed = ''
            for ind, char in enumerate(s):
                if not (ind != len(s) - 1 and s[ind] == " " and s[ind + 1] == " "):
                    analyzed += char
            s = analyzed
        dic = {'purpose': purpose, 'analyzed_text': s}
        return render(request, 'removepunctuation.html', dic)
    elif chcount == 'on':
        dic = {'purpose': 'Character Count', 'analyzed_text': len(s)}
        return render(request, 'removepunctuation.html', dic)
    else:
        return HttpResponse("Click on checkbox, BAKA!")


def capitalizefirst(request):
    return HttpResponse('''capitalize first<a href='/' target="_blank"><h2>Home</h2></a>''')


def newlineremove(request):
    return HttpResponse('''new line remove<a href='/' target="_blank"><h2>Home</h2></a>''')


def spaceremove(request):
    return HttpResponse('''space remove<a href='/' target="_blank"><h2>Home</h2></a>''')


def charcount(request):
    return HttpResponse('''char count<a href='/' target="_blank"><h2>Home</h2></a>''')
