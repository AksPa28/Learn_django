from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("About Akshit")


def analyze(request):
    post_obj = request.POST
    org_text = post_obj.get('analysis-text', 'default')
    print("ORIGINAL TEXT:", org_text)
    analyzed_text = ''

    # Check which buttons are enabled
    removepunc = post_obj.get('removepunc', 'off')
    capitalize = post_obj.get('capitalize', 'off')
    newlineremover = post_obj.get('newlineremover', 'off')
    extraspaceremover = post_obj.get('extraspaceremover', 'off')
    charcount = post_obj.get('charcount', 'off')


    if removepunc == 'on':
        punctuations = '''{}()[];:'"\,!@#$`?%^&*~.|/-_+<>'''
        removed = ''
        for char in org_text:
            if char not in punctuations:
                analyzed_text += char
            else:
                removed += char
        print('Removed characters:', removed)
        params = {'purpose': 'Removed punctuations',
                  'analyzed_text': analyzed_text}
        return render(request, 'analyze.html', params)

    elif capitalize == 'on':
        analyzed_text = org_text.upper()
        params = {'purpose': 'Converted to Uppercase',
                  'analyzed_text': analyzed_text}
        return render(request, 'analyze.html', params)

    elif newlineremover == 'on':
        for char in org_text:
            if char != '\n':
                analyzed_text += char
        params = {'purpose': 'Removed new line',
                  'analyzed_text': analyzed_text}
        return render(request, 'analyze.html', params)

    elif extraspaceremover == 'on':
        for index, char in enumerate(org_text):
            if not (org_text[index] == '' and org_text[index + 1] == ''):
                analyzed_text += char
        params = {'purpose': 'Removed extra spaces',
                  'analyzed_text': analyzed_text}
        return render(request, 'analyze.html', params)

    elif charcount == 'on':
        count = 0
        for char in org_text:
            if char != ' ':
                count += 1
        params = {'purpose': 'Count number of characters',
                  'analyzed_text': org_text, 'count': count}
        return render(request, 'analyze.html', params)
    
    else:
        return HttpResponse("Error")
