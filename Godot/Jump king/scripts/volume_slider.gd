extends HSlider

@export
var busName: String # zmienna która dodaje się do configa i można wpisać odpowiednią ścieżkę

var busIndex: int # index ścieżki

func _ready() -> void:
	busIndex = AudioServer.get_bus_index(busName) # sprawdza na jakim indexie jest ścieżka
	value_changed.connect(_on_value_changed) # podpina onChange listenera
	
	# wyciąganie zapisanych wartości głośności(flaga, bo wykonuje się dla każdego busa)
	if(FileAccess.file_exists(Global.AUDIO_FILE_PATH)):
		var file = FileAccess.open(Global.AUDIO_FILE_PATH, FileAccess.READ)
		if(!Global.audioValuesRetrieved):
			Global.audioValuesRetrieved = true
			Global.audioValues = file.get_var(true)
	
		value = db_to_linear(Global.audioValues[busIndex])
	else:
		value = db_to_linear(AudioServer.get_bus_volume_db(busIndex))

func _on_value_changed(db: float) -> void:
	var newDB = linear_to_db(db)
	if(newDB == -INF):
		newDB = -60 # bo linear_to_db daje -inf jak db == 0
	AudioServer.set_bus_volume_db(busIndex, newDB)

	var file = FileAccess.open(Global.AUDIO_FILE_PATH, FileAccess.WRITE)
	Global.audioValues[busIndex] = newDB
	file.store_var(Global.audioValues, true)
