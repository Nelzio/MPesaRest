# from django.shortcuts import render
# https://mpesa-fa.herokuapp.com/ | https://git.heroku.com/mpesa-fa.git

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .mpesa import payment
from .models import EntradasApi


@api_view(['GET', 'POST'])
def purchase_api(request, format=None):

    if request.method == 'POST':
        cad = EntradasApi(page="API Payment")  # @classmethod is used here
        cad.save()
        # print(product.title)
        result = payment(
            msidsn=request.data['msidsn'],
            api_key=request.data['api_key'],
            public_key=request.data['public_key'],
            amount=request.data['amount'],
            product=request.data['product'],
            business=request.data['business']
        )
        '''
        pprint(result.status_code)
        pprint(result.headers)
        pprint(result.body)
        '''

        # print(request.data['card'])
        return Response(result.body, status=result.status_code)
    return Response(status=status.HTTP_400_BAD_REQUEST)
