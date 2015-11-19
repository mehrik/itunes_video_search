from system.core.controller import *

class Main(Controller):
    def __init__(self, action):
        super(Main, self).__init__(action)

    def index(self):
        return self.load_view('index.html')

    def get_video(self):
        artist = request.form['user_input']
        url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"
        response = requests.get(url).content
        return response
