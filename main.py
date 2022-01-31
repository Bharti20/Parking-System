import json
import re
import random

main_dic = {'vehicle_details': []}

def singup():
    username = input('Please enter your name  ')
    password = input('Please enter password  ')
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
    user_name = input('Enter your username  ')
    password = input('Enter your password   ')
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

def read_json(fname):
    if fname == "total_parking_slots.json":
        j_data = open("total_parking_slots.json", "r")
        t_p_slots = json.load(j_data)
        j_data.close()
        return t_p_slots
    elif fname == "location_tokens.json":
        j_data = open("location_tokens.json", "r")
        location_tokens = json.load(j_data)
        j_data.close()
        return location_tokens
    elif fname == 'vehicledetails.json':
        json_data = open('vehicledetails.json', 'r')
        p_data = json.load(json_data)
        json_data.close()
        return p_data

def write_in_json(fname, data):
    if fname == 'vehicledetails.json':
        all_d = read_json('vehicledetails.json')
        all_d['vehicle_details'].append(data)
        f = open(fname, 'w')
        json.dump(all_d, f , indent = 2)
        f.close()
    elif fname == 'location_tokens.json':
        f = open(fname, 'w')
        json.dump(data, f, indent=2)
        f.close()
    else:
        f = open(fname, 'w')
        json.dump(data, f)
        f.close()

def checkIn():
    print()
    print('Welcome to Bharti Mall parking')
    print()
    print('Vehicle and Charge -  1.Motorcycle: 30   2.Car: 50   3.Bus: 70')
    vehicle_type = input('Enter veicle type 1.motorcycle 2. car 3. buses')
    vehicle_no = input('Enter vehicle number...')
    mobile_no = int(input('Enter your mobile number  '))
    date = input('Enter date' )
    time = input('Enter in time')
    total_parking_slots = read_json("total_parking_slots.json")
    p_location_tokens = read_json("location_tokens.json")
    if vehicle_type == '1':
        if total_parking_slots['motorcycle_spots'] == '0':
            return 'Sorry, Motorcycle slot is full Now. You can try somtime later'
        else:
            parking_slot = 'motorcycle_spots'
            sub_motorCy_s = total_parking_slots['motorcycle_spots'] -1
            total_parking_slots['motorcycle_spots'] = sub_motorCy_s

            write_in_json('total_parking_slots.json',total_parking_slots)

            token_no = random.choice(p_location_tokens["m_location_tokens"])
            p_location_tokens['m_location_tokens'].remove(token_no)
            slip_print('motorcycle',vehicle_no, date, time, parking_slot,token_no, 30)
            write_in_json('location_tokens.json', p_location_tokens)
            dic = {'vehicle_type': 'motorcycle', 'Mobile_no': mobile_no,'vehicle_no': vehicle_no, 'Date': date, 'Time': time, 'parking_slot': parking_slot}
            write_in_json('vehicledetails.json',dic)

    elif vehicle_type == '2':
        if total_parking_slots['car'] == '0':
            return 'Sorry, car slot is full Now. You can try somtime later'
        else:
            parking_slot = 'car_spots'
            sub_car_s = total_parking_slots['car_spots'] -1
            total_parking_slots['car_spots'] = sub_car_s
            write_in_json('total_parking_slots.json',total_parking_slots)
            token_no = random.choice(p_location_tokens['c_location_tokens'])
            p_location_tokens['c_location_tokens'].remove(token_no)
            slip_print('Car',vehicle_no, date, time, parking_slot,token_no, 50)
            write_in_json('location_tokens.json', p_location_tokens)
            dic = {'vehicle_type': 'Car', 'Mobile_no': mobile_no,'vehicle_no': vehicle_no, 'Date': date, 'Time': time, 'parking_slot': parking_slot}
            write_in_json('vehicledetails.json',dic)

    elif vehicle_type == '3':
        if total_parking_slots['bus'] == '0':
            return 'Sorry, Bus slot is full Now. You can try somtime later'
        else:
            parking_slot = 'bus_spots'
            sub_bus_s = total_parking_slots['bus_spots'] -1
            total_parking_slots['bus_spots'] = sub_bus_s
            write_in_json('total_parking_slots.json',total_parking_slots)
            token_no = random.choice(p_location_tokens['b_location_tokens'])
            p_location_tokens['b_location_tokens'].remove(token_no)
            slip_print("Bus",vehicle_no, date, time, parking_slot,token_no, 70)
            write_in_json('location_tokens.json', p_location_tokens)
            dic = {'vehicle_type': 'Bus', 'Mobile_no': mobile_no,'vehicle_no': vehicle_no, 'Date': date, 'Time': time, 'parking_slot': parking_slot}
            write_in_json('vehicledetails.json', dic)
    else:
        print('Invalid input')

def checkout():
    vehicle_type = input('Enter vehicle type motorcycle/car/buses  ')
    tokens = read_json("location_tokens.json")
    token = int(input('Please give your token number'))
    if vehicle_type == 'motorcycle':
        tokens["m_location_tokens"].append(token)
        write_in_json('location_tokens.json', tokens)
    elif vehicle_type == 'car':
        tokens["c_location_tokens"].append(token)
        write_in_json('location_tokens.json', tokens)
    elif vehicle_type == 'buses':
        tokens["b_location_tokens"].append(token)
        write_in_json('location_tokens.json', tokens)
    else:
        print('Enter valid token')

def slip_print(vehicle_t, vehicles_n, date, time, parking_slot, token, amount):
    print()
    print('        Parking Slip            ')
    print()
    print('vehicle_type : ', vehicle_t)
    print('Vehicle number: ', vehicles_n)
    print('Date : ', date)
    print('Time:', time)
    print('Parking slot: ', parking_slot)
    print('Location token :', token)
    print('Amount :', amount)
    print()

def main():
    parking_spots = ['motorcycle_spots', 'car_spots','bus_spots' ]
    agent_input = input('For signup press 1 or For login press 2.  ')
    if agent_input == '1':
        singup()
    else:
        agent_login()
        print()
        choose = input('Select in/out ')
        if choose == 'in':
            checkIn()
        elif choose == 'out':
            checkout()
        else:
            print('Enter valid input')
main()






    









