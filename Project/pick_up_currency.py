import xmltodict

def currency_names():
    with open("dist/currency.xml", "rb") as archive_currency:
        dic_currency = xmltodict.parse(archive_currency)
    
    currency = dic_currency["xml"]
    return currency
    
def available_conversions():
    with open("dist/converter.xml", "rb") as archive_converter:
        dic_converter = xmltodict.parse(archive_converter)
    
    converter = dic_converter["xml"]
    dic_converter_available = {}
    
    for pair_conversion in converter:
        currency_origin, destination_currency = pair_conversion.split('-')
        if currency_origin in dic_converter_available:
            dic_converter_available[currency_origin].append(destination_currency)
        else:
            dic_converter_available[currency_origin] = [destination_currency]
    
    return dic_converter_available
