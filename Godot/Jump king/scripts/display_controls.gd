extends GridContainer

@onready var modeButton = $ModeButton # przycisk zmiany typu obrazu(fullscreen, windowed)
@onready var resizeButton = $ResizeButton # przycisk zmiany rozmiaru okna


func _ready():
	# ustawienie podstawowych tekstów dla przycisków(musi być trzymane globalnie bo pokazuje się w 2 różnych isntancjach(menu, pause))
	resizeButton.text = Global.currentWindowSize
	modeButton.text = Global.currentWindowMode
	if(get_window().mode == Window.MODE_FULLSCREEN):
		resizeButton.disabled = true


func _on_mode_button_pressed():
	# ustawienie odpowiedniego trybu oraz napisu po wciśnięciu przycisku + zapisanie zmiany w Global
	if(get_window().mode == Window.MODE_WINDOWED):
		modeButton.text = 'Windowed'
		get_window().mode = Window.MODE_FULLSCREEN
		resizeButton.disabled = true
	elif(get_window().mode == Window.MODE_FULLSCREEN):
		modeButton.text = 'Fullscreen'
		get_window().mode = Window.MODE_WINDOWED
		resizeButton.disabled = false
	
	Global.currentWindowMode = modeButton.text


func _on_resize_button_pressed():
	# ustawienie odpowiedniego trybu oraz napisu po wciśnięciu przycisku + zapisanie zmiany w Global
	if(resizeButton.text == 'x1'):
		resizeButton.text = 'x2'
		get_window().size = Global.x1WindowSize
	elif(resizeButton.text == 'x2'):
		resizeButton.text = 'x3'
		get_window().size = Global.x2WindowSize
	elif(resizeButton.text == 'x3'):
		resizeButton.text = 'x1'
		get_window().size = Global.x3WindowSize
	
	Global.currentWindowSize = resizeButton.text
