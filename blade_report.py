from ucsmsdk.ucshandle import UcsHandle
import xlsxwriter

'''
+ Connect to UCSM
+ Extract physical blade information (model)
+ Write extracted information to blade.xlsx file
+ There are some images, if you don download images, please delete insert image command in this file
Prerequisite:
+ Install xlsxwriter package for additional info how to http://xlsxwriter.readthedocs.io
+ Install UCSM Python SDK


'''
ucsm_ip = "172.16.185.144"
admin = "ucspe"
password = "ucspe"
handle = UcsHandle(ucsm_ip,admin,password)
handle.login()

print "You are login ton UCSM at 172.16.185.144"
print "Information about Blades:"
print "Please check file name blade.xlsx for further information"
blades = handle.query_classid("computeBlade")

print type(blades)
print 'Blade 1 UUID:'
print blades[0].original_uuid

for blade in blades:
	print blade.model,blade.serial,blade.dn

'''
# Print result to CSV format file
csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)

with open('ucs_stat.csv', 'w') as mycsvfile:
    thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
    for blade in blades:
        thedatawriter.writerow(blade.model
'''
# Create Excel file

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('blade.xlsx')
worksheet = workbook.add_worksheet()


ds_b200m3 = "http://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-b200-m3-blade-server/data_sheet_c78-700625.html"
ds_b200m4 = "http://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-b200-m4-blade-server/datasheet-c78-732434.html"
ds_b420m3 = "http://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-b-series-blade-servers/data_sheet_c78-706603.html"

tup = {len(ds_b200m3),len(ds_b200m4),len(ds_b420m3)}
lcol = max(tup)
print lcol

# Widen the first column to make the text clearer.

worksheet.set_column('A:A', 25)
worksheet.set_column('B:B', lcol)
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Format background color of green for the cell:
format = workbook.add_format()
format.set_pattern(1)  # This is optional when using a solid fill.
format.set_bg_color('green')
format.set_bold()
format.set_font_color('white')
format.set_border()
format.set_font_size(13)

# Format background color of blue for the cell:
formatblue = workbook.add_format()
formatblue.set_pattern(1)  # This is optional when using a solid fill.
formatblue.set_bg_color('blue')
formatblue.set_bold()
formatblue.set_font_color('white')
formatblue.set_border()
formatblue.set_font_color(13)

# Write some simple text for row 1.
worksheet.write('A1', 'BLADE MODEL:',format)
worksheet.write('B1', 'DATASHEET:',formatblue)
# Text with formatting.

for i in range(len(blades)):
    print i
    worksheet.write(i+1,0,blades[i].model)
    if "B200-M3" in blades[i].model:
        worksheet.write(i+1,1,ds_b200m3)
    elif "B200-M4" in blades[i].model:
        worksheet.write(i+1,1,ds_b200m4)
    elif "B420-M3" in blades[i].model:
        worksheet.write(i+1,1,ds_b420m3)

# Insert an image.
worksheet.insert_image('A10', 'ucsm_logo.png')

# Write some numbers, with row/column notation.
#worksheet.write(2, 0, 123)
#worksheet.write(3, 0, 123.456)

workbook.close()

