import xml.etree.ElementTree as et
raw_str=""
out_path=""
xml_path=""

tree=et.parse(xml_path)
root=tree.getroot()
for item in root:
  for txt in item.itertext():
    raw_str+=txt
      
with open(out_path, 'wt', encoding='UTF-8') as txt_file:
  txt_file.write(raw_input)
  
