#include <Python.h>

#include "modules/SquarePixels_eastereggs_credits_Easteregg.py.h"
#include "modules/SquarePixels_enemymanagement_enemy_manager.py.h"
#include "modules/SquarePixels_enemymanagement_enemy.py.h"
#include "modules/SquarePixels_game_game.py.h"
#include "modules/SquarePixels_multiplayer_client.py.h"
#include "modules/SquarePixels_multiplayer_clientr.py.h"
#include "modules/SquarePixels_multiplayer_server.py.h"
#include "modules/SquarePixels_player_player.py.h"
#include "modules/SquarePixels_render_render.py.h"
#include "modules/SquarePixels_render_Lighting.py.h"
#include "modules/SquarePixels_soundmanagement_music.py.h"
#include "modules/SquarePixels_soundmanagement_MusicManager.py.h"
#include "modules/SquarePixels_terraingen_terrain_gen.py.h"
#include "modules/SquarePixels_uimanagement_Character_creation.py.h"
#include "modules/SquarePixels_uimanagement_client_ui.py.h"
#include "modules/SquarePixels_uimanagement_death.py.h"
#include "modules/SquarePixels_uimanagement_inventory.py.h"
#include "modules/SquarePixels_uimanagement_logo.py.h"
#include "modules/SquarePixels_uimanagement_store.py.h"
#include "modules/SquarePixels_uimanagement_transition.py.h"
#include "modules/SquarePixels_uimanagement_EllipsesWarning.py.h"
#include "modules/SquarePixels_uimanagement_MainMen.py.h"
#include "modules/SquarePixels_uimanagement_server_ui.py.h"
#include "modules/SquarePixels_uimanagement_elements_button.py.h"
#include "modules/SquarePixels_uimanagement_elements_input_feild.py.h"
#include "modules/SquarePixels_uimanagement_elements_slider.py.h"
#include "modules/SquarePixels_uimanagement_elements_numeric_input.py.h"
#include "modules/SquarePixels_uimanagement_clouds.py.h"
#include "modules/SquarePixels_uimanagement_friends.py.h"
#include "modules/SquarePixels_uimanagement_elements_TextElement.py.h"
#include "modules/SquarePixels_uimanagement_easy_ui_maker.py.h"
#include "modules/SquarePixels_uimanagement_elements_Checkbox.py.h"
#include "modules/SquarePixels_uimanagement_elements_Image.py.h"
#include "modules/SquarePixels_uimanagement_elements_unfinished_Nodes.py.h"
#include "modules/SquarePixels_uimanagement_elements_unfinished_musicmaker.py.h"
#include "modules/SquarePixels_uimanagement_UIpanel.py.h"
#include "modules/SquarePixels_uimanagement_get_user_avatar.py.h"
#include "modules/SquarePixels_uimanagement_elements_color.py.h"

int main() {
	Py_Initialize();

	PyRun_SimpleString(SquarePixel.py);

	PyRun_SimpleString(credits_Easteregg_py);
	PyRun_SimpleString(enemy_manager_py);
	PyRun_SimpleString(enemy_py);
	PyRun_SimpleString(game_py);
	PyRun_SimpleString(client_py);
	PyRun_SimpleString(clientr_py);
	PyRun_SimpleString(server_py);
	PyRun_SimpleString(player_py);
	PyRun_SimpleString(render_py);
	PyRun_SimpleString(Lighting_py);
	PyRun_SimpleString(music_py);
	PyRun_SimpleString(MusicManager_py);
	PyRun_SimpleString(terrain_gen_py);
	PyRun_SimpleString(Character_creation_py);
	PyRun_SimpleString(client_ui_py);
	PyRun_SimpleString(death_py);
	PyRun_SimpleString(inventory_py);
	PyRun_SimpleString(logo_py);
	PyRun_SimpleString(store_py);
	PyRun_SimpleString(transition_py);
	PyRun_SimpleString(EllipsesWarning_py);
	PyRun_SimpleString(MainMen_py);
	PyRun_SimpleString(server_ui_py);
	PyRun_SimpleString(button_py);
	PyRun_SimpleString(input_feild_py);
	PyRun_SimpleString(slider_py);
	PyRun_SimpleString(numeric_input_py);
	PyRun_SimpleString(clouds_py);
	PyRun_SimpleString(friends_py);
	PyRun_SimpleString(TextElement_py);
	PyRun_SimpleString(easy_ui_maker_py);
	PyRun_SimpleString(Checkbox_py);
	PyRun_SimpleString(Image_py);
	PyRun_SimpleString(Nodes_py);
	PyRun_SimpleString(musicmaker_py);
	PyRun_SimpleString(UIpanel_py);
	PyRun_SimpleString(get_user_avatar_py);
	PyRun_SimpleString(color_py);

	Py_Finalize();

	return 0;
}
