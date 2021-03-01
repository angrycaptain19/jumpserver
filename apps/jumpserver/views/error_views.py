# -*- coding: utf-8 -*-
#
from django.shortcuts import render
from django.http import JsonResponse

__all__ = ['handler404', 'handler500']


def handler404(request, *args, **argv):
    if request.content_type.find('application/json') > -1:
        return JsonResponse({'error': 'Not found'}, status=404)
    else:
        return render(request, '404.html', status=404)


def handler500(request, *args, **argv):
    if request.content_type.find('application/json') > -1:
        return JsonResponse({'error': 'Server internal error'}, status=500)
    else:
        return render(request, '500.html', status=500)
