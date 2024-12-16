def validation_error_handler(data):
    key = list(data.keys())[0]
    value = data[key]
    print(data)

    if key == 'non_field_errors':
        return value[0]
    if type(value) == list:
        message = f"{value[0]}"
    else:
        message = f"{value}"
    return message