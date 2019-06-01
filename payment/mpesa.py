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
    '''# api_context.add_parameter('input_TransactionReference', 'Produto {0} da {1}'.format(kwargs['product'], kwargs['business']))
    api_context.add_parameter('input_Amount', kwargs['amount']) # price of item
    api_context.add_parameter('input_ThirdPartyReference', kwargs['thirdParty'])'''


    api_context = APIContext()
    api_context.api_key = kwargs['api_key']
    api_context.public_key = kwargs['public_key']
    api_context.ssl = True
    api_context.method_type = APIMethodType.POST
    api_context.address = 'api.sandbox.vm.co.mz'
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
    api_context.add_parameter('input_ServiceProviderCode','171717')


    api_request = APIRequest(api_context)
    result = api_request.execute()
    return result
    # pprint(result.status_code)
    # pprint(result.headers)
    # pprint(result.body)