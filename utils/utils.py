from ast import Try
import json
import os
import settings as app_settings


class JsonLib:

    def __init__(self) -> None:
        # print(BASE_DIR)
        pass

    def read_json_file(self, filepath):
        with open(filepath, "r+", encoding="utf8") as f:
            data = json.load(f)
            return data

    def modify_data(self, data, new_tag):
        data.insert(0, new_tag)
        return data

    def add_tag_to_json_file(self, filepath, new_tag):
        try:
            data = self.read_json_file(filepath)
            data = self.modify_data(data, new_tag)
            self.write_json_file(filepath, data)

            return data
        except json.decoder.JSONDecodeError as e:
            return str(e)

    def write_json_file(self, filepath, data):
        with open(filepath, 'w') as outfile:
            json.dump(data, outfile)

    def create_new_folder(self, foldername):
        try:
            os.makedirs(os.path.join(app_settings.folder_path_for_root,foldername))
            return True
        except Exception as e:
            print(e)
            return False


    def create_json_file(self, foldername, filename):
        try:
            self.write_json_file(os.path.join(app_settings.folder_path_for_root, foldername, str(filename)+".json"),data=[])
            return True
        except Exception as e:
            print(e)
            return False

    


if __name__ == "__main__":
    data = [
        {
            "tag": "Tesla",
            "patterns": [
                "who are you?",
                "how are you?"
            ],
            "responses": ["good", " fine", "nice"]
        }
    ]
    script = JsonLib()
    data = script.read_json_file(
        os.path.join(app_settings.BASE_DIR, "output.json"))

    print(data)
