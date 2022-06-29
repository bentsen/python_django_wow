import json
import urllib.request

import requests
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from .utils import get_data_from_api
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def get_item(request, itemId):
    params = {
        'namespace': 'static-eu',
        'locale': 'en_US'
    }
    return Response(get_data_from_api('eu', f'/data/wow/item/{itemId}', params))


@api_view(['GET'])
def get_mounts(request):
    params = {
        'namespace': 'static-eu',
        'locale': 'en_US'
    }
    return Response(get_data_from_api('eu', '/data/wow/mount/index', params))


@api_view(['GET'])
def get_mount(request, mountId):
    params = {
        'namespace': 'static-eu',
        'locale': 'en_US'
    }
    return Response(get_data_from_api('eu', f'/data/wow/mount/{mountId}', params))


@api_view(['GET'])
def get_character_media(request, region, realmSlug, characterName):
    params ={
        'namespace': f'static-{region}'
        'locale:' 'en_US'
    }
    return Response(get_data_from_api
                    (f'{region}', f'/profile/wow/character/{realmSlug}/{characterName}/character-media', params))