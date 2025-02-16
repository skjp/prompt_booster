#Requires AutoHotkey v2.0

#include "..\..\shared\BaseGui.ahk"



SpoutAddon_Prompt_Booster_nui(*) {
    booster := SpoutFunctionNoGUI("prompt_booster")
    booster.Run()
}

SpoutAddon_Prompt_Booster_gui(auto := false, text := "") {
    booster_gui := SpoutFunction(auto)
    booster_gui.originalContent := (text != "") ? text : A_Clipboard
    booster_gui.InitializeGUI("prompt_booster", "Boosted")
}


