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
    costomerMSISDN = '{}{}'.format(258, kwargs['msidsn'])  # number cotomer
    api_context = APIContext()
    api_context.api_key = kwargs['api_key']
    api_context.public_key = kwargs['public_key']
    api_context.ssl = True
    api_context.method_type = APIMethodType.POST
    api_context.address = 'api.sandbox.vm.co.mz'
    api_context.port = 18346
    api_context.path = '/ipg/v1/c2bpayment/'

    api_context.add_header('Origin', '*')

    api_context.add_parameter('input_ThirdPartyReference', 'Produto {} da {}'.format(kwargs['product'], kwargs['business']))
    api_context.add_parameter('input_Amount', kwargs['amount'])
    api_context.add_parameter('input_CustomerMSISDN', costomerMSISDN) # 848403149
    api_context.add_parameter('input_ServiceProviderCode', '171717')
    api_context.add_parameter('input_TransactionReference', 'T12344C')

    # api_context.add_parameter('output_ResponseDesc', 'SmellMoz')

    api_request = APIRequest(api_context)
    result = api_request.execute()
    return result
    pprint(result.status_code)
    pprint(result.headers)
    pprint(result.body)


'''
api_context = APIContext()
    api_context.api_key = 'wyi2qfh5fw270e3ytlykda4250pwouas'
    api_context.public_key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmptSWqV7cGUUJJhUBxsMLonux24u+FoTlrb+4Kgc6092JIszmI1QUoMohaDDXSVueXx6IXwYGsjjWY32HGXj1iQhkALXfObJ4DqXn5h6E8y5/xQYNAyd5bpN5Z8r892B6toGzZQVB7qtebH4apDjmvTi5FGZVjVYxalyyQkj4uQbbRQjgCkubSi45Xl4CGtLqZztsKssWz3mcKncgTnq3DHGYYEYiKq0xIj100LGbnvNz20Sgqmw/cH+Bua4GJsWYLEqf/h/yiMgiBbxFxsnwZl0im5vXDlwKPw+QnO2fscDhxZFAwV06bgG0oEoWm9FnjMsfvwm0rUNYFlZ+TOtCEhmhtFp+Tsx9jPCuOd5h2emGdSKD8A6jtwhNa7oQ8RtLEEqwAn44orENa1ibOkxMiiiFpmmJkwgZPOG/zMCjXIrrhDWTDUOZaPx/lEQoInJoE2i43VN/HTGCCw8dKQAwg0jsEXau5ixD0GUothqvuX3B9taoeoFAIvUPEq35YulprMM7ThdKodSHvhnwKG82dCsodRwY428kg2xM/UjiTENog4B6zzZfPhMxFlOSFX4MnrqkAS+8Jamhy1GgoHkEMrsT5+/ofjCx0HjKbT5NuA2V/lmzgJLl3jIERadLzuTYnKGWxVJcGLkWXlEPYLbiaKzbJb2sYxt+Kt5OxQqC1MCAwEAAQ=='
    api_context.ssl = True
    api_context.method_type = APIMethodType.POST
    api_context.address = 'api.sandbox.vm.co.mz'
    api_context.port = 18346
    api_context.path = '/ipg/v1/c2bpayment/'

    api_context.add_header('Origin', '*')

    api_context.add_parameter('input_ThirdPartyReference', '0408e902-ad5d-4976-8aac-2f04d90f14e7')
    api_context.add_parameter('input_Amount', '10')
    api_context.add_parameter('input_CustomerMSISDN', costomerMSISDN) # 848403149
    api_context.add_parameter('input_ServiceProviderCode', '171717')
    api_context.add_parameter('input_TransactionReference', 'T12344C')
    '''