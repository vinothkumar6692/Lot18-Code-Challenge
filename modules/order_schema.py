# -*- coding: utf-8 -*-
#
# @Author: Vinoth Kumar
# @Date:   2016-09-06
# @Email:  vinothkumar@nyu.edu

from schematics.models import Model
from schematics.types import StringType, BooleanType
from schematics.exceptions import ValidationError
from time import strptime
import datetime
from datetime import date
import re

#This acts as a config file to specify all the rules using Schematics to perform validation.

class Order(Model):
    id = StringType()
    name = StringType()
    email = StringType()
    state = StringType()
    zipcode = StringType()
    birthday = StringType()
    year = StringType()
    def validate_email(self, data, value):
    	email_valid_regex = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{3,4}$')
    	email_regex_net = re.compile('^([A-Z0-9a-z]+@[A-Z0-9a-z]+\.net)+$')
        if email_regex_net.match(data['email']) and data['state']=='NY':
            raise ValidationError('NY state members cannot have .net email address')
        if not email_valid_regex.match(data['email']):
        	raise ValidationError('Your email address is invalid')
        return value
    def validate_state(self,data,value):
    	invalid_states = ['NJ','CT','PA','MA','IL','ID','OR']
    	if data['state'] in invalid_states:
    		raise ValidationError(str('We dont ship to '+data['state']))
    	return value

    def validate_zipcode(self,data,value):
    	zipcode_valid_regex = re.compile('^([0-9]{5}[*-]{1}[0-9]{4}|[0-9]{5})$')
    	if not zipcode_valid_regex.match(data['zipcode']):
    		raise ValidationError('Zipcode must be 5 or 9 digits')
    	if len(data['zipcode']) == 5  and sum(int(i) for i in str(data['zipcode'])) > 20:
    		raise ValidationError('Sum of Zipcode digits is greater than 20')
    	if len(data['zipcode']) == 10  and sum(int(i) for i in value[:5])+ sum((int(i) for i in value[6:])) > 20:
    		raise ValidationError('Sum of Zipcode digits is greater than 20')

    def validate_birthday(self,data,value):
        year = int(data['year'])
        month = int(strptime(value[:3],'%b').tm_mon)
        day = int(value[-2:].strip(''))
        today = date.today()
        birth_date = date(year,month,day)
        if today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)) <= 21:
            raise ValidationError("Age should be greater than 21")
