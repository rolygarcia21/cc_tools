import cc_dat_utils
import cc_classes
import json

def make_cc_level_pack_from_json( json_data ):
	#Initialize a new CCLevelPack
    level_pack = cc_classes.CCLevelPack()

    #Loop through the json_data
    for level in json_data:
        #Initialize a new CCLevel
        cclevel = cc_classes.CCLevel()

        #  Level number
        cclevel.level_number = level["level_number"]
        print("level number: " + str(cclevel.level_number))
        #  Time
        cclevel.time = level["time_limit"]
        print("time limit: " + str(cclevel.time))
        #  Number of chips
        cclevel.num_chips = level["num_chips"]
        print("# of chips: " + str(cclevel.num_chips))
        #  Upper layer
        cclevel.upper_layer = level["upper_layer"]
        print("upper layer: " + str(cclevel.upper_layer))

        for field in level["optional_fields"]:
            print(field)

            if field["field_type"] == "title":
                title = cc_classes.CCMapTitleField(field["map_title"])
                cclevel.add_field(title)

            elif field["field_type"] == "hint":
                hint = cc_classes.CCMapHintField(field["hint_text"])
                cclevel.add_field(hint)

            elif field["field_type"] == "password":
                password = cc_classes.CCEncodedPasswordField(field["password_array"])
                cclevel.add_field(password)

            elif field["field_type"] == "monsters":
                monster_coords_list = []

                for ord_pair in field["monster_coords"]:
                    coords = cc_classes.CCCoordinate(ord_pair["x"],ord_pair["y"])
                    monster_coords_list.append(coords)

                monster_list = cc_classes.CCMonsterMovementField(monster_coords_list)

                cclevel.add_field(monster_list)

        level_pack.add_level(cclevel)

    return level_pack

#Part 3
#Load your custom JSON file
input_json_file = "data/rolandog_cc1.json"
file = open(input_json_file, "r")
json_file = json.load(file)

#Convert JSON data to CCLevelPack
level_pack = make_cc_level_pack_from_json(json_file)
print(level_pack)

#Save converted data to DAT file
cc_dat_utils.write_cc_level_pack_to_dat(level_pack, "data/rolandog_cc1.dat")