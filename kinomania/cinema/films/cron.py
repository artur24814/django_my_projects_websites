from .models import Ticket

import datetime
x=datetime.datetime.now()

def delete_ticket():
  bad_ticket = Ticket.objects.filter(data__lt=x.strftime("%Y-%m-%d"))
  bad_ticket.delete()