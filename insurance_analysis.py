import csv
import matplotlib.pyplot as pl

#lists for all attributes of the insurance data

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

# function to load csv data into a particular list:

def ins_dict_list(lst, csv_file, column_name):
	with open(csv_file) as csv_import:
		csv_dict = csv.DictReader(csv_import)
		for row in csv_dict:
			lst.append(row[column_name])
	return lst


# Now we can load the data from the csv file into the 7 lists very efficiently:

ins_dict_list(ages, "insurance.csv", "age")
ins_dict_list(sexes, "insurance.csv", "sex")
ins_dict_list(bmis, "insurance.csv", "bmi")
ins_dict_list(num_children, "insurance.csv", "children")
ins_dict_list(smoker_statuses, "insurance.csv", "smoker")
ins_dict_list(regions, "insurance.csv", "region")
ins_dict_list(insurance_charges, "insurance.csv", "charges")

# Now that the lists have been organized for each column in the csv file, we can perform analysis of the data. We will perform the following operations on the data:
# find average age of the patients
# find the number of males and females in the population
# find the distribution of the regions of the patients
# find the distribution of the geographical location of the patients
# find the average yearly medical costs of the patients
# find average costs for male patients
# find average costs for female patients
# create a dictionary to store all patient information

# A InfoMaker class has been created that will implement these methods.

class InfoMaker:
	#constructor that takes in all lists previously found.
	def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses, patients_regions, patients_charges):
		self.patients_ages = patients_ages
		self.patients_sexes = patients_sexes
		self.patients_bmis = patients_bmis
		self.patients_num_children = patients_num_children
		self.patients_smoker_statuses = patients_smoker_statuses
		self.patients_regions = patients_regions
		self.patients_charges = patients_charges
	def average_age(self):
		count = 0
		total_age = 0
		for age in self.patients_ages:
			count += 1
			total_age += int(age)
		print("The average age of the sample is {} years old.".format(total_age / count))
	def males_and_females(self):
		male = 0
		female = 0
		for sex in self.patients_sexes:
			if sex == 'male':
				male += 1
			elif sex == 'female':
				female += 1
		print("There are {} males and {} females in the sample.".format(male, female))
	def regions(self):
		region_dict = dict()
		for region in self.patients_regions:
			if region in region_dict:
				region_dict[region] += 1
			else:
				region_dict[region] = 1
		print(region_dict)
	def average_costs(self):
		total_charges = 0
		count = 0
		for charge in self.patients_charges:
			total_charges += float(charge)
			count += 1
		print("The average insurance cost is {} dollars.".format(total_charges / count))
	def average_costs_male(self):
		total_male_charges = 0
		count = 0
		male_count = 0
		for charge in self.patients_charges:
			if self.patients_sexes[count] == 'male':
				total_male_charges += float(charge)
				male_count += 1
			count += 1
		print("The average cost for males is {} dollars.".format(total_male_charges / male_count))
	def average_costs_female(self):
		total_female_charges = 0
		count = 0
		female_count = 0
		for charge in self.patients_charges:
			if self.patients_sexes[count] == 'female':
				total_female_charges += float(charge)
				female_count += 1
			count += 1
		print("The average cost for females is {} dollars.".format(total_female_charges / female_count))	
	def create_dictionary(self):
		self.dic = dict()
		self.dic["Age"] = [int(age) for age in self.patients_ages]
		self.dic["Sex"] = self.patients_sexes
		self.dic["BMI"] = [float(bmi) for bmi in self.patients_bmis]
		self.dic["Children"] = [int(children) for children in self.patients_num_children]
		self.dic["Smoker"] = self.patients_smoker_statuses
		self.dic["Regions"] = self.patients_regions
		self.dic["Charges"] = [float(charges) for charges in self.patients_charges]

		return self.dic


# We create an instance of the class InfoMaker in order to run methods on it and see our analysis:


info = InfoMaker(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

# We find the average age of the sample:

info.average_age()

# We analyze the balance of males and females:

info.males_and_females()

# We find the regions of the patients:

#print("The regions of the patients are as follows:")
info.regions()

# We find the average costs of the patients:
info.average_costs()

# We find the average costs for males and for females:
info.average_costs_male()
info.average_costs_female()
