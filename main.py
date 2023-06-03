import sys,gi
import styling,handlers
gi.require_version("Gtk","4.0")
gi.require_version("Adw","1")
from gi.repository import Gtk,Adw
from styling import style_resource

global builder
builder =Gtk.Builder()
builder.add_from_file("newsgtk.ui")
style_resource()

class newsApp(Adw.Application):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.connect('activate',self.on_activate)

    def on_activate(self,app):
        # Objects Obtained
        window = builder.get_object("mainWin")
        self.results =builder.get_object("searchResult")
        searchEntry = builder.get_object("searchEntry")
        self.titleText = builder.get_object("searchTitle")
        self.headlines = builder.get_object("headlinesCont")
        # To set css references
        styling.widgetStyling(searchEntry,window)
        
        # Connectors
        searchEntry.connect('activate',self.onSearchEntry)

        # Window Actions
        window.set_application(self)
        window.present()
        
    def onSearchEntry(self,searchEntry):
            resbox = self.results
            title=self.titleText
            handlers.onSearchEntry(searchEntry,results=resbox,title=title)
        
app = newsApp(application_id="com.imnotndesh.mynews")
app.run(sys.argv)