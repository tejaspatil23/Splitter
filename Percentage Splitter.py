import numpy as np
import sys

n = int(input("How many components are in your system? "))

entering_streams = []
rows_in = int(input("How many streams are entering your system? "))
for w in range(rows_in):
    stream_in = []
    for i in range(n):
        flow_rate = float(input('In entering stream ' + str(w+1) + ', enter the flowrate of component ' + str((i+1)) + ' :'))
        stream_in.append(flow_rate)
    stream_in = np.asarray(stream_in)
    entering_streams.append(stream_in)

entering_streams = np.transpose(np.asarray(entering_streams))
entering_streams = np.vstack(entering_streams)
entering_array = entering_streams.sum(axis = 1)
entering_array = entering_array.reshape(-1,1)

percentage_out = []
rows_out = int(input("How many streams are exiting your system? "))
for w in range(rows_out):
    percent = float(input('Enter the percentage split of exiting stream ' + str(w+1) + ': ')) / 100
    percentage_out.append(percent)

counter = 0
for i in percentage_out:
    counter += i
if counter != 1:
    sys.exit("Inputted percentages do not add up to 100!")

percentage_out = np.asarray(percentage_out)

exiting_streams = np.multiply(entering_array, percentage_out)
print("The exiting streams are presented in the array where each row corresponds to",
      "the components in the system and each column corresponds to the exiting streams respectively.")
print(exiting_streams)

