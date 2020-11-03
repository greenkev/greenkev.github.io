#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution


from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re

#todo: incorporate different collection types rather than a catch all publications, requires other changes to template

BOLDED_AUTHOR_FIRST_NAME = "kevin"
BOLDED_AUTHOR_LAST_NAME = "green"

HACK_SEPERATION_STRING = "}\n\n@"


publist = {
    "article": {
        "file" : "KevinGreenPapers.bib",
        "venuekey": "journal",
        "venue-pretext": "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
        
    },
    "inproceedings":{
        "file": "KevinGreenPapers.bib",
        "venuekey" : "booktitle",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    },
    "patent":{
        "file": "KevinGreenPapers.bib",
        "venuekey" : "number",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    },
    "inbook":{
        "file": "KevinGreenPapers.bib",
        "venuekey" : "number",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    },
    "misc":{
        "file": "KevinGreenPapers.bib",
        "venuekey" : "bookTitle",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    }
}

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


for pubsource in publist:
    # print(publist[pubsource])
    parser = bibtex.Parser()
    bibdata = parser.parse_file(publist[pubsource]["file"])

    # Seperate bibtex entried
    raw_bibtex = bibdata.to_string('bibtex')
    # print(raw_bibtex)
    seperated_raw_bibtex = []
    start_idx = 1
    while start_idx > 0:
        curr_idx = raw_bibtex.find(HACK_SEPERATION_STRING, start_idx)
        seperated_raw_bibtex.append(raw_bibtex[start_idx:curr_idx+1])
        start_idx = curr_idx + 1

    #loop through the individual references in a given bibtex file
    for bib_id in bibdata.entries:
        #reset default date

        pub_year = "1900"
        pub_month = "01"
        pub_day = "01"
        
        b = bibdata.entries[bib_id].fields
        
        try:
            if pubsource != "misc" and bibdata.entries[bib_id].type != pubsource:
                continue
            pub_year = f'{b["year"]}'

            #todo: this hack for month and day needs some cleanup
            if "month" in b.keys(): 
                if(len(b["month"])<3):
                    pub_month = "0"+b["month"]
                    pub_month = pub_month[-2:]
                elif(b["month"] not in range(12)):
                    tmnth = strptime(b["month"][:3],'%b').tm_mon   
                    pub_month = "{:02d}".format(tmnth) 
                else:
                    pub_month = str(b["month"])
            if "day" in b.keys(): 
                pub_day = str(b["day"])

                
            pub_date = pub_year+"-"+pub_month+"-"+pub_day
            
            #strip out {} as needed (some bibtex entries that maintain formatting)
            clean_title = b["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-")    

            url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
            url_slug = url_slug.replace("--","-")
            url_slug = url_slug[0:100] # Keep url from being too long

            md_filename = (str(pub_date) + "-" + url_slug + ".md").replace("--","-")
            md_filename = os.path.basename(md_filename)
            bib_filename = md_filename[0:-3]+".bib"

            html_filename = (str(pub_date) + "-" + url_slug).replace("--","-")

            #Build Citation from text
            citation = ""

            #citation authors - todo - add highlighting for primary author?
            for author in bibdata.entries[bib_id].persons["author"]:
                if len(author.middle_names) == 0:
                    name = "".join(author.first_names) + " " + "".join(author.last_names)
                else:
                    name = "".join(author.first_names) + " " + "".join(author.middle_names) + " " + "".join(author.last_names)
                        
                print(name)
                if author.first_names[0].lower() == BOLDED_AUTHOR_FIRST_NAME.lower() and \
                   author.last_names[0].lower() == BOLDED_AUTHOR_LAST_NAME.lower():
                    citation = citation+" <b>"+name+"</b>, "
                else:
                    citation = citation+" "+ name +", "

            #citation title
            citation = citation + "\"" + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + ".\""

            #add venue logic depending on citation type
            venue = publist[pubsource]["venue-pretext"]+b[publist[pubsource]["venuekey"]].replace("{", "").replace("}","").replace("\\","")

            citation = citation + " " + html_escape(venue)
            citation = citation + ", " + pub_year + "."

            
            ## YAML variables
            md = "---\ntitle: \""   + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + '"\n'
            
            md += """collection: """ +  publist[pubsource]["collection"]["name"]

            md += """\npermalink: """ + publist[pubsource]["collection"]["permalink"]  + html_filename
            
            note = False
            if "note" in b.keys():
                if len(str(b["note"])) > 5:
                    md += "\nexcerpt: '" + html_escape(b["note"]) + "'"
                    note = True

            md += "\ndate: " + str(pub_date)

            md += "\nvenue: '" + html_escape(venue) + "'"
            
            url = False
            if "url" in b.keys():
                if len(str(b["url"])) > 5:
                    md += "\npaperurl: '" + b["url"] + "'"
                    url = True

            md += "\ncitation: '" + html_escape(citation) + "'"

            # Add publication_type
            md += "\npublication_type: '" + html_escape(bibdata.entries[bib_id].type) + "'"

            # add presentation video url if it exists (no url )
            if 'preprint_url' in b.keys():
                if len(str(b["preprint_url"])) > 5:
                    md += "\npreprint: '" + b['preprint_url'] + "'"

            if 'presentation_video_url' in b.keys():
                if len(str(b["presentation_video_url"])) > 5:
                    md += "\npresentation_video_url: '" + b['presentation_video_url'] + "'"

            if 'attached_video_url' in b.keys():
                if len(str(b["attached_video_url"])) > 5:
                    md += "\nattached_video_url: '" + b['attached_video_url'] + "'"

            md += "\nbib_file_name: '" + bib_filename + "'"

            md += "\n---"


            
            ## Markdown description for individual page
            if note:
                md += "\n" + html_escape(b["note"]) + "\n"

            # if url:
            #     md += "\n[Access paper here](" + b["url"] + "){:target=\"_blank\"}\n" 
            # else:
            #     md += "\nUse [Google Scholar](https://scholar.google.com/scholar?q="+html.escape(clean_title.replace("-","+"))+"){:target=\"_blank\"} for full citation"

            with open("../_publications/" + md_filename, 'w') as f:
                f.write(md)
            with open("../files/individualBib/" + bib_filename, 'w') as f:
                f.write(seperated_raw_bibtex[list(bibdata.entries.keys()).index(bib_id)])
                
            print(f'SUCESSFULLY PARSED {bib_id}: \"', b["title"][:60],"..."*(len(b['title'])>60),"\"")
        # field may not exist for a reference
        except KeyError as e:
            print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', b["title"][:30],"..."*(len(b['title'])>30),"\"")
            continue
