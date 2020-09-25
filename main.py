'''

Name: Andrea Napoli-Wilson
Class: CIS 250
Date: 9/25/2020
Project name: Task 2--Draft Program in a .py File

INSTRUCTIONS:
X = "done"
X Create a Python Application which asks the user for their zip code or city.
X Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
X Display the weather forecast in a readable format to the user.
X Use comments within the application where appropriate in order to document what the program is doing.
X Use functions including a main function.
X Allow the user to run the program multiple times.
X Validate whether the user entered valid data. If valid data isn’t presented notify the user.
X Use the Requests library in order to request data from the webservice.
X Use Python 3.
X Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful.
Deliverables (More detail on these deliverables is provided in the the weeks they are due):
'''

# Python program to find current
# weather details of any city
# using openweathermap api
# import required modules


import requests

def fer(k):
    """return Kelvin to Fahrenheit"""
    f = (9/5) * (k - 273) + 32
    return f


def get_data(url, zip=None, city=None):
    # base_url variable to store url
    #open_weather = "http://api.openweathermap.org/data/2.5/weather"
    #apiid = "cba7fee375a53b5fde82e6dda8ce69a1"
# check if user gave you the zip or the city

  if zip is not None:
    #us at the end for USA
      url += "&zip="+str(zip)+",us"
  else:
      #url += "&q="+str(city)+",us"
      url += "&q="+city
      #url += "&apiid="+str(apiid)
  #make get requests using request module
  r = requests.get(url)

  #return response
  return r

def itworks(resp):
    #print(resp)
    if resp.status_code == 200:
        data = resp.json()
        #print(data['name'])
        #print("""{data['name']} Weather Forecast:
        #There will be {data['weather'][0]['description']} with wind speed of {data['wind']['speedf']}.
        #Visibility will be {data['visibility']}.
        #Min. Temp will be {data{['main']['temp_min']} and max will be {data['main']['temp_nax']}.
        #""")
        #print(data)
        my_str="""
{name} Weather Forecast:
There will be {description} with wind speed of {windspeed}.
Visibility will be {visibility}.
Min. Temp will be {temp_min:.2f} and max will be {temp_max:.2f}.""".format(name=data['name'],description=data['weather'][0]['description'], windspeed=data['wind']['speed'], visibility=data['visibility'], temp_min=fer(data['main']['temp_min']), temp_max=fer(data['main']['temp_max']))
        print(my_str)
    else:
        print("Request not valid, try again: ",resp)

def main():

    #Enter your API key here
    apiid = "cba7fee375a53b5fde82e6dda8ce69a1"

    # base_url variable to store url
    apiurl = "http://api.openweathermap.org/data/2.5/weather?appid=" + apiid

    while (True):
    #show choices
        inp =int(input("Please select one :\n1. Zip Code\n2. City Name\n3. Exit\n"))

        if inp == 1:
            dataZip=input("Please enter the zip code: ")
            dataZip = dataZip.strip()
            if len(dataZip) != 5:
                print("Please enter a 5-digit zip code")
                continue
            try:
                # See if it can be converted to an integer.
                # Don't use the converted value, but error if it can't be converted.
                test = int(dataZip)
                resp= get_data(apiurl,dataZip,None)
                itworks(resp)
            except Exception as ex:
                print("Error : ",ex)
        elif inp == 2:

            dataZip = input("Please enter city name :")
        
            try:    
                resp= get_data(apiurl,None,dataZip)
                itworks(resp)
            except Exception as ex:
                print("Error :",ex)
        elif inp==3:
            break
        else:
            print("Invalid, please try again..\n")


if __name__ =="__main__":
    main()
