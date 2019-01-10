# coding: utf8
import argparse
from jobs import create_invoices

if __name__ == '__main__' :
	parser = argparse.ArgumentParser(
		description='Fortnox Scripter',
		formatter_class=argparse.RawDescriptionHelpFormatter,
		epilog="""
	 ___            _                   ___            _        _      
	| __>___  _ _ _| |_ ._ _  ___ __   / __> ___  _ _ <_> ___ _| |_ ___
	| _>/ . \| '_> | |  | ' |/ . \\ \/ \__ \/ | '| '_>| || . \ | | <_-<
	|_| \___/|_|   |_|  |_|_|\___//\_\ <___/\_|_.|_|  |_||  _/ |_| /__/
	                                                     |_|           
	""")
	# Define the arguments
	parser.add_argument(
		'-ci',
		'--create_invoices',
		action='store_true',
		help="""Iterate over all passed invoices and create invoices
				    programmatically. Requires a path to be executed.
				 """
	)
	parser.add_argument(
		'-p',
		'--path',
		type=str,
		help="""Input path."""
	)
	args = parser.parse_args()
	if args.create_invoices :
		if args.path is None :
			raise ValueError('Input path -p most be specified!')
		else :
			create_invoices(args.path)
