import gi
gi.require_version("Gtk","4.0")
gi.require_version("Gdk","4.0")
from gi.repository import Gtk,Gdk
builder = Gtk.Builder()

def style_resource():
    css_provider = Gtk.CssProvider()
    css_provider.load_from_path('main.css')
    Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    builder.add_from_file("newsgtk.ui")

def widgetStyling(searchEntry,window):
    searchEntry.set_css_classes(['searchBar'])
    window.set_css_classes(['mainWindow'])