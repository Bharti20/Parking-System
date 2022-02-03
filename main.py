import json
import re
import random

main_dic = {'vehicle_details': []}
all_tokens = [1,2,3,4,5,6,7,8,9,10]

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
                            print("User alredy exist")
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
                    json.dump(dic, json_file, indent = 2)
                    json_file.close()
                    print("congrarts", username, "you are Signed Up Successfully")
                
                if(check != 1):
                    userData = {'username': username, 'password': password}
                    all_data['user'].append(userData)
                    my_data = open("agentdetails.json", "w")
                    json.dump(all_data, my_data, indent = 2)
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
        return 'invalid'

def read_json(fname):
    if fname == "location_tokens.json":
        j_data = open("location_tokens.json", "r")
        location_tokens = json.load(j_data)
        j_data.close()
        return location_tokens
    elif fname == 'vehicledetails.json':
        json_data = open('vehicledetails.json', 'r')
        p_data = json.load(json_data)
        json_data.close()
        return p_data
    else:
        return 'Something is wrong'

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
        return 'Somthing is wrong'

def checkIn():
    print()
    print('Welcome to Bharti Mall parking')
    print()
    print('Vehicles and Charge -  1.Motorcycle: 30   2.Car: 50   3.Bus: 70')
    print()
    mobile_no = int(input('Enter your mobile number  '))
    date = input('Enter date    ' )
    time = input('Enter in time ')
    vehicle_no = input('Enter vehicle number...')
    vehicle_type = input('Enter veicle type 1.motorcycle 2. car 3. buses    ')
    p_location_tokens = read_json("location_tokens.json")
    if vehicle_type == '1':
        if len(p_location_tokens["m_location_tokens"]) == 0:
            print('Sorry, Motorcycle slot is full Now. You can try somtime later')
            return
        else:
            parking_slot = 'motorcycle_spots'
            token_no = random.choice(p_location_tokens["m_location_tokens"])
            p_location_tokens['m_location_tokens'].remove(token_no)
            slip_print('motorcycle',vehicle_no, date, time, parking_slot,token_no, 30)
            write_in_json('location_tokens.json', p_location_tokens)
            dic = {'vehicle_type': 'motorcycle', 'Mobile_no': mobile_no,'vehicle_no': vehicle_no, 'Date': date, 'Time': time, 'parking_slot': parking_slot}
            write_in_json('vehicledetails.json',dic)

    elif vehicle_type == '2':
        if len(p_location_tokens["c_location_tokens"]) == 0:
            print('Sorry, car slot is full Now. You can try somtime later')
            return
        else:
            parking_slot = 'car_spots'
            token_no = random.choice(p_location_tokens['c_location_tokens'])
            p_location_tokens['c_location_tokens'].remove(token_no)
            slip_print('Car',vehicle_no, date, time, parking_slot,token_no, 50)
            write_in_json('location_tokens.json', p_location_tokens)
            dic = {'vehicle_type': 'Car', 'Mobile_no': mobile_no,'vehicle_no': vehicle_no, 'Date': date, 'Time': time, 'parking_slot': parking_slot}
            write_in_json('vehicledetails.json',dic)

    elif vehicle_type == '3':
        if len(p_location_tokens["b_location_tokens"]) == 0:
            print('Sorry, Bus slot is full Now. You can try somtime later')
            return
        else:
            parking_slot = 'bus_spots'
            token_no = random.choice(p_location_tokens['b_location_tokens'])
            p_location_tokens['b_location_tokens'].remove(token_no)
            slip_print("Bus",vehicle_no, date, time, parking_slot,token_no, 70)
            write_in_json('location_tokens.json', p_location_tokens)
            dic = {'vehicle_type': 'Bus', 'Mobile_no': mobile_no,'vehicle_no': vehicle_no, 'Date': date, 'Time': time, 'parking_slot': parking_slot}
            write_in_json('vehicledetails.json', dic)
    else:
        print('Invalid input')

def checkout():
    p_location_tokens = read_json("location_tokens.json")
    vehicle_type = input('Enter vehicle type motorcycle/car/buses  ')
    tokens = read_json("location_tokens.json")
    token = int(input('Please give your token number  '))
    print()
    if vehicle_type == 'motorcycle':
        if token in all_tokens and token not in p_location_tokens["m_location_tokens"]:
            tokens["m_location_tokens"].append(token)
            write_in_json('location_tokens.json', tokens)
            print()
            print('Thank you for visit')
        else:
            print('Your Token is wrong, Please Talk with Manager')
    elif vehicle_type == 'car':
        if token in all_tokens and token not in p_location_tokens["c_location_tokens"]:
            tokens["c_location_tokens"].append(token)
            write_in_json('location_tokens.json', tokens)
            print()
            print('Thank you for visit')
        else:
            print('Your Token is wrong,  Please Talk with Manager')
    elif vehicle_type == 'buses':
        if token in all_tokens and token not in p_location_tokens["b_location_tokens"]:
            tokens["b_location_tokens"].append(token)
            write_in_json('location_tokens.json', tokens)
            print()
            print('Thank you for visit')
        else:
            print('Wrong token')
    else:
        print('Your token is wrong, Please Talk with Manager')

def slip_print(vehicle_t, vehicles_n, date, time, parking_slot, token, amount):
    print()
    print('      Parking Slip            ')
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
    elif agent_input == '2':
        outPut = agent_login()
        print()
        if outPut == 'invalid':
            return
        else:
            choose = input('For customer chekin and checkout:- Select in/out ')
            if choose == 'in':
                checkIn()
            elif choose == 'out':
                checkout()
            else:
                print('Enter valid input') 

            while True:
                agent_choice = input('Agent, Do you want to stop working? yes/no    ')
                if agent_choice == 'yes':
                    break 
                elif agent_choice == 'no':
                    choose = input('For customer chekin and checkout:- Select in/out ')
                    if choose == 'in':
                        checkIn()
                    elif choose == 'out':
                        checkout()
                    else:
                        print('Enter valid input')
                else:
                   print('Invalid input')
    else:
        print('please enter correct input')
main()





    









