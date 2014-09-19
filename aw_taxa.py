# -*- coding: utf-8 -*-
import argparse
import re
import HTMLParser
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("taxon", help="subfamily or genus, not case sensitive")
parser.add_argument("-s", "--subspecies", help="include subspecies, default=False",
                    action="store_true")
parser.add_argument("-a", "--author-citations", help="include author citations, default=True",
                    action="store_false")
parser.add_argument("-d", "--debug", help="debug mode, default=False",
                    action="store_true")
parser.add_argument("-f", "--file", type=argparse.FileType('r'), help="input file, default=null")
args = parser.parse_args()
target_taxon = args.taxon
include_subspecies = args.subspecies
include_author_citations = args.author_citations
debug = args.debug
if args.file:
	filename = args.file.name
else:
	filename = False

url = "http://www.antweb.org/browse.do?rank=genus&genus=%s&project=worldants" % target_taxon

print "taxon =", target_taxon.capitalize()
print "include_author_citations =", include_author_citations
print "include_subspecies =", include_subspecies

if filename:
	print "filename =", filename
	with open(filename, 'r') as content_file:
		content = content_file.read()
else:
	print "url =", url
	print "\nDownloading page..."
	try:
	    request = requests.get(url)
	    request.raise_for_status()
	except HTTPError:
		#Does not work, AntWeb returns HTTP 200 OK for all requests to browse.do
	    print 'Could not download page'
	    exit(1)
	else:
	    print request.url, 'downloaded successfully'

	if "is not in the AntWeb database for project" in request.text:
	    print "The taxon \"%s\" is not in AntWeb's database. Quitting..." % target_taxon
	    exit(1)
	content = request.text

print "\nParsing HTML..."
soup = BeautifulSoup(content)
html_parser = HTMLParser.HTMLParser()

page_data = soup.find_all("div", {"class": "specimen_layout"}) # <div id="page_data">

output = ""
taxon_count = 0

for specimen_layout in page_data:
	links = specimen_layout.find_all('a', text=True) # all a elements in <div class="specimen_layout">
	taxon = links[0].decode_contents(formatter="html")
	subgenus_pattern = re.compile(r" \(.*?\) ")

	if subgenus_pattern.search(taxon) is not None:
		if debug:
			print "Subgenus:", taxon
		taxon = re.sub(subgenus_pattern, " ", taxon) # remove subgenera
	
	author_date = specimen_layout.find_all('div', text=True) # <div class="author_date">
	author_citation = author_date[0].decode_contents(formatter="html")

	if not include_subspecies and taxon.count(' ') > 1:
		if debug:
			print "Subspecies:", taxon
		continue

	output = output + "*''[[" + html_parser.unescape(taxon) + "]]''"
	if include_author_citations:
		output = output + " <small>" + html_parser.unescape(author_citation) + "</small>"
	output += "\n"
	taxon_count += 1

output = output.replace(u"*''[[†", u"*†''[[")

print "\n==Species==\n{{div col|2}}\n" + output + "{{div col end}}"

print "\n%s: %i taxa" % (target_taxon.capitalize(), taxon_count)

if "[no authors]" in output:
	print "Warning: output contains %i occurrence(s) of \"[no authors]\"" % output.count('[no authors]')
