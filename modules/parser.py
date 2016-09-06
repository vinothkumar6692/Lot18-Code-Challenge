# -*- coding: utf-8 -*-
#
# @Author: Vinoth Kumar
# @Date:   2016-09-06
# @Email:  vinothkumar@nyu.edu

#This module is to parse the the csv file received and convert into a standard JSON format for validation

import pprint
import json
import csv

output = {'orders': []}


def parse(file):
	with open(file) as csv_file:
		orders = csv.DictReader(csv_file)
		headers = orders.fieldnames		
		for line in orders:
			current = {}
			for i,head in enumerate(headers):
				for j,title in enumerate(head.split('|')):
					current[title] = line[head].split('|')[j]

			output['orders'].append((current))
	return output

