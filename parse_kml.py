import os
import re

def add_placemarks(string):
	return "<Placemark>" + string + "</Placemark>"

def add_xml_tags(kml):
	return '<?xml version="1.0" encoding="utf-8" ?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n' + kml + '\n</kml>'


def main():

	kml_file = open("/home/thatchej/renooble/QGIS_data/zipcodes.kml").read()

	#separates all of the kml files for each zip code
	regex = re.compile('<Placemark>(.*?)</Placemark>', re.DOTALL).findall(kml_file) 

	#adds <Placemark> tags back onto each kml, and adds xml tags since we are separating
	#one big file into multiple  
	#TODO: Fix the regex so this is not needed
	kml_for_each_zip = [add_placemarks(x) for x in regex]
	kml_for_each_zip = [add_xml_tags(x) for x in kml_for_each_zip]

	for x in kml_for_each_zip:
		name = re.compile('<name>(.*?)</name>', re.DOTALL).findall(x) 
		temp_file = open("/home/thatchej/renooble/fixed_kmls/%s.kml" % name[0], "w")
		temp_file.write(x)

if __name__ == '__main__':
	main()

