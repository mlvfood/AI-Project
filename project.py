'''
Authors: Siddhi Venkatesh and Preyanka Sarvendrarajah 
Course: CP468 - Artificial Intelligence 
Title of Program: Covid-19 Dataset Implementation 
Description: This Algorithm focuses on implementing a covid-19 dataset using crticial variables such as:
            1. Country/Region
            2. Confirmed cases 
            3. Active cases 
            4. Number of deaths 
            5. Recovered cases
            6. New cases
            7. New Deaths
            8. New recovered
            9. Death/100 cases rate
            10. Recovered/100 Cases
            11. Region Name
            12. Latitude
            13. Longtitude
'''
#Import the math library 
import math

# Helper Functions
# Creating class node
class Node:
    def __init__(self,value):
        # Initializes node values
        self.value = value 
        self.left = None
        self.right = None
    
    # insert function
    def insert(self,value):
        # Nested If statement to compare value to node and insert appropriately 
        if value != None: # Check to see if value exists
            if value < self.value: # if value is less than node
                if self.left == None:
                    self.left = Node(value) #insert on the left of the node
                else:
                    self.left.insert(value)
            elif value > self.value: # if value is greater than node
                if self.right == None:
                    self.right = Node(value) #insert on the right of the node
                else:
                    self.right.insert(value)
            else: # if value is equal to node
                self.value = value # insert as a new value for the node

#function that implements the numbers of cases per region 
def report_region(data, filename): 
    name = region_name(data) # Retrieves the region name for the selected country

    # Create list
    data = []

    # Initialize variable
    totalCases = 0

    #Opens the file to retrieve data
    with open(filename, 'r+') as file:
        contents = file.readlines()
        # For loop to iterate through each line in the file
        for line in contents:
            data = line.split(",") #Splits line to create a list of values
            if region_name(data) == name: 
                totalCases = totalCases + int(confirmed_cases(data)) # If the region matches the selected region, it adds to the total number of confirmed cases
    return totalCases # Retrieves the total cases in the region

#function that implements the display of the region's name of a country 
def region_name(data):
    return data[14]

#function that implements the display of the country's name
def country_name(data):
    name = data[0]
    return name

#function that implements the confirmed cases in each state 
def confirmed_cases(data):
    ccases = data[1]
    return ccases

#function that implements the active cases in each state 
def active_cases(data):
    acases = data[4]
    return acases

#function that implements the number of deaths in each state 
def deaths(data):
    dcases = data[2]
    return dcases

#function that implements the number of recovered cases in each state 
def recovered(data):
    rcases = data[3]
    return rcases

#function that implements the new cases per country 
def new_cases(data):
    ncases = data[5]
    return ncases

#function that implements the new deaths per country 
def new_deaths(data):
    ndcases = data[6]
    return ndcases

#function that implements the new recoverd cases per country 
def new_recovered(data):
    nrcases = data[7]
    return nrcases

#function that implements the death rate per country 
def death_rate(data):
    dr = data[8]
    return dr

#function that implements the recovery rate per country 
def recovery_rate(data):
    rr = data[9]
    return rr

#function that implements the latitude of a country
def lat_val(data):
    return float(data[15])

#function that implements the longtitude of a country
def long_val(data):
    return float(data[16].strip())

#function reads the file to retrieve country's information
def read_data(filename, num):
    # Creating list
    data = []

    #Initialize variable
    count = 1

    #Opens the file to create list
    with open(filename, 'r+') as file:
        contents = file.readlines()
        # For loop to iterate through each line in the file
        for line in contents:
            if count == num:
                data = line.split(",") #Splits line to create a list of values
                break
            count = count + 1
    return data # returns the country's information

# Hill Climbing Algorithm
#function that implements the most active cases in all countries
def hill_climbing(filename):
    #Intialize variables
    countryone = read_data(filename, 1)
    max = int(active_cases(countryone)) # Initialize the max variable to the first country's active case
    
    # Creating lists
    data = []

    #Opens the file to retrieve data
    with open(filename, 'r+') as file:
        contents = file.readlines()
        # For loop to iterate through each line in the file
        for line in contents:
            data = line.split(",") #Splits line to create a list of values
            ccnum = int(active_cases(data)) # Retrieves the # of active cases for this country
            if max<ccnum: # Check to see if the max value is less than the retrieved value
                max = ccnum  # If the condition is true, assigns the max value to the retrieved value
                name = country_name(data) # Retrieves the country's name that has the most cases
    return max, name # Returns the max value and the country's name that has the most active cases

