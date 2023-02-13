"Hello Piyush dangi this side"
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check box Values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Check which check box if on
    analyzed = djtext
    params = {'purpose': "Removed Punctuation", 'analyzed_text': analyzed}
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        djtext = analyzed
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': "Removed Punctuation", 'analyzed_text': analyzed}

    if(fullcaps == "on"):
        djtext = analyzed
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Changed to Upper Case", 'analyzed_text': analyzed}

    if (newlineremover == "on"):
        djtext = analyzed
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': "New Line Removed", 'analyzed_text': analyzed}

    if (extraspaceremover == "on"):
        djtext = analyzed
        analyzed =""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': "Space Removed", 'analyzed_text': analyzed}

    if removepunc == "off" and fullcaps == "off" and newlineremover == "off" and extraspaceremover == "off":
        return HttpResponse("Error")
    return render(request, 'analyze.html', params)