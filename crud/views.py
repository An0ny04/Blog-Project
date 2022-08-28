from django.shortcuts import render,redirect

from crud.forms import StudentForm
from crud.models.student import Student

# Create your views here.
def index(request):
    context ={}
 
    # add the dictionary during initialization
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.FILES)
            form.save()
        return redirect('home')
    data = Student.objects.all()
    context['data'] = data
    context['form']= form
    return render(request, "index.html", context)