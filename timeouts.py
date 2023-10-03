import re


#Read files
with open('output_100.txt', 'r') as file:
    text_1 = file.read()
   
with open('output_1000.txt', 'r') as file:
    text_2 = file.read()

search = "ConnectTimeoutException"

response_time_pattern = r'Response time: (\d+) ms'

# Clients = 100

matches_1 = re.findall(search, text_1)

count_1 = len(matches_1)

response_times_1 = re.findall(response_time_pattern,text_1)

response_times_1 = [int(time) for time in response_times_1]

n_1 = 100
print("***NUMBER OF CLIENTS: " + str(n_1) + "***")
print("Number of timeouts: " + str(count_1))
print("Percentage of timeouts: " + str((count_1/n_1)*100) + " %)")
print(f'Tiempo de respuesta promedio: {sum(response_times_1)/len(response_times_1):.2f} ms')


# Clients = 1000

matches_2 = re.findall(search, text_2)

count_2 = len(matches_2)


response_times_2 = re.findall(response_time_pattern,text_2)

response_times_2 = [int(time) for time in response_times_2]



# Imprime el resultado
n_2 = 1000
print("***NUMBER OF CLIENTS: " + str(n_2) + "***")
print("Number of timeouts: " + str(count_2))
print("Percentage of timeouts: " + str((count_2/n_2)*100) + " %)")
print(f'Tiempo de respuesta promedio: {sum(response_times_2)/len(response_times_2):.2f} ms')



