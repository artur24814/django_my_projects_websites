from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.views.generic import ListView
from django.contrib import messages

from .models import Film, Hall, Screening, Ticket
from django.contrib.auth.decorators import login_required


import datetime
import random

columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rows = ['a', 'b', 'c', 'd','e']

x=datetime.datetime.now()


class Home(View):
    def get(self, request):
        random_film_list = []
        for film in Film.objects.all():
            random_film_list.append(film)
        context = {
            'film': random.choice(random_film_list)
        }
        return render(request, 'films/home.html', context)

class SearchView(View):
    def get(self,request):
        return render(request, 'films/search.html')

    def post(self,request):
        question = request.POST.get('question')
        film = Film.objects.filter(title__contains=question)

        if film:
            hall = Hall.objects.get(film=film[0])
        context = {
            'question': question,
            'films': film,
            'hall': hall,
        }
        return render(request, 'films/search.html', context)

class AllFilms(ListView):
    template_name = "films/all_films.html"
    queryset = Film.objects.all()

class AllHall(ListView):
    template_name = "films/all_hall.html"
    queryset = Hall.objects.filter(used_to__gt=x.strftime("%Y-%m-%d"))

class FreeHall(ListView):
    template_name = "films/free_halls.html"
    queryset = Hall.objects.filter(used_to__lt=x.strftime("%Y-%m-%d"))

class HallDetail(View):
    def get(self, request, id):
        hall = get_object_or_404(Hall, id=id)
        show = Screening.objects.filter(film=hall.film)
        context = {
            'hall': hall,
            'show': show
        }
        return render(request, 'films/hall_detail.html', context)

class HallView(View):
    def get(self, request, id, hall, time):

        # hall = Hall.objects.get(id=id)
        hall = get_object_or_404(Hall, title=hall)

        reserved = Ticket.objects.filter(screening= id)
        rowcolums = []
        for item in reserved:
            rowcolums.append(item.rowcolums)
        context = {
            'screening_id': id,
            'hall': hall,
            'columns': columns,
            'rows': rows,
            'rowcolums': rowcolums,
            'time': time,
        }
        return render(request, 'films/hall.html', context)

class ReserveTicket(View):
    def get(self, request, rowcolums, id, time):
        # screaning = Ticket.objects.filter(screening=id)
        screening = get_object_or_404(Screening, id=id)
        # obj_hall = get_object_or_404(Hall, pk=id)
        test = Ticket.objects.filter(screening=id,rowcolums=(rowcolums))
        if test :
            messages.success(request, ('this place already chose, choose another one'))
            return redirect(f"/{screening.id}/{screening.hall}/{time}/", {})

        ticket = Ticket.objects.create(screening=screening, rowcolums=rowcolums)
        context = {
            'ticket': ticket
        }
        ticket.customer = request.user
        ticket.save()
        return render(request, 'films/ticket.html', context)
        # except Exception:
        #     return redirect("Error/")

class ErrorView(View):
    def get(self,request):
        return render(request, 'films/Error.html')

@login_required
def UserTicket(request):
    if request.method == "GET":
        queryset = Ticket.objects.filter(customer=request.user)
        context = {
            'ticket': queryset
        }
        return render(request,'films/your_ticket.html', context)

@login_required
def DeleteTicket(request, id):
    ticket = get_object_or_404(Ticket, pk=id, customer=request.user)
    ticket.delete()
    messages.success(request, ('Ticket was delited'))
    return redirect('/your-ticket/')

