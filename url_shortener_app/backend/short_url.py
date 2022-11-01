import string
from url_shortener_app.models import Utility

class ShortURL:
    URL_LENGTH = 6
    current_url_no = Utility.objects.all()[0].current_url_no
    # This will create a URl of 6 characters that can be [A-Z, a-z, 0-9]. This will create total of 56 billion unique urls
    chars = [c for c in string.ascii_letters] + [str(i) for i in range(10)]

    @classmethod
    def get_short_url(cls):
        temp_current_url_no = ShortURL.current_url_no
        char_string = [0 for _ in range(ShortURL.URL_LENGTH)]
        short_url = ""
        for i in range(len(char_string)):
            possible = len(ShortURL.chars)**(len(char_string)-i-1)
            short_url += ShortURL.chars[temp_current_url_no//possible]
            temp_current_url_no = temp_current_url_no % possible
        ShortURL.current_url_no += 1
        Utility.objects.update(current_url_no=ShortURL.current_url_no)
        return short_url
