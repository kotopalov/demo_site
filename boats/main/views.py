from django.shortcuts import render
from django.http import JsonResponse

from .apps.goolets_net import GooletsNet
from .apps.m_blueyachts_com import MBlueyachtsCom

def goolets_net_get_data():
    return GooletsNet.get_data()

def m_blueyachts_com_get_data():
    return MBlueyachtsCom.get_data()

FUNCTION_MAP = {
    "goolets.net": goolets_net_get_data,
    "m-blueyachts.com": m_blueyachts_com_get_data,
}

def index(request):
    return render(request, 'main.html', {'functions': FUNCTION_MAP.keys()})

def get_data(request):
    func_name = request.GET.get('func')
    data = FUNCTION_MAP.get(func_name, lambda: {"columns": [], "rows": []})()
    return JsonResponse(data)
