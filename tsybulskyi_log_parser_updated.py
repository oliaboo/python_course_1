import time
import datetime

def log_to_dictionary(file):
	log_dict = {}
	i = 1
	with open(file) as f:
		for line in f.readlines():
			log_dict[i] = line.split(' ')
			i += 1
	return log_dict

def filter_by_time(log_dict, from_time = 0, to_time = 0):
	if to_time == 0:
		to_time = time.time()
	else:
		to_time = time.mktime(datetime.datetime.strptime(to_time, "%d/%b/%Y:%H:%M:%S").timetuple())
	if from_time != 0:
		from_time = time.mktime(datetime.datetime.strptime(from_time, "%d/%b/%Y:%H:%M:%S").timetuple())
	filtered_log_dict = {}
	n = 1
	for i in log_dict:
		log_time = time.mktime(datetime.datetime.strptime(log_dict[i][3].replace('[',''), "%d/%b/%Y:%H:%M:%S").timetuple())
		if from_time < log_time and to_time > log_time:
			filtered_log_dict[n] = log_dict[i]
			n += 1
	return filtered_log_dict

def filter_by_code(log_dict, code = 200):
	filtered_log_dict = {}
	n = 1
	for i in log_dict:
		if str(code) in log_dict[i]:
			filtered_log_dict[n] = log_dict[i]
			n += 1
	return filtered_log_dict

def filter_by_sum_last_elements(log_dict, min_sum = 0, max_sum = 20):
	filtered_log_dict = {}
	n = 1
	if max_sum == 0 or min_sum >= max_sum:
		return log_dict
	else:
		for i in log_dict:
			log_sum = 0
			for e in str(log_dict[i][-1].replace('\n', '')):
				log_sum += int(e)
			if log_sum >= min_sum and log_sum <= max_sum:
				filtered_log_dict[n] = log_dict[i]
				n += 1
		return filtered_log_dict

def filter_by_ip_address(log_dict, ip_addr = '0.0.0.0'):
	if ip_addr == '0.0.0.0':
		return log_dict
	else:
		filtered_log_dict = {}
		n = 1
		for i in log_dict:
			if log_dict[i][0] == ip_addr:
				filtered_log_dict[n] = log_dict[i]
				n += 1
		return filtered_log_dict

def print_dictionary(log_dict):
	for i in log_dict:
		print(i, ": ", log_dict[i])


dict = filter_by_ip_address(filter_by_sum_last_elements(filter_by_code(filter_by_time(log_to_dictionary('log.txt'),from_time = '07/Mar/2004:16:10:00', to_time = '07/Mar/2004:17:20:00'), code=200), min_sum = 0, max_sum = 20), ip_addr = '64.242.88.10')

print_dictionary(dict)