import os
from bs4 import BeautifulSoup
import pandas as pd
import glob



if not os.path.exists("heritage_parsed_files"):
	os.mkdir("heritage_parsed_files")


df = pd.DataFrame()

for file_name in glob.glob('heritage_html_files/*.html'):
	print("Parsing " + file_name)

	f = open(file_name, "r", encoding="utf8")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	case_table = soup.find("div",{"class":"table-wrapper"}).find("div", {"class":"view-content"})
	case_rows = case_table.find_all("div",{"class":"views-row"})


	for r in case_rows:
		case_state_span = r.find("span",{"class":"views-field-field-fraud-state-administrative-area"}).find("span",{"class":"field-content"})
		if case_state_span is not None:
			case_state = case_state_span.text
		else:
			case_state = None

		case_year_span = r.find("span",{"class":"views-field-field-year-of-disposition"}).find("span",{"class":"field-content"})
		if case_year_span is not None:
			case_year = case_year_span.text
		else:
			case_year = None

		case_name_span = r.find("span",{"class":"views-field-name"}).find("span",{"class":"field-content"})
		if case_name_span is not None:
			case_name = case_name_span.text
		else:
			case_name = None

		case_type_span = r.find("span",{"class":"views-field-field-case-type"}).find("span",{"class":"field-content"})
		if case_type_span is not None:
				case_type = case_type_span.text
		else:
				case_type = None

		case_fraud_span = r.find("span",{"class":"views-field-field-fraud-type"}).find("span",{"class":"field-content"})
		if case_fraud_span is not None:
				case_fraud = case_fraud_span.text
		else:
				case_fraud = None

		df = df.append({
				'State': case_state,
				'Year': case_year,
				'Name': case_name,
				'Type': case_type,
				'Fraud': case_fraud,
			}, ignore_index=True)


	df.to_csv("heritage_parsed_files/heritage_dataset.csv")


print("Parsing complete")
print(" ")
print(" ")
print(" ")
print(df)
