from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import ListView
import random
from django.contrib import messages

from .models import Words

from django.http import JsonResponse

#Translating app
import deepl

auth_key = "5c956ed3-f892-e7ad-470d-d8010548f352:fx"
translator = deepl.Translator(auth_key)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class HomeView(View):
    def get(self, request):
        word = request.GET.get("word")
        if is_ajax(request=request):
            result = translator.translate_text(f"{word}", target_lang="EN-GB")

            return JsonResponse({'translated': str(result), 'word': word}, status=200)
        return render(request, 'words/home.html', {})

    def post(self, request):
        text = request.POST.get('text')
        list = text.split('---')
        existword = Words.objects.filter(word=list[0])
        if existword:
            message = 'this word alredy exist at dictionary'
            return JsonResponse({'data': message}, status=200)
        else:
            words = Words.objects.create(word=list[0], definition=list[1], author=request.user)
            words.save()

            message = f"{text} is added to dictonary !!!"
            return JsonResponse({'data': message}, status=200)

class Dictionary(ListView):
    queryset = Words.objects.all().order_by('alphabet')
    template_name = 'words/dictionary.html'


class CadrdGame(View):
    def get(self, request):
        words = Words.objects.all()
        if len(words) < 16:
            messages.success(request, ('you mast have at least 16 words at dictionary'))
            return render(request, 'words/home.html', messages)
        else:
            resultList = []
            i = 0
            while len(resultList) < 16:
                index = words[random.randint(0, (len(words)-1))]
                if index not in resultList:
                    resultList.append(index)
            j = 1
            context = {}
            for word in resultList:
                context[f'list{j}'] = word
                j += 1
            return render(request, 'words/cardGame.html', context)


