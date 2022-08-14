from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
import random
from django.contrib import messages

import os

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate

from .models import Words, TextWithWord, CommentsText, RandomWordForHomeView, LikeText
from .form import WordsForm
from django.http import JsonResponse

# Translating app
import deepl

auth_key = os.environ.get("auth_key")
translator = deepl.Translator(auth_key)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

import datetime
x=datetime.datetime.now()


class HomeView(View):
    """
    view home page for search word
    """
    def get(self, request):
        word = request.GET.get("word")
        #check lengh text which write user
        if len(str(word)) > 100:
            #if text too long
            return redirect('/')
        if is_ajax(request=request):
            result = translator.translate_text(f"{word}", target_lang="EN-GB")

            return JsonResponse({'translated': str(result), 'word': word}, status=200)
        #Day word in maine page
        word_for_home_view = RandomWordForHomeView.objects.all()
        #if word didn't exist
        if len(word_for_home_view) == 0:
            list = Words.objects.all()
            random_word = random.choice(list)
            RandomWordForHomeView.objects.create(word=random_word)
            return render(request, 'words/home.html', {'random_word': word_for_home_view})
        bad_words = RandomWordForHomeView.objects.filter(create__lt=x.strftime("%Y-%m-%d"))
        if bad_words:
            bad_words.delete()
            list = Words.objects.all()
            random_word = random.choice(list)
            word_for_home_view = RandomWordForHomeView.objects.create(word=random_word)
            return render(request, 'words/home.html', {'random_word': word_for_home_view})
        else:
            word_for_home_view = RandomWordForHomeView.objects.all().first()
            return render(request, 'words/home.html', {'random_word': word_for_home_view})

    def post(self, request):
        # if user not log in
        if request.user.is_anonymous:
            message = "to save word you must be login in !!!"
            return JsonResponse({'data': message}, status=200)
        #separate word and definition
        text = request.POST.get('text')
        list = text.split('---')
        existword = Words.objects.filter(word=list[0])
        #check if word alredy exist
        if existword:
            message = 'this word alredy exist at dictionary'
            return JsonResponse({'data': message}, status=200)
        else:
            #when everything ok
            words = Words.objects.create(word=list[0], definition=list[1], author=request.user)
            words.save()

            message = f"{text} is added to dictonary !!!"
            return JsonResponse({'data': message}, status=200)


class HomeViewEn(View):
    """
    view home page for search word
    """
    def get(self, request):
        word = request.GET.get("word")
        #check lengh text which write user
        if len(str(word)) > 100:
            #if text too long
            return redirect('/')
        if is_ajax(request=request):
            result = translator.translate_text(f"{word}", target_lang="PL")

            return JsonResponse({'translated': word, 'word': str(result)}, status=200)
        #Day word in maine page
        word_for_home_view = RandomWordForHomeView.objects.all()
        #if word didn't exist
        if len(word_for_home_view) == 0:
            list = Words.objects.all()
            random_word = random.choice(list)
            RandomWordForHomeView.objects.create(word=random_word)
            return render(request, 'words/home_en.html', {'random_word': word_for_home_view})
        bad_words = RandomWordForHomeView.objects.filter(create__lt=x.strftime("%Y-%m-%d"))
        if bad_words:
            bad_words.delete()
            list = Words.objects.all()
            random_word = random.choice(list)
            word_for_home_view = RandomWordForHomeView.objects.create(word=random_word)
            return render(request, 'words/home.html', {'random_word': word_for_home_view})
        else:
            word_for_home_view = RandomWordForHomeView.objects.all().first()
            return render(request, 'words/home_en.html', {'random_word': word_for_home_view})

    def post(self, request):
        # if user not log in
        if request.user.is_anonymous:
            message = "to save word you must be login in !!!"
            return JsonResponse({'data': message}, status=200)
        #separate word and definition
        text = request.POST.get('text')
        list = text.split('---')
        existword = Words.objects.filter(word=list[0])
        #check if word alredy exist
        if existword:
            message = 'this word alredy exist at dictionary'
            return JsonResponse({'data': message}, status=200)
        else:
            #when everything ok
            words = Words.objects.create(word=list[0], definition=list[1], author=request.user)
            words.save()

            message = f"{text} is added to dictonary !!!"
            return JsonResponse({'data': message}, status=200)


class Dictionary(ListView):
    """
    view global dictionary
    """
    queryset = Words.objects.all().order_by('alphabet')
    template_name = 'words/dictionary.html'


