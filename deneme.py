import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf

icons = ["edit-cut", "edit-paste", "edit-copy"]


class IconViewWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)

      
        iconview = Gtk.IconView.new()
        
        pixbuf = Gtk.IconTheme.get_default().load_icon("edit-cut", 64, 0)
        iconview.set_model([pixbuf, "QR"])
        iconview.set_pixbuf_column(0)
        iconview.set_text_column(1)

        

        self.add(iconview)


win = IconViewWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()