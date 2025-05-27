from django.shortcuts import render
from django.http import JsonResponse

def dummy_func_1():
    return {"columns": ["Name", "Age"], "rows": [["Alice", 30], ["Bob", 25]]}

def dummy_func_2():
    return {"columns": ["Product", "Price"], "rows": [["Book", 10], ["Pen", 2]]}

FUNCTION_MAP = {
    "func1": dummy_func_1,
    "func2": dummy_func_2,
}

def index(request):
    return render(request, 'main.html', {'functions': FUNCTION_MAP.keys()})

def get_data(request):
    func_name = request.GET.get('func')
    data = FUNCTION_MAP.get(func_name, lambda: {"columns": [], "rows": []})()
    return JsonResponse(data)