class BlogView(View):
    """
    view Blog
    """
    def get(self, request):
        #all Posts sorted by date created
        posts = TextWithWord.objects.all().order_by('-create')
        #all comments
        comments = CommentsText.objects.all()
        context = {
            'posts': posts,
            'comments': comments
        }
        return render(request, 'words/blog.html', context)



class CreateLike(LoginRequiredMixin,View):
    """
    creating LIKE
    """
    def get(self,request, id_post):
        post = get_object_or_404(TextWithWord, id=id_post)
        username = request.user.username
        like_filter = LikeText.objects.filter(text=post, username=username).first()
        #check if user never like this post
        if like_filter == None:
            new_like = LikeText.objects.create(text=post, username=username)
            new_like.save()
            post.no_of_likes = post.no_of_likes + 1
            post.save()
            return redirect('/blog/')
        else:
            # when user already like this post
            like_filter.delete()
            post.no_of_likes = post.no_of_likes - 1
            post.save()

            return redirect('/blog/')

class CreateComment(LoginRequiredMixin,View):
    """
    creating COMMENT
    """
    def post(self, request, id_post):
        text = request.POST.get('text')
        post = get_object_or_404(TextWithWord, id=id_post)
        CommentsText.objects.create(text=text, post=post, author=request.user)
        return redirect('/blog/')


class CardGame(View):
    """
    global Card GAME
    """
    def get(self, request):
        words = Words.objects.all()
        #check length list all words
        if len(words) < 16:
            messages.success(request, ('you mast have at least 16 words at dictionary'))
            return render(request, 'words/home.html')
        else:
            resultList = []
            i = 0
            #create list of random not repeated words
            while len(resultList) < 16:
                index = words[random.randint(0, (len(words) - 1))]
                if index not in resultList:
                    resultList.append(index)
            j = 1
            #create dict with random word
            context = {}
            for word in resultList:
                context[f'list{j}'] = word
                j += 1
            return render(request, 'words/cardGame.html', context)


class UserDictionary(LoginRequiredMixin,View):
    """
    view user own dictionary
    """
    def get(self, request):
        queryset = Words.objects.filter(author=request.user).order_by('alphabet')
        context = {
            'object_list': queryset
        }
        return render(request, 'words/User_dictionary.html', context)


@login_required
def update_word(request, id):
    """
    view for update word in user own dictinary
    """
    word = get_object_or_404(Words, pk=id)
    #check if user is owner of this word
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
    """
    view for delete word in user own dictinary
    """
    word = get_object_or_404(Words, pk=id, author=request.user)
    word.delete()
    messages.success(request, 'Word was deleted from dictionary!')
    return redirect('/user-dictionary/')


class UserCardGame(LoginRequiredMixin,View):
    """
    view for user own card GAME
    """
    def get(self, request):
        if request.user.is_authenticated:
            words = Words.objects.filter(author=request.user)
            # check length list all words
            if len(words) < 16:
                messages.success(request, ('you mast have at least 16 words at dictionary'))
                return redirect('/')
            else:
                resultList = []
                i = 0
                while len(resultList) < 16:
                    index = words[random.randint(0, (len(words) - 1))]
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


class FrassesView(LoginRequiredMixin,View):
    """
    view for get random frase and write text to this word
    """
    def get(self, request):
        #get random word
        words = Words.objects.all()
        if len(words) == 0:
            messages.success(request, ('Upsss.... you do not have any word, plese create some word'))
            return render(request, 'words/frasses.html')
        random_word = random.choice(words)
        #get another random word
        if is_ajax(request=request):
            random_word = random.choice(words)
            return JsonResponse({'word': random_word.definition}, status=200)
        context = {
            "word": random_word,
        }
        return render(request, 'words/frasses.html', context)

    def post(self, request):
        word = str(request.POST.get('word'))
        word_result = get_object_or_404(Words, definition=word)
        text = str(request.POST.get('text'))
        test_text = []
        #check lengh text
        for leter in text:
            test_text.append(leter)
        # if too short
        if len(test_text) < 25:
            message = "too short text"
            return JsonResponse({'data': message}, status=200)
        #if text ok
        else:
            word_and_text = TextWithWord.objects.create(word=word_result, text=text, author=request.user)
            word_and_text.save()

            message = "You save this text"
            return JsonResponse({'data': message}, status=200)
