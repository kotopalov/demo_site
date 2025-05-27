from django.shortcuts import render
from django.http import JsonResponse

from .apps.goolets_net import GooletsNet

def GooletsNet_get_data():
    # return {"columns": ["Name", "Age"], "rows": [["Alice", 30], ["Bob", 25]]}
    return GooletsNet.get_data()

def dummy_func_2():
    return {"columns": ["Product", "Price"], "rows": [["Book", 10], ["Pen", 2]]}

FUNCTION_MAP = {
    "goolets.net": GooletsNet_get_data,
    "func2": dummy_func_2,
}

def index(request):
    return render(request, 'main.html', {'functions': FUNCTION_MAP.keys()})

def get_data(request):
    func_name = request.GET.get('func')
    data = FUNCTION_MAP.get(func_name, lambda: {"columns": [], "rows": []})()
    return JsonResponse(data)
