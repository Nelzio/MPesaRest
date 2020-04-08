from pprint import pprint

from .portalsdk import APIContext, APIMethodType, APIRequest


def payment(**kwargs):  # antes main sem argumento | passar os values
    '''
    Modulo para pagamento que recebe uma dict
    msidsn: numeroTelefoneCliente
    api_key: api_key # encontre no teu perfil do mPesa
    public_key: public_key # encontre no teu perfil do mPesa
    amount: valorDaTransacao
    '''

    api_context = APIContext()
    api_context.api_key = kwargs['api_key']
    # api_context.public_key = kwargs['public_key']
    api_context.ssl = True
    api_context.method_type = APIMethodType.POST
    if kwargs['serviceprovidercode'] == '171717':
        api_context.public_key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmptSWqV7cGUUJJhUBxsMLonux24u+FoTlrb+4Kgc6092JIszmI1QUoMohaDDXSVueXx6IXwYGsjjWY32HGXj1iQhkALXfObJ4DqXn5h6E8y5/xQYNAyd5bpN5Z8r892B6toGzZQVB7qtebH4apDjmvTi5FGZVjVYxalyyQkj4uQbbRQjgCkubSi45Xl4CGtLqZztsKssWz3mcKncgTnq3DHGYYEYiKq0xIj100LGbnvNz20Sgqmw/cH+Bua4GJsWYLEqf/h/yiMgiBbxFxsnwZl0im5vXDlwKPw+QnO2fscDhxZFAwV06bgG0oEoWm9FnjMsfvwm0rUNYFlZ+TOtCEhmhtFp+Tsx9jPCuOd5h2emGdSKD8A6jtwhNa7oQ8RtLEEqwAn44orENa1ibOkxMiiiFpmmJkwgZPOG/zMCjXIrrhDWTDUOZaPx/lEQoInJoE2i43VN/HTGCCw8dKQAwg0jsEXau5ixD0GUothqvuX3B9taoeoFAIvUPEq35YulprMM7ThdKodSHvhnwKG82dCsodRwY428kg2xM/UjiTENog4B6zzZfPhMxFlOSFX4MnrqkAS+8Jamhy1GgoHkEMrsT5+/ofjCx0HjKbT5NuA2V/lmzgJLl3jIERadLzuTYnKGWxVJcGLkWXlEPYLbiaKzbJb2sYxt+Kt5OxQqC1MCAwEAAQ=='
        api_context.address = 'api.sandbox.vm.co.mz'
    else:
        api_context.public_key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAyrOP7fgXIJgJyp6nP/Vtlu8kW94Qu+gJjfMaTNOSd/mQJChqXiMWsZPH8uOoZGeR/9m7Y8vAU83D96usXUaKoDYiVmxoMBkfmw8DJAtHHt/8LWDdoAS/kpXyZJ5dt19Pv+rTApcjg7AoGczT+yIU7xp4Ku23EqQz70V5Rud+Qgerf6So28Pt3qZ9hxgUA6lgF7OjoYOIAKPqg07pHp2eOp4P6oQW8oXsS+cQkaPVo3nM1f+fctFGQtgLJ0y5VG61ZiWWWFMOjYFkBSbNOyJpQVcMKPcfdDRKq+9r5DFLtFGztPYIAovBm3a1Q6XYDkGYZWtnD8mDJxgEiHWCzog0wZqJtfNREnLf1g2ZOanTDcrEFzsnP2MQwIatV8M6q/fYrh5WejlNm4ujnKUVbnPMYH0wcbXQifSDhg2jcnRLHh9CF9iabkxAzjbYkaG1qa4zG+bCidLCRe0cEQvt0+/lQ40yESvpWF60omTy1dLSd10gl2//0v4IMjLMn9tgxhPp9c+C2Aw7x2Yjx3GquSYhU6IL41lrURwDuCQpg3F30QwIHgy1D8xIfQzno3XywiiUvoq4YfCkN9WiyKz0btD6ZX02RRK6DrXTFefeKjWf0RHREHlfwkhesZ4X168Lxe9iCWjP2d0xUB+lr10835ZUpYYIr4Gon9NTjkoOGwFyS5ECAwEAAQ=='
        api_context.address = 'api.vm.co.mz'
    if kwargs['method'] == "C2B":
        api_context.port = 18352
        api_context.path = '/ipg/v1x/c2bPayment/singleStage/'
    elif kwargs['method'] == "B2C":
        api_context.port = 18345
        api_context.path = '/ipg/v1x/b2cPayment/'
    
    api_context.add_header('Origin', '*')

    api_context.add_parameter('input_TransactionReference','T12344C')
    api_context.add_parameter('input_CustomerMSISDN','258{0}'.format(kwargs['msidsn']))
    api_context.add_parameter('input_Amount','{0}'.format(kwargs['amount']))
    api_context.add_parameter('input_ThirdPartyReference',kwargs['thirdParty'])
    api_context.add_parameter('input_ServiceProviderCode',kwargs['serviceprovidercode'])
    # api_context.add_parameter('input_ServiceProviderCode','171717')



    api_request = APIRequest(api_context)
    result = api_request.execute()
    # =====
    # # pprint(result.status_code)
    # # pprint(result.headers)
    # # pprint(result.body)
    pprint(result)
    # =====
    return result
