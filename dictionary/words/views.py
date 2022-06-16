from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from django.views import View
from django.views.generic import ListView
import random
from django.contrib import messages

import os

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate

from .models import Words, TextWithWord
from .form import WordsForm
from django.http import JsonResponse

#Translating app
import deepl

auth_key = os.environ.get("auth_key")
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
            return render(request, 'words/home.html')
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

class UserDictionary(View):
    def get(self,request):
        queryset = Words.objects.filter(author=request.user).order_by('alphabet')
        context = {
            'object_list': queryset
        }
        return render(request, 'words/User_dictionary.html', context)

@login_required
def update_word(request, id):
    word = get_object_or_404(Words, pk=id)
    if word.author != request.user:
        messages.success(request, "you can't change this word, you not an author of this word")
        return redirect('/user-dictionary/')
    if request.method == "POST":
        form = WordsForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            messages.success(request, "you change your world")
            return redirect('/user-dictionary/')
    else:
        form = WordsForm(instance=word)
    context = {
        'form': form,
    }
    return render(request, 'words/update-word.html', context)

@login_required
def delete_word(request, id):
    word =get_object_or_404(Words, pk=id, author=request.user)
    word.delete()
    messages.success(request, 'Word was delited from dictionary!')
    return redirect('/user-dictionary/')


class UserCadrdGame(View):
    def get(self, request):
        if request.user.is_authenticated:
            words = Words.objects.filter(author=request.user)
            if len(words) < 16:
                messages.success(request, ('you mast have at least 16 words at dictionary'))
                return redirect('/')
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
        else:
            messages.success(request, 'You mast to loggin!!')
            return redirect('/login/')

class FrassesView(View):
    def get(self,request):
        words = Words.objects.all()
        random_word = random.choice(words)
        if is_ajax(request=request):
            random_word = random.choice(words)
            return JsonResponse({'word': random_word.definition}, status=200)
        context = {
            "word": random_word,
        }
        return render(request, 'words/frasses.html', context)

    def post(self,request):
        word = str(request.POST.get('word'))
        word_result = get_object_or_404(Words,definition=word)
        text = str(request.POST.get('text'))
        test_text = []
        for leter in text:
            test_text.append(leter)
        if len(test_text) < 25:
            message = "too short text"
            return JsonResponse({'data': message}, status=200)
        else:
            word_and_text = TextWithWord.objects.create(word=word_result, text=text, author=request.user)
            word_and_text.save()

            message = "You save this text"
            return JsonResponse({'data': message}, status=200)
