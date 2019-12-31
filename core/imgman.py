from lab.pod_data import get_pod_data
from flask import render_template_string
from io import StringIO, BytesIO
from PIL import Image, ImageDraw, ImageFont
import os
import csv

def txtimage(img_id, pod_id):

    csvdata = readcsv(img_id,pod_id)
    print(csvdata)

    APP_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir))
    try:
        base = Image.open(APP_ROOT + '/lab/static/images/'+csvdata[0][3]).convert('RGBA')
    except:
        print("We had a problem openning the image:" + APP_ROOT + '/lab/static/images/'+csvdata[0][3])

    col = {"index": 0,
            "type": 1,
            "action": 2,
            "filename": 3,
            "x": 4,
            "y": 5,
            "textrotation": 6,
            "fontsize": 7,
            "textcolor": 8,
            "boxcolor": 9,
            "boxfill": 10,
            "font": 11,
            "align": 12,
            "text": 13}

    # Index,TYPE,ACTION(POINT/TXT),ImageFilename,X,Y,TextRotation,FontSize,TextColor,BoxColor,BoxFill,Font,Align,Text


    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(txt)

    for row in csvdata:
        if row[2] == "TXT":
            fnt = ImageFont.truetype(APP_ROOT + '/core/static/fonts'+row[col["font"]], int(row[col["fontsize"]]))
            draw.text((int(row[col["x"]]), int(row[col["y"]])), row[col["text"]], font=fnt, fill=row[col["textcolor"]])
        if row[2] == "CHECK":
            fnt = ImageFont.truetype(APP_ROOT + '/core/static/fonts'+row[col["font"]], int(row[col["fontsize"]]))
            draw.text((int(row[col["x"]]), int(row[col["y"]])), u"\u2714", font=fnt, fill=row[col["textcolor"]])
        if row[2] == "PLEFT":
            fnt = ImageFont.truetype(APP_ROOT + '/core/static/fonts'+row[col["font"]] , int(row[col["fontsize"]]))
            width, height = fnt.getsize(row[col["text"]])
            width += 2
            height += 2
            draw.line((int(row[col["x"]]), int(row[col["y"]])+12, int(row[col["x"]])+20, int(row[col["y"]])+12), fill=row[col["boxcolor"]], width=2)
            draw.line((int(row[col["x"]]), int(row[col["y"]])+12, int(row[col["x"]])+6,  int(row[col["y"]])+6),  fill=row[col["boxcolor"]], width=2)
            draw.line((int(row[col["x"]]), int(row[col["y"]])+12, int(row[col["x"]])+6,  int(row[col["y"]])+18), fill=row[col["boxcolor"]], width=2)
            draw.rectangle((int(row[col["x"]]) + 20 , int(row[col["y"]]), int(row[col["x"]]) + 26 + width, int(row[col["y"]]) + 8 + height), fill=row[col["boxfill"]], outline=row[col["boxcolor"]])
            draw.text((int(row[col["x"]])+25, int(row[col["y"]])+4), row[col["text"]], font=fnt, fill=row[col["textcolor"]])
        if row[2] == "PDOWN":
            fnt = ImageFont.truetype(APP_ROOT + '/core/static/fonts'+row[col["font"]], int(row[col["fontsize"]]))
            width, height = fnt.getsize(row[col["text"]])
            width += 2
            height += 2
            draw.line((int(row[col["x"]]), int(row[col["y"]]) + 8 + height,       int(row[col["x"]]),    int(row[col["y"]]) + 8 + height + 15),     fill=row[col["boxcolor"]], width=2)
            draw.line((int(row[col["x"]]), int(row[col["y"]]) + 8 + height + 15, int(row[col["x"]]) - 6, int(row[col["y"]]) + 8 + height + 15 - 6), fill=row[col["boxcolor"]], width=2)
            draw.line((int(row[col["x"]]), int(row[col["y"]]) + 8 + height + 15, int(row[col["x"]]) + 6, int(row[col["y"]]) + 8 + height + 15 - 6), fill=row[col["boxcolor"]], width=2)
            draw.rectangle((int(row[col["x"]]), int(row[col["y"]]), int(row[col["x"]]) + 6 + width, int(row[col["y"]]) + 8 + height), fill=row[col["boxfill"]], outline=row[col["boxcolor"]])
            draw.text((int(row[col["x"]])+4, int(row[col["y"]])+3), row[col["text"]], font=fnt, fill=row[col["textcolor"]])
        if row[2] == "LEFT":
            fnt = ImageFont.truetype(APP_ROOT + '/core/static/fonts'+row[col["font"]], int(row[col["fontsize"]]))
            width, height = fnt.getsize(row[col["text"]])
            width += 2
            height += 2
            draw.line((int(row[col["x"]]), int(row[col["y"]])+12, int(row[col["x"]])+20, int(row[col["y"]])+12), fill=row[col["boxcolor"]], width=2)
            draw.line((int(row[col["x"]]), int(row[col["y"]])+12, int(row[col["x"]])+6,  int(row[col["y"]])+6),  fill=row[col["boxcolor"]], width=2)
            draw.line((int(row[col["x"]]), int(row[col["y"]])+12, int(row[col["x"]])+6,  int(row[col["y"]])+18), fill=row[col["boxcolor"]], width=2)
            draw.text((int(row[col["x"]])+25, int(row[col["y"]])+4), row[col["text"]], font=fnt, fill=row[col["textcolor"]])
        #Attempt to make some rounded corner dialog boxes        
        if row[2] == "PLEFT2":
            fnt = ImageFont.truetype(APP_ROOT + '/core/static/fonts'+row[col["font"]], int(row[col["fontsize"]]))
            width, height = fnt.getsize(row[col["text"]])
            width += 2
            height += 2
            radius = 20
            fill = "red"
            corner = round_corner(radius, fill)
            txt.paste(corner, (0, 0))
            txt.paste(corner.rotate(90), (0, height - radius)) # Rotate the corner and paste it
            txt.paste(corner.rotate(180), (width - radius, height - radius))
            txt.paste(corner.rotate(270), (width - radius, 0))

            
    #img_io = StringIO()
    img_io = BytesIO()
    Image.alpha_composite(base, txt).save(img_io, 'PNG', quality=100)
    img_io.seek(0)

    return img_io