#Gradient Descent Algorithm
#function that implements the least active cases in all countries
def gradient_descent(filename):
    #Intialize variables
    countryone = read_data(filename, 1)
    min = int(active_cases(countryone))

    # Creating list
    data = []

    #Opens the file to retrieve data
    with open(filename, 'r+') as file:
        contents = file.readlines()
        # For loop to iterate through each line in the file
        for line in contents:
            data = line.split(",") #Splits line to create a list of values
            ccnum = int(active_cases(data)) # Retrieves the # of active cases for this country
            if min>ccnum: # Check to see if the min value is greater than the retrieved value
                min = ccnum # If the condition is true, assigns the min value to the retrieved value
                name = country_name(data) # Retrieves the country's name that has the least cases
    return min, name # Returns the min value and the country's name that has the least cases

#Display the Cluster
#function that implements to gather data for cluster
def gather_data(filename):
    # Creates lists
    data = []
    list = []

    #Opens the file to retrieve data
    with open(filename, 'r+') as file:
        contents = file.readlines()
        # For loop to iterate through each line in the file
        for line in contents:
            list = line.split(",") # Splits line into list to retrieve values
            data.append([float(list[16].strip()),float(list[15])]) # Adds the lat and long values into a list

    return data # Returns the list containing the lat and long values

#function that implements to find the cluster data points
def kmeans(data, k, clusterdata):
    #Initialize the centroids with the first "k" data points 
    centroids = data[:k]  
    
    #while loop to compute the centroids and keep looping until all points are set 
    while True:
        #Assign each observation to the closest centroid 
        labels, clusterdata = add_labels(data, centroids, clusterdata)  

        #Calculate the new centroids 
        new_centroids = calculate_centroids(data, labels, k)
        
        #If statement to validate whether the centroids have converged 
        if centroids == new_centroids: 
            break
        
        centroids = new_centroids

        # Remove all values in the clusterdata list
        for x in range(k):
            clusterdata.pop()
        
        # Create empty list for each group
        for y in range(k):
            clusterdata.append([])
       
    return centroids, clusterdata # Returns centroids, clusterdata

#function that implements the sorting of points
def add_labels(data, centroids, clusterdata):

    #Create an array for labels 
    labels = []
    
    #For loop to go through each element in the data 
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        cluster_index = distances.index(min(distances))  # Index of the closest centroid
        labels.append(cluster_index)

        clusterdata[cluster_index].append(point) #Add the point to it's specific cluster group
    
    return labels, clusterdata # Returns labels and clusterdata

#function that implements the calculation of centroids 
def calculate_centroids(data, labels, k):

    #Create empty array to hold the centroids 
    centroids = []
    
    #For loop to go through each value
    for i in range(k):

        #Data points in the cluster 
        cluster_points = [data[j] for j in range(len(data)) if labels[j] == i]  

        #Calculate the mean of each dimension 
        centroid = [round(sum(dim) / len(cluster_points),2) for dim in zip(*cluster_points)]

        centroids.append(centroid)
    
    return centroids # Return the centroids

#function that implements the calculation of the euclidean distance 
def euclidean_distance(point1, point2):
    return math.sqrt(sum([(x - y) ** 2 for x, y in zip(point1, point2)])) # Returns the calculation of the euclidean distance

#function that implements finding the highest # of actives out of the cluster groups
def find_highest_data(filename,clusterdata):
    # Intialize lists and variable
    activedata = []
    data_list = []

    #Opens file and retrieves data
    with open(filename, 'r+') as file:
        contents = file.readlines()

        for line in contents:
            list = line.split(",") # Splits the line into a list
            data_list.append([long_val(list),lat_val(list), int(active_cases(list))]) # Retrieve the lat and long values as well as # of active cases

    # Finds the total number of active cases per cluster group
    for x in range(6): # Goes through each cluster group
        total = 0 # Intialize the total variable
        for y in range(len(clusterdata[x])): # Goes through each lat and long values in the cluster group
            for z in range(len(data_list)): # Goes through each country's data
                if(clusterdata[x][y][0] == data_list[z][0] and clusterdata[x][y][1] == data_list[z][1]): # Checks to see if the current lat and long value matches the one in the list
                    total = total + data_list[z][2]  # If it is true adds to the total value of # of active cases of that cluster group
                    break
        activedata.append(total) # Adds the total number of active cases for the cluster group to the active data list
    
    # Find the highest number of active cases out of each cluster group
    # Initialize the variables
    highestval = activedata[0] # Intialize the value to the first value in tnhe activedata list
    num = 0
    total = 0
    # Goes through each loop to determine the maximum number of active cases
    for x in range(6):
        total = total + activedata[x] # Calculates the total number of active cases
        if activedata[x]> highestval: # Checks to see if the current total value is greater than the highestval
            highestval = activedata[x] # If it is true, change the highestval to the current total value
            num = x # Changes the cluster group number to the one with the highest number of cases

    return activedata, highestval, num, total # Returns the list of the total number of cases per cluster group, the highest number of active cases, the group number containing the highest number of cases and the total number of active cases

