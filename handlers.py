import gi,newsApi
gi.require_version("Gtk","4.0")
from gi.repository import Gtk
builder = Gtk.Builder()

def onBackButtonClick(backButton):
    print("atleast")

def onSearchEntry(searchEntry,results):
    usrTopic=str(searchEntry.get_text())
    newsApi.apiFetch(usrTopic)
    newscount=1
    print(newsApi.newsCollection['status'])

    # News titles populate
    for items in newsApi.newsCollection['articles']:
        newsBox = Gtk.ListBoxRow()
        wordCont = Gtk.TextView()
        textbuff = wordCont.get_buffer()
        textbuff.set_text(f"{newscount}: {items['title']}")
        newsBox.set_child(wordCont)
        results.append(newsBox)
        wordCont.set_css_classes(['titleContainers'])
        newscount = newscount+1