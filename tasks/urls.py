from django.urls import  path
from .views import  (index, update_task,
                        delete_task, 
                        add_product,
                        get_product_category,products ,
                        create_task_json,
                        all_tasks,
                        delete_task_json,
                        update_task_json) 

app_name = 'tasks'
urlpatterns = [
    path('', index, name="tasks"),
    path('update/<int:id>', update_task , name="update_task"),
    path('delete/<int:id>', delete_task , name="delete_task"),

    #JSON 

    path('create_task', create_task_json, name="create_task_json"),
    path('delete_task', delete_task_json, name="delete_task_json"),
    path('update_task_json', update_task_json, name="update_task_json"),
    path('tasks', all_tasks, name="all_tasks_json"),
    
    #products
    path("products", products, name="products"),
    path("addproduct", add_product, name="add_product"),
    path("category/<str:title>", get_product_category, name="product_category")
]
