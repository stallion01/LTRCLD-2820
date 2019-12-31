import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Blueprint, render_template
from core.routefunc import podlist, ordered_menu_list, base_section_files
from core.lab_data import get_lab_data
from lab.pod_data import get_pod_data

core = Blueprint('core',__name__, template_folder='templates', static_folder='static')
root = Blueprint('',__name__, template_folder='templates', static_folder='static')

@root.route('/')
def landing_page():
    return render_template('landing.html',
                           title=get_lab_data()['cl_id'],
                           pod=0,
                           data=get_lab_data(),
                           lab_data=get_lab_data(),
                           podlist=podlist(),
                           )