# A function implements a list of data for each country made up of country name, lat and long points and number of active cases 
def read_country_data(filename):
    # Creating lists
    list = [] 
    country_data = []

    # Opens file and retrieves the data
    with open(filename, 'r+') as file:
        contents = file.readlines()

        for line in contents: # Goes through each line of country data
            list = line.split(",") # Splits each line into a list of data 
            country_data.append([country_name(list),lat_val(list),long_val(list), active_cases(list)]) # Finds the country name, the lat and long values and the number of active cases for the country

    return country_data # Returns the country data information

# Calculates the Euclidean distance for all countries
def create_distance_matrix(country_data):
    distance_matrix = [len(country_data)] # Creating a matrix based on the length of the country_data

    # Goes through a loop and calculates the distance between each country
    for i in range(len(country_data)-1):
        distance = math.sqrt((country_data[i+1][1] - country_data[i][1]) ** 2 + (country_data[i+1][2] - country_data[i][2]) ** 2) # Calculates the distance
        distance_matrix.append(distance) # Appends the distance to the matrix
    return distance_matrix # Returns the matrix containing the distances

# Recursive function to display the shortest route to take to travel to all the countries
def dfs(node, set_val, country_data):
    # Intialize the current node 
    current_node = node

    # Checking if the node is None
    if current_node == None: 
        return
    # If it's not None, displays the shortest route
    else:
        # Goes through each country data in the loop
        for x in range(len(country_data)):
            if country_data[x][0] == current_node.value: # Checks to see the current country matches the country in the list
                if int(country_data[x][3]) > set_val: # Checks to see if the current active # of cases is greater the set val
                    print(current_node.value + ": A high clustered country")  # If it is true, then displays it is a high clustered country
                else:
                    print(current_node.value + ": Not a high clustered country") # If it is false, then displays it is not a high clustered country
                break
        dfs(current_node.left, set_val, country_data) 
        dfs(current_node.right, set_val, country_data)

#User Input
#Asks user to select country
print("Hi, please enter a numeric value for the country of choice:")
country = input('''
1. Afghanistan
2. Albania
3. Algeria
4. Andorra
5. Angola
6. Antigua and Barbuda
7. Argentina
8. Armenia
9. Australia
10. Austria
11. Azerbaijan
12. Bahamas
13. Bahrain
14. Bangladesh
15. Barbados
16. Belarus
17. Belgium
18. Belize
19. Benin
20. Bhutan
21. Bolivia
22. Bosnia and Herzegovina
23. Botswana
24. Brazil
25. Brunei
26. Bulgaria
27. Burkina Faso
28. Burma
29. Burundi
30. Cabo Verde
31. Cambodia
32. Cameroon
33. Canada
34. Central African Republic
35. Chad
36. Chile
37. China
38. Colombia
39. Comoros
40. Congo (Brazzaville)
41. Congo (Kinshasa)
42. Costa Rica
43. Cote d'Ivoire
44. Croatia
45. Cuba
46. Cyprus
47. Czechia
48. Denmark
49. Djibouti
50. Dominica
51. Dominican Republic
52. Ecuador
53. Egypt
54. El Salvador
55. Equatorial Guinea
56. Eritrea
57. Estonia
58. Eswatini
59. Ethiopia
60. Fiji
61. Finland
62. France
63. Gabon
64. Gambia
65. Georgia
66. Germany
67. Ghana
68. Greece
69. Greenland
70. Grenada
71. Guatemala
72. Guinea
73. Guinea-Bissau
74. Guyana
75. Haiti
76. Holy See
77. Honduras
78. Hungary
79. Iceland
80. India
81. Indonesia
82. Iran
83. Iraq
84. Ireland
85. Israel
86. Italy
87. Jamaica
88. Japan
89. Jordan
90. Kazakhstan
91. Kenya
92. Kosovo
93. Kuwait
94. Kyrgyzstan
95. Laos
96. Latvia
97. Lebanon
98. Lesotho
99. Liberia
100. Libya
101. Liechtenstein
102. Lithuania
103. Luxembourg
104. Madagascar
105. Malawi
106. Malaysia
107. Maldives
108. Mali
109. Malta
110. Mauritania
111. Mauritius
112. Mexico
113. Moldova
114. Monaco
115. Mongolia
116. Montenegro
117. Morocco
118. Mozambique
119. Namibia
120. Nepal
121. Netherlands
122. New Zealand
123. Nicaragua
124. Niger
125. Nigeria
126. North Macedonia
127. Norway
128. Oman
129. Pakistan
130. Panama
131. Papua New Guinea
132. Paraguay
133. Peru
134. Philippines
135. Poland
136. Portugal
137. Qatar
138. Romania
139. Russia
140. Rwanda
141. Saint Kitts and Nevis
142. Saint Lucia
143. Saint Vincent and the Grenadines
144. San Marino
145. Sao Tome and Principe
146. Saudi Arabia
147. Senegal
148. Serbia
149. Seychelles
150. Sierra Leone
151. Singapore
152. Slovakia
153. Slovenia
154. Somalia
155. South Africa
156. South Korea
157. South Sudan
158. Spain
159. Sri Lanka
160. Sudan
161. Suriname
162. Sweden
163. Switzerland
164. Syria
165. Taiwan
166. Tajikistan
167. Tanzania
168. Thailand
169. Timor-Leste
170. Togo
171. Trinidad and Tobago
172. Tunisia
173. Turkey
174. US
175. Uganda
176. Ukraine
177. United Arab Emirates
178. United Kingdom
179. Uruguay
180. Uzbekistan
181. Venezuela
182. Vietnam
183. West Bank and Gaza
184. Western Sahara
185. Yemen
186. Zambia
187. Zimbabwe
''')

