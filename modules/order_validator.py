# -*- coding: utf-8 -*-
#
# @Author: Vinoth Kumar
# @Date:   2016-09-06
# @Email:  vinothkumar@nyu.edu

#This module is to validate the order information and it uses the validation rules specified in schema.py using schematics.

import order_schema as schema1
from schematics.models import Model
from schematics.types import StringType, BooleanType
from schematics.exceptions import ValidationError


def validate_orders(data):
    #Rules to error message mapping criteria
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
        #Validate each order one by one
        current_order = data[i]
        #Check if the state and Zipcode of the current order being processed is same as the previous. If yes, no validation rules will apply
        if(previous_order_zipcode==current_order['zipcode'] and previous_order_state==current_order['state']):
            current_order['valid'] = True
            current_order['errors'] = []
        else:
            #Validate the current order using the specified validation rules in schema.py
            try:
                valid_order = schema1.Order(current_order,strict=False).validate()
                #No exceptions raised after validation. Current order is valid
                current_order['valid'] = True
                current_order['errors'] = []
                previous_order_state = current_order['state']
                previous_order_zipcode = current_order['zipcode']
            except ValidationError as errors:
                #Current order is invalid since exceptions are raised during validation
                previous_order_state = current_order['state']
                previous_order_zipcode = current_order['zipcode']
                current_order['valid'] = False
                validation_errors = []
                for i,error in enumerate(errors.messages.values()):
                    #add the errors from validation to current order and set valid to false
                    current_error = {}
                    rule = rules_message_mapping[error[0]]
                    current_error['rule']=rule
                    current_error['message']=error[0]
                    validation_errors.append(current_error)
                current_order['errors'] = validation_errors
    return data


        

