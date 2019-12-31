import collections
import yaml
import os


def base_section_files():
    """
    Each member of the list is a section. Inside is a dictionary that contains the information for the chapters.
    These three separate sections are split in the template to separate columns to fit the many sections on the
    menu as needed.

    You have two places for the URL indicator. The first is index of the dictionary and the second is the weburl.
    These need to match. The dictionary is read from two separate places. One that just uses the dictionary
    reference. The second that converts the dictionary to a list based on the POS column to keep the dictionary
    in order as specified by the numeric value order.
    """
    empty_menu = [
        {
            "head":             {"line": "head", "step": 0, "pos": 1, "ls": True, "weburl": "head", "file": None, "title": "Introduction"},
            "landing":          {"line": "data", "step": 1, "pos": 2, "ls": True, "weburl": "landing", "file": "podlanding.html", "title": "Introduction"},
        }
    ]

    yaml_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir, 'lab/yaml/menu.yaml'))
    if os.path.exists(yaml_path):
        print("Menu YAML file exists. Processing")
        yaml_data = open(yaml_path, 'r')
        menu_dict = yaml.load(yaml_data, Loader=yaml.FullLoader)
    else:
        print("Menu !!NOT FOUND!!. Returning blank menu")
        menu_dict = empty_menu
    return menu_dict


def ordered_menu_list(data):
    """
    :param data:
    The purpose of this function is to take the menu dictionary and return a dictionary that is indexed by the
    section and then that section would contain a list based on the sorted value of the POS column. If not the
    MENU would end up with a different order as dictionaries in Python don't have order. This function is called
    when the menu data is passed to the template that then processes it. Since we can't have the lambda function
    inside of the template, we have to pass it ordered to the template.
    """
    ordered_submenu_list = {}

    for menu_section in data:
        for key in menu_section.keys():
            ordered_submenu_list[key] = []

    for menu_section in data:
        sorted_menus = sorted(
            [v for v in next(iter(menu_section.values())).values()], key=lambda x: x['pos'])
        topkey = menu_section.popitem()[0]
        ordered_submenu_list[topkey] = sorted_menus

    return ordered_submenu_list


def ordered_section_list(data):
    """
    :param data:
    This returns an ordered section list from the list dictionary of the menu.
    """
    ordered_section_list = []

    for menu_section in data:
        for key in menu_section.keys():
            ordered_section_list.append(key)
    return ordered_section_list


def unordered_menu_dictionary():
    data = base_section_files()
    unordered_dictionary = {}

    for menu_section in data:
        for topkey, value in menu_section.items():
            unordered_dictionary[topkey] = value

    return unordered_dictionary


def create_lab_ui_steps(data, current_section):
    """
    :param data:
    :param current_section:
    This function creates an HTML string around specific Cisco UI steps position to give the
    user a sense of where they are located in the lab.
    """
    html = "<div class='progress_step'>"
    #html += "<div class='step_title'>LAB PROGRESS</div>"
    html += "<div class='ui-steps step-list'>"
    count = 1
    list_of_sections = []

    for section in data:
        for key, dict in section.items():
            list_of_sections.append(key)

    current_list_position = list_of_sections.index(current_section)

    for section in data:
        for key, section_dict in section.items():
            if section_dict["head"]["ls"]:
                if key == current_section:
                    html += "<div class='ui-step active'>"
                else:
                    position_in_list = list_of_sections.index(key)
                    if position_in_list < current_list_position:
                        html += "<div class='ui-step visited'>"
                    else:
                        html += "<div class='ui-step'>"
                html += "<div class='step__icon'>" + str(count) + "</div>"
                html += "<div class='step__label'>" + \
                    section_dict["head"]["title"] + "</div>"
                html += "</div>"
                count += 1

    html += "</div></div>"
    return html


def create_footer_urls():
    """
    This function will read the YAML file called footer_links.yaml in the 
    lab section and create the HTML links at the bottom bar from that data.
    """
    yaml_path = os.path.abspath(os.path.join(os.path.dirname(
        __file__), os.pardir, 'lab/yaml/footer_links.yaml'))
    if os.path.exists(yaml_path):
        print("The footers yaml file exists, procesing")
        yaml_data = open(yaml_path, 'r')
        list_of_urls = yaml.load(yaml_data, Loader=yaml.FullLoader)
    else:
        list_of_urls = []
    return list_of_urls


def ordered_page_list(data):
    """
    this function takes the menu items and returns a list of them in sequential order based on the pos value. this
    is used to then create the "next" and "previous" steps at the bottom of the page so the user goes back and
    forth across the sections without the menu.
    """
    mylist = []
    newlist = {}
    # the menu is a list of dictionaries in order. loop to extract the section dicts.
    for menudict in data:
        for menukey, menudata in menudict.items():
            for menuitem_key, menuitem_entry in menudata.items():

                if menuitem_entry["line"] == "data":
                    newlist["exists"] = True
                    newlist["pos"] = menuitem_entry["pos"]
                    newlist["file"] = menuitem_entry["file"]
                    newlist["title"] = menuitem_entry["title"][:20]
                    newlist["weburl"] = menuitem_entry["weburl"]
                    newlist["section"] = menukey
                    mylist.append(newlist)
                    newlist = {}

    ordered_list = sorted(mylist, key=lambda k: k['pos'])
    return ordered_list


def get_page_position_data(page):
    """
    :param page:
    returns a list that contains the previous, current and next page position in the document
    from the reference document structure list based on the current page.
    """
    all_pages = ordered_page_list(base_section_files())
    pageindex = page_find_numericindex(all_pages, page)
    page_position_data = []

    prev_page = page_index_info(pageindex - 1, all_pages)
    current_page = page_index_info(pageindex, all_pages)
    next_page = page_index_info(pageindex + 1, all_pages)

    if prev_page["pos"] < current_page["pos"]:
        page_position_data.append(prev_page)
    else:
        page_position_data.append({"exists": False})

    page_position_data.append(current_page)

    if next_page is not False:
        if next_page["pos"] > current_page["pos"]:
            page_position_data.append(next_page)
        else:
            page_position_data.append({"exists": False})
    else:
        page_position_data.append({"exists": False})

    return page_position_data


def page_index_info(pageindex, all_pages):
    try:
        page_info = all_pages[pageindex]
    except Exception:
        return False
    return page_info


def page_find_numericindex(all_pages, page):
    for i, dic in enumerate(all_pages):
        if dic['pos'] == page:
            # print "this page is pos=" + str(dic['pos']) + " and index on the list of: " + str(i)
            return i
    return -1


def podlist():
    yaml_path = os.path.abspath(os.path.join(os.path.dirname(
        __file__), os.pardir, 'lab/yaml/pod_list.yaml'))
    yaml_data = open(yaml_path, 'r')
    return yaml.load(yaml_data, Loader=yaml.FullLoader)


def extract_parsed_commands(section, chapter):
    import os
    from bs4 import BeautifulSoup
    from .routefunc import base_section_files

    dict_menu = unordered_menu_dictionary()

    path_to_file = os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir, 'lab/templates/' + dict_menu[section][chapter]["file"]))

    f = open(path_to_file)
    contents = f.read()
    htmlstring = "<pre>"
    soup = BeautifulSoup(contents, features="html.parser")
    for tag in soup.find_all("code"):
        htmlstring += tag.get_text()
    htmlstring += "</pre>"
    return htmlstring
