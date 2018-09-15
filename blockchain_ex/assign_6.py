import json, pickle

json_file_name = 'assign_6.txt'
pickle_fn = 'pickle.dat'

def write_to_file(text):
    file_r = open(json_file_name, mode='r')
    file_contents = file_r.readline()
    file_r.close()
    if file_contents == '':
        file_contents = '{"text": []}'
    data = json.loads(file_contents)
    data['text'].append(text)
    file_w = open(json_file_name, mode='w')
    file_w.write(json.dumps(data))
    file_w.close()
        

def display_file():
    with open(json_file_name, mode='r') as file:
        file_contents = file.readline()
        data = json.loads(file_contents)
        for line in data['text']:
            print(line)


def write_with_pickle(text):
    pickle_file = open(pickle_fn, 'rb')
    try:
        file_content = pickle.loads(pickle_file.read())
    except:
        file_content = []
    file_content.append(text)
    pickle_file.close()
    pickle_file_w = open(pickle_fn, 'wb')
    pickle.dump(file_content, pickle_file_w)
    pickle_file_w.close()


def display_pickle_file():
    pickle_file = open(pickle_fn, 'rb')
    file_content = pickle.loads(pickle_file.read())
    for line in file_content:
        print(line)
    pickle_file.close()

loop = True

while loop:
    choice = input('Enter:\n1 to write to text file,\n2 to display text file contents,\n3 to write with pickle\n4 to display pickle file contents\nAny other key to quit:\n')
    if choice == '1':
        text = input("Enter text to write to text file:\n")
        write_to_file(text)
    elif choice == '2':
        display_file()
    elif choice == '3':
        text = input("Enter text to write to text file:\n")
        write_with_pickle(text)
    elif choice == '4':
        display_pickle_file()
    else:
        loop = False