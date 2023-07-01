import gi,newsApi
import threading
gi.require_version("Gtk","4.0")
from gi.repository import Gtk
builder = Gtk.Builder()

# def onAppLaunch(headlineCont):
#     print(newsApi.headCollection['articles']['title'])
#     # for items in newsApi.headlineCollection['articles']:
#     #     headBox = Gtk.ListBoxRow()
#     #     wordCont = Gtk.TextView()
#     #     textbuff = wordCont.get_buffer()
#     #     textbuff.set_text(f"{newscount}: {items['title']}")
#     #     headBox.set_child(wordCont)
#     #     headlineCont.append(headBox)
#     #     wordCont.set_css_classes(['titleContainers'])
#     #     newscount = newscount+1

def onSearchEntry(searchEntry,results,title):
    usrTopic=str(searchEntry.get_text())
    title.set_text(f"Showing results for : {usrTopic}")
    submitThread = threading.Thread(target=newsApi.searchFetch,daemon=True,args=(1,)).start()
    newsApi.searchFetch(usrTopic)
    newscount=1

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