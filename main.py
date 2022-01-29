import json
import re
import random

motorCy_parking_charge = 30
car_parking_charge = 50
bus_parking_charge = 70

# total_parking_slots = {'motorcycle_spots': 20, 'car_spots':20,'bus_spots':20 }
m_location_tokens = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
c_location_tokens = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b_location_tokens = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def singup():
    username = input('Please enter your name ')
    password = input('Please enter password ')
    confirm_password = input('Re-enter your password  ')
    dic  = {'user':[]}
    userData = {'username':"", 'password':""}
    check = 0
    if password == confirm_password:
        if "#" in password or "@" in password:
            if re.findall(r"^\w+",password):
                try:
                    json_data=open("agentdetails.json", "r")
                    all_data=json.load(json_data)
                    json_data.close()
                    i = 0
                    while i<len(all_data["user"]):
                        a=(all_data["user"][i])
                        if a["username"] == username:
                            print("alredy exist")
                            check = 1
                            break
                        i=i+1
                except:
                    check = 1
                    userData['username'] = username
                    userData['password'] = password
                    print(userData)
                    dic['user'].append(userData)
                    print(dic)
                    json_file = open("agentdetails.json", "w")
                    json.dump(dic, json_file)
                    json_file.close()
                    print("congrarts", username, "you are Signed Up Successfully")
                
                if(check != 1):
                    userData = {'username': username, 'password': password}
                    all_data['user'].append(userData)
                    my_data = open("agentdetails.json", "w")
                    json.dump(all_data, my_data)
                    my_data.close()
                    print("congrarts", username, "you are Signed Up Successfully")
            else:
                print('Atleast password should contain one special character and on number')
        else:
            print('Atleast password should contain one special character and on number')
    else:
        print('Both password are not same')

def agent_login():
    user_name = input('Enter your username ')
    password = input('Enter your password  ')
    jsonData = open("agentdetails.json", "r")
    allData = json.load(jsonData)
    i = 0
    while i < len(allData['user']):
        if allData['user'][i]['username'] == user_name and allData['user'][i]['password']:
            print("You are logged in sucessfully")
            break
        i = i +1  
    else:
        print("Invalid username and password")

def main():
    parking_spots = ['motorcycle_spots', 'car_spots','bus_spots' ]
    agent_input = input('For signup press 1 or For login press 2.  ')
    if agent_input == '1':
        singup()
    else:
        agent_login()
        
        print()
        choose = input('Select in/out')
main()

def read_json(fname):
    if fname == "total_parking_slots.json":
        j_data = open("total_parking_slots.json", "r")
        t_p_slots = json.load(j_data)
        j_data.close()
        return t_p_slots
    else:
        j_data = open("location_tokens.json", "r")
        location_tokens = json.load(j_data)
        j_data.close()
        return location_tokens




def checkIn():
    print()
    print('Welcome to Bharti Mall parking')
    print()
    print('Vehicle and Charge -  1.Motorcycle: 30   2.Car: 50   3.Bus: 70')
    vehicle_type = input('Enter veicle type 1.motorcycle 2. car 3. buses')
    vehicle_no = input('Enter vehicle number...')
    mobile_no = int(input('Enter your mobile number  '))
    total_parking_slots = read_json("total_parking_slots.json")
    p_location_tokens = read_json("location_tokens.json")
    if vehicle_type == '1':
        if total_parking_slots['motorcycle_spots'] == '0':
            return 'Sorry, Motorcycle slot is full Now. You can try somtime later'
        else:
            sub_motorCy_s = total_parking_slots['motorcycle_spots'] -1
            total_parking_slots['motorcycle_spots'] = sub_motorCy_s
            token_no = random.choice(p_location_tokens["m_location_tokens"])
            m_location_tokens.remove(token_no)

    elif vehicle_type == '2':
        if total_parking_slots['car'] == '0':
            return 'Sorry, car slot is full Now. You can try somtime later'
        else:
            sub_car_s = total_parking_slots['car_spots'] -1
            total_parking_slots['car_spots'] = sub_car_s
            token_no = random.choice(c_location_tokens)
            c_location_tokens.remove(token_no)
    elif vehicle_type == '3':
        if total_parking_slots['bus'] == '0':
            return 'Sorry, Bus slot is full Now. You can try somtime later'
        else:
            sub_bus_s = total_parking_slots['bus_spots'] -1
            total_parking_slots['bus_spots'] = sub_bus_s
            token_no = random.choice(b_location_tokens)
            b_location_tokens.remove(token_no)
    else:
        print('Invalid input')





    









