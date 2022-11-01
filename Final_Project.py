# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Josh Basker
# Section:      465, 561
# Assignment:   Final Project
# Date:         12/7/2021

import numpy as np
import matplotlib.pyplot as plt


#fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(20,10))

numericals = []
countries = []
consumer_data = []
with open ("EnergyConsumers.txt") as f:
    for line in f:
        consumer_data.append(line.split("\t"))
consumers = np.array(consumer_data)
del consumer_data[0:3]
years1 = consumers[2]

#print(consumers)
for i in range(len(consumer_data)):
        for y in range(27):
            if y!= 0:
                numericals.append(float(consumer_data[i][y]))
    
    
#print(numericals)
plt.hist(numericals, bins = 150)
#plt.xlabel("Countries")
plt.ylabel("Energy Consumption")
plt.title("Total Energy Consumption per year")
#plt.legend()
plt.savefig("figure_1.png")
plt.close()
#print(consumer_data[0])


    
xp = []
yp = []
nums = 44
EnergyType = []
Natural_Gas = []
Electricity = []
total_electric = 0
total_naturalgas = 0
Electricity1 = []
years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
         2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
         2012, 2013, 2014, 2015]

with open ("EnergyRawDataFinal.txt") as f:
    for line in f:
        EnergyType.append(line.split(","))
#print(EnergyType[1])

for type in range(len(EnergyType)):
    if EnergyType[type][2] == "Electricity":
        Electricity.append(EnergyType[type])
       # total_electric += EnergyType[type][1]
        
    elif EnergyType[type][2] == "Natural Gas":
        Natural_Gas.append(EnergyType[type])
       # total_naturalgas += EnergyType[type][1]

def Year_List(list1):
    var1990 = []
    var1991 = []
    var1992 = []
    var1993 = []
    var1994 = []
    var1995 = []
    var1996 = []
    var1997 = []
    var1998 = []
    var1999 = []
    var2000 = []
    var2001 = []
    var2002 = []
    var2003 = []
    var2004 = []
    var2005 = []
    var2006 = []
    var2007 = []
    var2008 = []
    var2009 = []
    var2010 = []
    var2011 = []
    var2012 = []
    var2013 = []
    var2014 = []
    var2015 = []
    nums = []
    for i in range(len(list1)):
        if int(list1[i][3]) == 1990:
            var1990.append(float(list1[i][1]))
        elif int(list1[i][3]) == 1991:
            var1991.append(float(list1[i][1]))
        elif int(list1[i][3]) == 1992:
            var1992.append(float(list1[i][1]))
        elif int(list1[i][3]) == 1993:
            var1993.append(float(list1[i][1]))
        elif int(list1[i][3]) == 1994:
            var1994.append(float(list1[i][1]))
        elif int(list1[i][3]) == 1995:
            var1995.append(float(list1[i][1]))
        elif int(list1[i][3]) == 1996:
            var1996.append(float(list1[i][1]))
        elif int(list1[i][3]) == 1997:
            var1997.append(float(list1[i][1]))
        elif int(list1[i][3]) == 1998:
            var1998.append(float(list1[i][1]))
        elif int(list1[i][3]) == 1999:
            var1999.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2000:
            var2000.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2001:
            var2001.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2002:
            var2002.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2003:
            var2003.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2004:
            var2004.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2005:
            var2005.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2006:
            var2006.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2007:
            var2007.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2008:
            var2008.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2009:
            var2009.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2010:
            var2010.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2011:
            var2011.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2012:
            var2012.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2013:
            var2013.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2014:
             var2014.append(float(list1[i][1]))
        elif int(list1[i][3]) == 2015:
             var2015.append(float(list1[i][1]))
    
    nums.append(np.sum(var1990))
    nums.append(np.sum(var1991))
    nums.append(np.sum(var1992))
    nums.append(np.sum(var1993))
    nums.append(np.sum(var1994))
    nums.append(np.sum(var1995))
    nums.append(np.sum(var1996))
    nums.append(np.sum(var1997))
    nums.append(np.sum(var1998))
    nums.append(np.sum(var1999))
    nums.append(np.sum(var2000))
    nums.append(np.sum(var2001))
    nums.append(np.sum(var2002))
    nums.append(np.sum(var2003))
    nums.append(np.sum(var2004))
    nums.append(np.sum(var2005))
    nums.append(np.sum(var2006))
    nums.append(np.sum(var2007))
    nums.append(np.sum(var2008))
    nums.append(np.sum(var2009))
    nums.append(np.sum(var2010))
    nums.append(np.sum(var2011))
    nums.append(np.sum(var2012))
    nums.append(np.sum(var2013))
    nums.append(np.sum(var2014))
    nums.append(np.sum(var2015))
    return nums
    
