import datetime
current_date_time = str(datetime.datetime.now()).replace(" ", "-").split('.')[0]
log_file = '\\logs\\' + current_date_time + '.log'
print(log_file)
print(current_date_time.split('.')[0])