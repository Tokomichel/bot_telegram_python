import pickle
# lecture ecriture

def put(obj):
    with open("bd.txt", 'wb') as b:
        pickle.dump(obj, b) 

def get():
    with open("bd.txt", 'rb') as b:
        o = pickle.load(b)
        print(o)
    
    return o

if __name__ == "__main__":
    obj = {"nom": "Toko", "age": 15}
    with open("bd.txt", 'rb') as b:
        o = pickle.load(b)
        print(f"{o[0].user_name}\n {o[0].u_data}\n {o[0].r_data}")