thinggy = Year_List(Electricity)      
stuffy = Year_List(Natural_Gas)
#print(Natural_Gas)   
#print(len(yp))
#print(len(xp))
#print(var2001)
plt.plot(years, thinggy, label = "Electricty")
plt.plot(years, stuffy, label = "Natural Gas")

plt.xlabel("Years")
plt.ylabel("Energy Consumption")
plt.title("Natural Gas vs Electricity")
plt.legend()
#plt.show()
plt.savefig("figure_2.png")
plt.close()


industrial_usage_before = []
industrial_usage_after = []
for i in range(len(consumer_data)):
    for y in range(26):
        if y != 0:
            if y <= 10:
                industrial_usage_before.append(0.15 * float(consumer_data[i][y]))
            else:
                industrial_usage_after.append(0.35 * float(consumer_data[i][y]))

#print(industrial_usage)

plt.hist(industrial_usage_before, bins = 50, alpha=0.5,label='Before 2000')
  
plt.hist(industrial_usage_after,bins = 50, alpha=0.5, label='After 2000')
  
plt.legend(loc='upper right')
plt.title('Industrial Usage before and after 2000')
#plt.xlabel("Countries")
plt.xlabel("Industrial Usage")
plt.legend()
plt.savefig("figure_3.png")
plt.close()
  
China = []

for i in range(len(consumer_data)):
    if consumer_data[i][0] == "China":
        for y in range(27):
            if y!= 0:
                China.append(float(consumer_data[i][y]))
            
#print(China)
plt.hist(China, bins = 20)
plt.title('Energy Consumption of China')
#plt.ylabel("Countries")
plt.xlabel("Energy Consumption")
#plt.legend()
plt.savefig("figure_4.png")
plt.close()

countries = ["Europe", "North America", "South America", 
             "Asia", "Africa", "Middle East"]
Europe = []
North_America = []
South_America = [consumer_data[20], consumer_data[21], consumer_data[22], 
                 consumer_data[23], consumer_data[25]]
Asia = [consumer_data[26], consumer_data[27], consumer_data[28], 
                 consumer_data[29], consumer_data[30], consumer_data[31],
                 consumer_data[32], consumer_data[33], consumer_data[34],
                 consumer_data[35]]
Africa = [consumer_data[36], consumer_data[37], consumer_data[38], 
          consumer_data[39]]
Middle_East = [consumer_data[41], consumer_data[42], consumer_data[43]]

for i in range(len(consumer_data)):
    if consumer_data[i][0] == 'United States':
        North_America.append(consumer_data[i])
    elif consumer_data[i][0] == 'Canada':
        North_America.append(consumer_data[i])
    elif consumer_data[i][0] == 'Mexico':
         North_America.append(consumer_data[i])
#     elif consumer_data[i][0] == 'Turkey':
#         Europe.append(consumer_data[i])
#     elif consumer_data[i][0] == 'Turkey':
#         Europe.append(consumer_data[i])

for i in range(14):
    Europe.append(consumer_data[i])

Asia.append(consumer_data[15])
Asia.append(consumer_data[14])
Asia.append(consumer_data[16])
Asia.append(consumer_data[17])

continent_total = []

def total_continent(list1):
    residential_usage_before = []
    residential_usage_after = []
    list_total = []
    for i in range(len(list1)):
        for y in range(26):
            if y != 0:
                if y <= 10:
                    residential_usage_before.append(0.85 * float(list1[i][y]))
                else:
                    residential_usage_after.append(0.65 * float(list1[i][y]))
    list_total = [residential_usage_before, residential_usage_after]
    return list_total

