import os, sys, uuid
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Blueprint, render_template, send_file, render_template_string
from core.routefunc import podlist, ordered_menu_list, base_section_files, create_lab_ui_steps, unordered_menu_dictionary
from core.routefunc import ordered_section_list, get_page_position_data, create_footer_urls
from core.lab_data import get_lab_data
from core.print_doc import create_whole_doc
from lab.pod_data import get_pod_data
from core.imgman import txtimage

lab = Blueprint('lab',__name__, template_folder='templates', static_folder='static')

@lab.route('/pod<int:pod_id>/<section>/<chapter>', methods=['GET', 'POST'])
@lab.route('/pod<int:pod_id>', methods=['GET', 'POST'])
def route2section(pod_id, section="intro", chapter="landing"):
    anchor = ""
    section_info = unordered_menu_dictionary()
    page_number = section_info[section][chapter]['pos']
    return render_template(section_info[section][chapter]['file'],
                           pod=str(pod_id),
                           podlist=podlist(),
                           data=get_pod_data(pod_id),
                           lab_data=get_lab_data(),
                           footer_urls=create_footer_urls(),
                           html_for_step_status=create_lab_ui_steps(base_section_files(),section),
                           section=section,
                           chapter=chapter,
                           anchor=anchor,
                           title=section_info[section][chapter]['title'],
                           menu=ordered_menu_list(base_section_files()),
                           unordered_menu=unordered_menu_dictionary(),
                           ordered_section_list=ordered_section_list(base_section_files()),
                           page_position=get_page_position_data(page_number),
                           cache_kill=uuid.uuid4()
                           )

@lab.route('/imgman/pod/<int:pod_id>/id/<int:imgman_id>')
def img_man(imgman_id, pod_id):
    # This takes the parameters of the URL and passes it to the image processor that then reads the CSV file
    # and returns back the binary image that is passed to the browser IMG tag.
    return send_file(txtimage(imgman_id, pod_id), mimetype='image/PNG')

@lab.route('/pod<int:pod_id>/print')
def print_doc(pod_id):
    data=get_pod_data(pod_id)
    return render_template_string(create_whole_doc(pod_id),
                                  title=get_lab_data().cl_id,
                                  pod=str(pod_id),
                                  page_position=get_page_position_data(1),
                                  data=data)

                                  
@lab.route('/extract/pod<int:pod_id>/<section>/<chapter>')
def extract_commands(pod_id, section, chapter):
    data = get_pod_data(pod_id)
    return render_template_string(extract_parsed_commands(section, chapter), title='Extract Commands', data=data)
