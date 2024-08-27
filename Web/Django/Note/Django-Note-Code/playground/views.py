from django.shortcuts import render
from .tasks import notify_customers


def say_hello(request):
    notify_customers.delay('Delay Task is starting......')
    # notify_customers('Hello')
    return render(request, 'hello.html', {'name': 'YIP, Ching'})
