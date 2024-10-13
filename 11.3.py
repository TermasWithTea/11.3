def introspection_info(obj):
    return {'type':type(obj).__name__, 'method': dir(obj), 'modelu': obj.__dir__(),
             'modelo':obj.__mod__,'doc':obj.__doc__}

number_info = introspection_info(42)
print(number_info)