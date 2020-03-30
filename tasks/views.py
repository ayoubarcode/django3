from django.shortcuts import render, redirect,get_object_or_404
from django.http import  HttpResponse,Http404,JsonResponse
from django.template.loader import  render_to_string
from django.contrib.auth.decorators import  login_required
from .models import  Task,Category, Product
from .forms import  TaskForm, ProductForm
from accounts.decorators import allowed_users
from django.core import serializers


# Create your views here.

def home(request):
    return render(request,"landing.html", {})


@login_required()
@allowed_users(allowed_roles=['admin','users'])
def index(request):
    tasks = Task.objects.tasks(request)
    form = TaskForm()
    # print(form)
    # print(request.session.keys())
    # print(request.session.items())
    # if request.method == 'POST':
    #     form = TaskForm(request.POST)
    #     print(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         user.user = request.user
    #         user.save()

    #     redirect('/tasks')

    context = { 'tasks': tasks, 'form': form}
    return render(request, 'tasks/index.html', context)
    # return HttpResponse('<h1> HEY</h1>')


def all_tasks(request):
    tasks = Task.objects.tasks(request)
    context = {'tasks':tasks}
    return render(request, 'tasks/tasks.html',context )
    

#create task json response
def create_task_json(request):
    form = TaskForm()
    data = {}
    if request.method == "POST":
        data = request.POST
        form  = TaskForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.user = request.user
            user.save()
            serializers_obj = serializers.serialize('json', [user])
    return  JsonResponse({'data':serializers_obj})

#delete task json
def delete_task_json(request):
    if request.POST:
        id = request.POST.get('id')
        task = Task.objects.get(id=id)
        task.dont_delete()
        serializers_obj = serializers.serialize('json', [task])
        return JsonResponse({'data':serializers_obj})
    return JsonResponse({'error':'does not exist'})
        
# update task json
def update_task_json(request):
    if request.POST:

        id = request.POST.get('task_id')
        task = Task.objects.get(id=id)

        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            user = form.save()
            user.user = request.user
            user.save()
            serialize_obj = serializers.serialize('json', [task])
            return JsonResponse({'obj':serialize_obj})

    return JsonResponse({'error':"error"})

def update_task(request, id):
    task_detail = get_object_or_404(Task, id=id)
    print('this is task detail', task_detail)
    form = TaskForm(instance=task_detail)

    if request.method == "POST":
        form  = TaskForm(request.POST, instance=task_detail)
        if form.is_valid():
            form.save()
            return redirect("/tasks")

    context = {
        "task_detail":task_detail,
        'form':form
    }
    return render(request, 'tasks/update.html', context)



def delete_task(request, id):
    task_delete = get_object_or_404(Task, id=id)
    print(type(task_delete))
    print( task_delete)
    if request.method == 'POST':
        task_delete.dont_delete()
        # task_delete.draft = False
        # task_delete.save()
        return redirect("/tasks")
    context = {
        'task_delete':task_delete
    }
    return render(request, 'tasks/delete.html',context)




def products(request):
    products = Product.objects.all()
    context = dict()
    context['products'] = products
    print(context)
    return render(request,'products/products.html', context)

def add_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('/tasks')
    context = {
        'form': form
    }
    return render(request,'products/add.html', context);

def get_product_category(request, title):
    categories_products = Category.objects.all().filter(name__iexact=title)
    if categories_products.count() != 1:
        raise Http404('WHAT')
    results = categories_products.first().product_set.all()
    context = {'products': results, 'category': title}
    return render(request, "products/categorie_products.html", context)
    