from models import UrlData

def test_expander(short_url):
    if 'g' in short_url:
        return "http://www.google.com"
    else:
        return None

def sqlitedb_expander(short_url):
    try:
        return UrlData.get(UrlData.short == short_url).full
    except:
        return None