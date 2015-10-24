import csv
from get import FullContactAdaptiveClient

api = FullContactAdaptiveClient()

open_file = open('sample.txt', 'r')

emails = map(lambda s: s.strip(), open_file.readlines())

fieldnames = ['email', 'name', 'role', 'company', 
'location', 'gender', 'linkedin', 
'twitter', 'facebook']

def csv_dict_writer(path, fieldnames, data):
    """
    Writes a CSV file using DictWriter
    """
    with open(path, "wb") as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

data = []

def get_data(response, email):
	dict_of_data = {}
	dict_of_data['email'] = email
	if response.has_key('contactInfo'):
		if response['contactInfo'].has_key("fullName"):
			name = response["contactInfo"]["fullName"]
			dict_of_data['name'] = name.encode('utf-8')
		else:
			name = ""
			dict_of_data['name'] = name

	if response.has_key("organizations"):
		if response["organizations"][0].has_key("title"):
			role = response["organizations"][0]["title"]
			dict_of_data['role'] = role.encode('utf-8')
		else:
			role = ""
			dict_of_data['role'] = role

	if response.has_key("organizations"):
		if response["organizations"][0].has_key("name"):
			company = response["organizations"][0]["name"]
			dict_of_data['company'] = company.encode('utf-8')
		else:
			company = ""
			dict_of_data['company'] = company

	if response.has_key('demographics'):
		if response["demographics"].has_key("locationGeneral"):
			location = response["demographics"]["locationGeneral"]
			dict_of_data['location'] = location.encode('utf-8')
		else:
			location = ""
			dict_of_data['location'] = location
		if response["demographics"].has_key("gender"):
			gender = response["demographics"]["gender"]
			dict_of_data['gender'] = gender.encode('utf-8')
		else:
			gender = ""
			dict_of_data['gender'] = gender

	if response.has_key('socialProfiles'):
		social_profiles = response["socialProfiles"]
		for i in social_profiles:
			if i["typeName"] == 'LinkedIn':
				linkedin = i["url"]
				dict_of_data['linkedin'] = linkedin.encode('utf-8')
			else:
				pass

			if i["typeName"] == 'Twitter':
				twitter = i["url"]
				dict_of_data['twitter'] = twitter.encode('utf-8')
			else:
				pass

			if i["typeName"] == 'Facebook':
				facebook = i["url"]
				dict_of_data['facebook'] = facebook.encode('utf-8')
			else:
				pass			
	return dict_of_data


for email in emails:
	res = api.call_fullcontact(email)
	dict_of_data = get_data(res, email)
	data.append(dict_of_data)
	print email, "done"


path = "dict_output.csv"
csv_dict_writer(path, fieldnames, data)