def round_corner(radius, fill):
    corner = Image.new('RGBA', (radius, radius), (0, 0, 0, 0))
    draw = ImageDraw.Draw(corner)
    draw.pieslice((0, 0, radius * 2, radius * 2), 180, 270, fill=fill)
    return corner

def readcsv(img_id,pod_id):

    # We read the CSV file via readcsvtemplate to be able to process the CSV file for the proper
    # data template points required. We use StringIO to take the string we get back and re-process
    # it back into csv.reader as a file.
    csvfiledata = readcsvtemplate(pod_id)
    fakecsvfile = StringIO(csvfiledata)
    data = []
    reader = csv.reader(fakecsvfile)
    for row in reader:
        if row[0] == str(img_id):
            data.append(row)
    return data


def readcsvtemplate(pod_id):
    APP_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir))
    try:
        with open ( APP_ROOT + "/lab/imgdata.csv", "r") as imagefiledata:
            csvfiledata=imagefiledata.read()
    except:
        print("We have a problem reading the CSV filedata:"+ APP_ROOT + "/lab/imgdata.csv")

    # data = get_pod_data(pod_id, 1)
    # Pass the variables from the session cookies into the template parser to replace the variables in
    # the CSV file with the values that we need and then return the data back.
    parsed_data = render_template_string(csvfiledata, data=get_pod_data(pod_id))
    return parsed_data

def csv2webtable(pod_id):
    # generate table contents
    import csv
    from io import StringIO

    rownum = 0

    csvfiledata = readcsvtemplate(pod_id)
    fakecsvfile = StringIO(csvfiledata)
    html = "<table width='100%' style='border:1px solid #696969;'>"

    reader = csv.reader(fakecsvfile)
    for row in reader:
        # Read a single row from the CSV file
        # The header row is only to be used for a header.
        if rownum == 0:
            html += '<tr>' # write <tr> tag
            for column in row:
                html += '<th>' + column + '</th>'
            html += '</tr>'
        # Write all following rows
        else:
            html += '<tr>'
            for column in row:
                html += '<td style=\'border:1px solid #696969;\'>' + column + '</td>'
            html += '</tr>'

        # increment row count
        rownum += 1

    # write </table> tag
    html += '</table>'

    return html

