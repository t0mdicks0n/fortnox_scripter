import csv
import pprint
import json
from helpers import delete_invoice

def iterate_over_invoices(invoice_ids, fortnox_key) :
	for fortnox_id in invoice_ids :
		delete_invoice(
			fortnox_id,
			fortnox_key['Access-Token'],
			fortnox_key['Client-Secret']
		)

def main(invoice_ids, sandbox=False) :
	print invoice_ids
	# Get the API key for Fortnox API
	if sandbox :
		fortnox_key = json.load(open('application/config/fortnox_key_sandbox.json'))
	else :
		fortnox_key = json.load(open('application/config/fortnox_key.json'))
	# Iterate over all the invocies and delete them
	iterate_over_invoices(invoice_ids, fortnox_key)