country_num = int(country)
              
#Retrieve file data
filename = "country_wise_latest.csv"
country_data = read_data(filename, country_num) #Gathers the data for the chosen country

#Display the results
print()
print("Confirmed Cases: ", confirmed_cases(country_data))
print("Active Cases: ", active_cases(country_data))
print("Recovered Cases: ", recovered(country_data))
print("Number of deaths: ", deaths(country_data))
print("New Cases: ", new_cases(country_data))
print("New Deaths: ", new_deaths(country_data))
print("New Recovered: ", new_recovered(country_data))
print("Death Rate: ", death_rate(country_data))
print("Recovery Rate: ", recovery_rate(country_data))
print("Region Cases: ", report_region(country_data, filename))

#Display results from finding Steepest Ascent Hill Climbing
num, name = hill_climbing(filename)
print('''Maximum number of cases is '''+ str(num)+''' found in '''+ name)
num, name = gradient_descent(filename)
print('''Minimum number of cases is '''+ str(num)+''' found in '''+ name)
print()

#Display the data points for the cluster of the data
# Create lists for data
data = gather_data(filename)

k = 6 #Since there are 6 regions, k = 6
clusterdata = [] # Create empty list to store each point in its specific group
for x in range(k): 
    clusterdata.append([]) 

centroids, clusterdata = kmeans(data, k, clusterdata) # Calls kmeans function
print("Centroids Points:", centroids) # Display the centroid values
print("Clusterdata Points:", clusterdata) # Display the points in each cluster
print()

activedata, highestactivedata, num, total = find_highest_data(filename, clusterdata) # Find out which cluster has the highest number of active cases

# Displays warning and the cluster group with the highest number of active cases
print('!!Warning: High Active Cases!!')
print('''The highest number of cases is ''' + str(highestactivedata) + ''' and it is found in cluster group ''' + str(num))

print()

# Display the shortest distance and shortest path taken using dfs as well as which country is high clustered
# Retrieve file data
country_data = read_country_data(filename)

# Creates a distance matrix using country_data
distance_matrix = create_distance_matrix(country_data)

# Creates a Node
node = Node(country_data[0][0])

# Inserts each country as a node
for i in range(len(country_data)):
    if i != 0:
        node.insert(country_data[i][0])

# Choosing a set value to see if the number of cases in each cluster is greater
set_val = total / len(country_data)
set_val = int(set_val)

shortd = 0 # A variable that holds the shortest distance for dfs 

# Calculates the shortest distance
for i in range(len(distance_matrix)):
    shortd = shortd + distance_matrix[i]

# Calls depth first search and print which country is a high clustered one
# Display Results
print("The shortest distance using DFS: " + str(shortd))
print()
print("The shortest route using DFS: ")
dfs(node, set_val, country_data)
print()