import sys

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

types = {}
records = {}

def sortType(type_name):
	return type_name.lower()

def sortPrimary(record_fields): 
    return record_fields[0]

with open(output_file_name, 'w') as output_file:
	with open(input_file_name, 'r') as input_file:
		for eachline in input_file:
			operation = eachline.rstrip().split()
			
			action = operation[0]
			type = operation[1]
			
			if action != "list" or type != "type":
				type_name = operation[2]
			
			# DDL Operation
			if type == "type":
				
				# Create
				if action == "create":
				
					field_number = operation[3]
					field_names = operation[4:]
					
					types[type_name] = field_names
					records[type_name] = {}
					
					#print(action, type, type_name, field_number, field_names)
				
				# Delete
				elif action == "delete":
					
					del types[type_name]
					del records[type_name]
					
					#print(action, type, type_name)

				# List
				else:
					sorted_types = sorted(types.keys(), key =sortType)
					for each_type in sorted_types:
						output_file.write(each_type + '\n')
					#print(action, type)
					
			# DML Operation
			else:
				
				if action != "create" and action != "list":
					primary_key = operation[3] 
					
				# Create
				if action == "create":
					field_values = operation[3:]
					records[type_name][field_values[0]] = field_values
					# print(action, type, type_name, field_values)
				# Delete
				elif action == "delete":
					del records[type_name][primary_key]
					# print(action, type, type_name, primary_key)
				# Update
				elif action == "update":
					field_values = operation[3:]
					records[type_name][primary_key] = field_values
					# print(action, type, type_name, primary_key, field_values)
				# Search
				elif action == "search":
					if type_name in records and primary_key in records[type_name]:
						for each_field in records[type_name][primary_key]:
							output_file.write(each_field + ' ')
						output_file.write('\n')
					# print(action, type, type_name, primary_key)
				# List
				else:
					sorted_records = sorted(records[type_name].values(), key = sortPrimary)
					for each_record in sorted_records:
						for each_field in each_record:
							output_file.write(each_field + ' ')
						output_file.write('\n')

					# print(action, type, type_name)
			
			#print(eachline.rstrip())
			#print(types)
			#print(records)
			#print()