from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    #to get the actual text
    djtext = request.POST.get('text','default')

    # to check the value of checkbox
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    charcount = request.POST.get('charcount', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    #check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for chr in djtext:
            if chr not in punctuations:
                analyzed = analyzed + chr
        param = {'purpose':'Removing Punctuatuons', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', param)

    if capitalize == 'on':
        analyzed = ""
        for chr in djtext:
            analyzed = analyzed + chr.upper()
        param = {'purpose':'Capitalizing', 'analyzed_text':analyzed} 
        djtext = analyzed  
        # return render(request, 'analyze.html', param)


    if charcount == "on":
        analyzed = 0
        space = 0
        for chr in djtext:
            analyzed +=1
        for index, chr in enumerate(djtext):
            if djtext[index] == " ":
                space += 1
        analyzed = analyzed - space
        param = {'purpose':'Counting Characters', 'analyzed_text':analyzed}
        return render(request,'analyze.html',param)

    if extraspaceremover == "on":
        analyzed = ""
        for index, chr in  enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + chr
        param = {'purpose':'After removing ExtraSpaces', 'analyzed_text':analyzed}
        # return render(request, 'analyze.html', param)

                  
    if (removepunc!="on" and capitalize!="on" and charcount!="on" and extraspaceremover!="on"):
        param = {'purpose':'Sorry choose either one option', 'analyzed_text':djtext}

        return render(request, 'error.html', param)

    return render(request, 'analyze.html', param)

# def capfirst(request):
#     return HttpResponse("capitilize first chr")


# def newlineremove(request):
#     return HttpResponse("remove new line")


# def spaceremove(request):
#     return HttpResponse("remove spaces")



# def charcount(request):
#     return HttpResponse("count characters")