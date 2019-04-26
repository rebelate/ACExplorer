from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import logging


class Reader(BaseReader):
	file_type = '1C4B22AA'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(6)
		b = file_object_data_wrapper.read_uint_8()
		if b == 3:
			file_object_data_wrapper.read_bytes(5)
			file_object_data_wrapper.read_id()
		elif b == 5:
			file_object_data_wrapper.read_id()
			file_object_data_wrapper.read_bytes(5)
			file_object_data_wrapper.read_id()
		else:
			logging.warning('value is not 3 or 5 I don\'t know how to deal with this')
