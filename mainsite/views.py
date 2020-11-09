from django.shortcuts import render
from until import chapter

# Create your views here.
def read(request):
    content=chapter.read()
    return render(request, "read.html",{"content":content});
