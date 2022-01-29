import json
import re


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
    agent_input = input('For signup press 1 or For login press 2.  ')
    if agent_input == '1':
        singup()
    else:
        agent_login()
main()





