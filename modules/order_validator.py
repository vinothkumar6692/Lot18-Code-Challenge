import order_schema as schema1
from schematics.models import Model
from schematics.types import StringType, BooleanType
from schematics.exceptions import ValidationError


def validate_orders(data):
    rules_message_mapping = {
    'Your email address is invalid':'InvalidEmail',
    'NY state members cannot have .net email address':'NYEmail.NetInvalid',
    'Zipcode must be 5 or 9 digits':'ZipCodeLength',
    'Sum of Zipcode digits is greater than 20':'ZipCodeSum',
    'Age should be greater than 21':'AgeAllowed',
    'We dont ship to NJ':'AllowedStates',
    'We dont ship to OR':'AllowedStates',
    'We dont ship to CT':'AllowedStates',
    'We dont ship to PA':'AllowedStates',
    'We dont ship to MA':'AllowedStates',
    'We dont ship to IL':'AllowedStates',
    'We dont ship to ID':'AllowedStates'

    }
    previous_order_state = ""
    previous_order_zipcode = ""
    for i in range(len(data)):
        current_order = data[i]
        if(previous_order_zipcode==current_order['zipcode'] and previous_order_state==current_order['state']):
            current_order['valid'] = True
            current_order['errors'] = []
        else:
            try:
                valid_order = schema1.Order(current_order,strict=False).validate()
                current_order['valid'] = True
                current_order['errors'] = []
                previous_order_state = current_order['state']
                previous_order_zipcode = current_order['zipcode']
            except ValidationError as errors:
                current_order['valid'] = False
                validation_errors = []
                for i,error in enumerate(errors.messages.values()):
                    current_error = {}
                    rule = rules_message_mapping[error[0]]
                    current_error['rule']=rule
                    current_error['message']=error[0]
                    validation_errors.append(current_error)
                current_order['errors'] = validation_errors
    return data


        

