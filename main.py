import sys
import gi
import requests
import json
import styling
gi.require_version("Gtk","4.0")
gi.require_version("Adw","1")
from gi.repository import Gtk,Adw
from styling import style_resource

global builder
builder =Gtk.Builder()
builder.add_from_file("newsgtk.ui")
style_resource()
# Obtained API key goes here
appKey = 'ab1a600bcfe741fdadad464a7698e0bf'

class newsApp(Adw.Application):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.connect('activate',self.on_activate)

    def on_activate(self,app):
        # Objects Obtained
        self.window = builder.get_object("mainWin")
        self.mainstack = builder.get_object("mainStack")
        self.results= builder.get_object("searchResult")
        backButton = builder.get_object("backButton")
        searchEntry = builder.get_object("searchEntry")

        # To set css references
        searchEntry.set_css_classes(['searchBar'])


        # Connectors
        backButton.connect('activate',self.onBackButtonClick)
        searchEntry.connect('activate',self.onSearchEntryActive)

        # Window Actions
        self.window.set_application(self)
        self.window.present()

    def onBackButtonClick(self,backButton):
        pages = self.mainstack.get_children()
        currPage = self.mainstack.get_visible_child()
        i = pages.index(currPage)
        if i ==0:return
        self.mainstack.set_visible_child(pages[i-1])

    def onSearchEntryActive(self,searchEntry):
        usrSearch=str(searchEntry.get_text())
        ############################temporarily##################################
        response = requests.get(f'https://newsapi.org/v2/everything?q={usrSearch}&apiKey={appKey}').text
        coll_info = json.loads(response)
        newscount=1
        for items in coll_info['articles']:
            self.newsBox = Gtk.ListBoxRow()
            wordCont = Gtk.TextView()
            textbuff = wordCont.get_buffer()
            textbuff.set_text(f"{newscount}: {items['title']}")
            self.newsBox.set_child(wordCont)
            self.results.append(self.newsBox)
            wordCont.set_css_classes(['titleContainers'])
            newscount=newscount+1
            self.newsBox.connect('activate',self.onTitleClick)
    def onTitleClick(self):
        position=self.newsBox.get_index()
        print(position)


        #########################################################################

        
app = newsApp(application_id="com.imnotndesh.mynews")
app.run(sys.argv)