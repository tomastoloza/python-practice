from xml.etree import ElementTree

tree = ElementTree.parse('archivo.xml')
# a = tree.getroot().findall('Pedido/')
a = tree.findall(".//Correlativas/")

for i in a:
    print(i)