residential_usage_before = []
residential_usage_after = []

residential_usage_before.append(np.sum(total_continent(Europe)[0]))
residential_usage_after.append(np.sum(total_continent(Europe)[1]))
residential_usage_before.append(np.sum(total_continent(Asia)[0]))
residential_usage_after.append(np.sum(total_continent(Asia)[1]))
residential_usage_before.append(np.sum(total_continent(North_America)[0]))
residential_usage_after.append(np.sum(total_continent(North_America)[1]))
residential_usage_before.append(np.sum(total_continent(South_America)[0]))
residential_usage_after.append(np.sum(total_continent(South_America)[1]))
residential_usage_before.append(np.sum(total_continent(Middle_East)[0]))
residential_usage_after.append(np.sum(total_continent(Middle_East)[1]))
residential_usage_before.append(np.sum(total_continent(Africa)[0]))
residential_usage_after.append(np.sum(total_continent(Africa)[1]))

residential_usage = residential_usage_before + residential_usage_after

plt.hist(residential_usage_before, bins = 10, alpha=0.5,label='Before 2000')
  
plt.hist(residential_usage_after,bins = 10, alpha=0.5, label='After 2000')

plt.legend(loc='upper right')
plt.title('Residential Usage per continent, per year')
#plt.xlabel("Countries")
plt.xlabel("Residential Usage")
plt.legend()
plt.savefig("figure_5.png")
plt.close()

CarbonEmissions = []
nations = []
carbon_nations = [1, 2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9, 0]
carbon_stuff = []

with open ("CarbonEmissions.txt") as f:
    for line in f:
        CarbonEmissions.append(line.split("\t"))
del CarbonEmissions[0]

for i in range(len(CarbonEmissions)):
    nations.append(CarbonEmissions[i][1])
    carbon_stuff.append(float(CarbonEmissions[i][2]))

#print(nations)


for i in range(len(consumer_data)):
    if consumer_data[i][0] == 'China':
       carbon_nations[0] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'United States':
     carbon_nations[1] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'India':
     carbon_nations[2] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'Russia':
     carbon_nations[3] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'Japan':
     carbon_nations[4] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'Germany':
     carbon_nations[5] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'South Korea':
     carbon_nations[6] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'Iran':
     carbon_nations[7] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'Canada':
     carbon_nations[8] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'Saudi Arabia':
     carbon_nations[9] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'Brazil':
     carbon_nations[10] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'Mexico':
     carbon_nations[11] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'Indonesia':
     carbon_nations[12] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'South Africa':
     carbon_nations[13] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'United Kingdom':
     carbon_nations[14] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'Australia':
     carbon_nations[15] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'Italy':
     carbon_nations[16] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'Turkey':
     carbon_nations[17] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'France':
     carbon_nations[18] = (float(consumer_data[i][26]))
    elif consumer_data[i][0] == 'Poland':
      carbon_nations[19] = (float(consumer_data[i][26]))
        
#carbon_nations_data = []    

# for i in range(len(carbon_nations)):
#     for y in range(27)
#         if y != 0:
#             carbon_nations_data.append(np.sum)
            
  
X_axis = np.arange(len(nations))
  
plt.bar(X_axis - 0.2, carbon_nations, 0.4, label = 'Carbon Emissions')
plt.bar(X_axis + 0.2, carbon_stuff, 0.4, label = 'Energy Consumption')


plt.xticks(X_axis, nations)
plt.xlabel("Countries")
plt.ylabel("Million Metric Tons")
plt.title("Carbon Emissions vs Energy Consumption in 2015")
plt.legend()
plt.savefig("figure_6.png")
plt.close()
#plt.show()
    
# carbon_nations.append(consumer_data[26])
# carbon_nations.append(consumer_data[43])
# carbon_nations.append(consumer_data[26])

print("USA is the number 1 energy consumer and is in North America.")
print("China is the number 2 energy consumer and is in Asia.")
print("India is the number 3 energy consumer and is in Asia.")




