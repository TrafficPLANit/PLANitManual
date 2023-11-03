from planit import *

# create a network converter
planit_instance = Planit()
network_converter = planit_instance.converter_factory.create(ConverterType.NETWORK)

################### OSM READER ###########
osm_reader = network_converter.create_reader(NetworkReaderType.OSM, "Australia")
osm_reader.settings.set_input_file(r"c:\Users\Public\sydneycbd_2023.osm.pbf")

################### SHAPE WRITER ########
geo_writer = network_converter.create_writer(NetworkWriterType.SHAPE)
geo_writer.settings.set_output_directory(r"c:\Users\Public\")
geo_writer.settings.set_country("Australia")
# Explicitly set what to persist from the network (these flags are the default, but are included for illustration purposes)
geo_writer.settings.set_persist_nodes(True)
geo_writer.settings.set_persist_links(True)

# perform conversion
network_converter.convert(osm_reader, geo_writer)
