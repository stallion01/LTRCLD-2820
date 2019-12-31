from .routefunc import base_section_files, ordered_menu_list, ordered_section_list
import os
from bs4 import BeautifulSoup


def create_whole_doc(pod_id):
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    all_html = ""

    section_list = ordered_section_list(base_section_files())
    all_page_list = ordered_menu_list(base_section_files())
    for section in section_list:
        for doc_list in all_page_list[section]:
            if doc_list['file'] != None:
                f = open(APP_ROOT + "/templates/" + str(doc_list["file"]))
                contents = f.read()
                contents = contents.replace('{% extends "base_cisco.html" %}', '')
                contents = contents.replace('{% block content %}', '')
                contents = contents.replace('{{  end_of_page(page_position,data) }}', '')
                contents = contents.replace('{% endblock %}', '')
                all_html += contents

    all_html = '{% extends "print.html" %}{% block content %}' + all_html + '{% endblock %}'
    soup = BeautifulSoup(all_html)
    return soup.prettify()

