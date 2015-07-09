import pickle


f = open('moviedata', 'r')
data = pickle.load(f)
f.close()

for key in data:
    data[key]['ratio'] = float(data[key]['worldwide']) / float(data[key]['budget'])

f = open('moviedata', 'w')
pickle.dump(data, f)
f.close()
