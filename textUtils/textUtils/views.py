from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("About Akshit")


def analyze(request):
    post_obj = request.POST
    org_text = post_obj.get('analysis-text', 'default')

    # Check which buttons are enabled
    removepunc = post_obj.get('removepunc', 'off')
    capitalize = post_obj.get('capitalize', 'off')
    newlineremover = post_obj.get('newlineremover', 'off')
    extraspaceremover = post_obj.get('extraspaceremover', 'off')
    charcount = post_obj.get('charcount', 'off')

    # Analyze the text, supports multiple operations
    if removepunc == 'on':
        analyzed_text = ''
        punctuations = '''{}()[];:'"\,!@#$`?%^&*~.|/-_+<>'''
        for char in org_text:
            if char not in punctuations:
                analyzed_text += char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed_text}
        org_text = analyzed_text

    if capitalize == 'on':
        analyzed_text = org_text.upper()
        params = {'purpose': 'Converted to Uppercase', 'analyzed_text': analyzed_text}
        org_text = analyzed_text

    if newlineremover == 'on':
        analyzed_text = ''
        for char in org_text:
            if char != '\n' and char != '\r':
                analyzed_text += char
        params = {'purpose': 'Removed new line', 'analyzed_text': analyzed_text}
        org_text = analyzed_text

    if extraspaceremover == 'on':
        analyzed_text = ''
        for index, char in enumerate(org_text):
            if not (org_text[index] == '' and org_text[index + 1] == ''):
                analyzed_text += char
        params = {'purpose': 'Removed extra spaces', 'analyzed_text': analyzed_text}
        org_text = analyzed_text

    if charcount == 'on':
        count = 0
        for char in org_text:
            if char != ' ':
                count += 1
        params = {'purpose': 'Count number of characters', 'count': count, 'analyzed_text': org_text}
        
    if(removepunc != 'on' and capitalize != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on'):
        return render(request, 'analyze.html', {'analyzed_text': org_text, 'purpose': 'No operation performed'})
    
    return render(request, 'analyze.html', params)
