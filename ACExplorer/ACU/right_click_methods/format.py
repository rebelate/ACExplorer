import os

plugin_name = 'Format'
plugin_level = 4
file_type = '*'


def plugin(app, file_id, forge_file_name, datafile_id):
	data = app.tempNewFiles(file_id, forge_file_name, datafile_id)
	if data is None:
		app.log.warn(__name__, f"Failed to find file {file_id:016X}")
		return
	out_file = open(
		os.path.join(
			app.CONFIG['dumpFolder'],
			f'{app.game_functions.game_identifier}_{data["fileName"]}_{file_id:016X}.format'
		), 'w'
	)
	app.read_file(data['rawFile'], out_file)
