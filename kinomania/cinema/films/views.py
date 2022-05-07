from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.views.generic import ListView
from .models import Film, Hall, Screening, Ticket
from django.contrib.auth.decorators import login_required
import datetime

columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rows = ['a', 'b', 'c', 'd','e']

x=datetime.datetime.now()
class Home(View):
    def get(self, request):
        return render(request, 'films/home.html')

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
            context = {
                'message': 'this place already chose, choose another one'
            }
            return redirect(f"/{screening.id}/{screening.hall}/{time}/", context)

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

