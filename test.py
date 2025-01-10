### to retrieve the last uploaded file name from the user
## main.py에서 진행되야됨 
## which midiutil.MidiFile3 해보고 없으면 brew install 하기 

def get_last_uploaded_file():
    try:
        with open('resources/samples/last_uploaded_file.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

uploaded_file_name = get_last_uploaded_file()
if uploaded_file_name:
    img_file = uploaded_file_name
else:
    img_file = "resources/samples/hbd.jpg"


print(img_file)