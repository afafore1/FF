from Tkinter import *
import json

class California():

    def loadJSON(self):
        with open('ca.json') as data_file:
            data = json.load(data_file)
            informationDict = {}
            for i in data:
                informationDict[i['name']] =  [i['full_county_name'], i['primary_latitude'], i['primary_longitude']]
            return informationDict

    def getCityOptions(self, informationDict):
        cityOption = []
        for key in informationDict:
            cityOption.append(key)
        return cityOption

    def toggleTextBoxState(self, toggle):
        if toggle == 1:
            txtCounty.config(state='normal')
            txtLatitude.config(state="normal")
            txtLongitude.config(state="normal")
        elif toggle == 0:
            txtCounty.config(state='disabled')
            txtLatitude.config(state="disabled")
            txtLongitude.config(state="disabled")

    def onOptionMenuSelect(self, value):
        valueList = informationDict.get(value)

        #get the values
        county = valueList[0]
        latitude = valueList[1]
        longitude = valueList[2]

        #make textbox editable
        self.toggleTextBoxState(1)

        #clear all text in textbox
        txtCounty.delete(1.0, END)
        txtLatitude.delete(1.0, END)
        txtLongitude.delete(1.0, END)

        #insert values, some values are null so check for that.
        if county != None:
            txtCounty.insert(END, county)
        if latitude != None:
            txtLatitude.insert(END, latitude)
        if longitude != None:
            txtLongitude.insert(END, longitude)

        #make textbox uneditable
        self.toggleTextBoxState(0)

california = California()
root = Tk()
root.title("City Information")
lblCity = Label(root, text="City")
lblCounty = Label(root, text="County")
lblLatitude = Label(root, text="Latitude")
lblLongitude = Label(root, text="Longitude")

lblCity.grid(row=0)
lblCounty.grid(row=1)
lblLatitude.grid(row=2)
lblLongitude.grid(row=3)

txtCounty = Text(root, state='disabled', width=44, height=1)
txtLatitude = Text(root, state='disabled', width=44, height=1)
txtLongitude = Text(root, state='disabled', width=44, height=1)

txtCounty.grid(row=1, column=1)
txtLatitude.grid(row=2, column=1)
txtLongitude.grid(row=3, column=1)

informationDict = california.loadJSON()
cityOption = california.getCityOptions(informationDict)

var = StringVar(root)
defaultCity = cityOption[0]
var.set(defaultCity)
#initial filling
california.onOptionMenuSelect(defaultCity)
option = OptionMenu(root, var, *cityOption, command= california.onOptionMenuSelect)
option.config(width=53, height=1)
option.grid(row=0, column=1)
root.mainloop()

