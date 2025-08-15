from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Task Manager API</h1><p>Visit <a href='/api/tasks/'>Tasks API</a></p>")
