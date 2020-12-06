from gi.repository import Gtk
from gi.repository import Pango
import sys

columns = ["First Name",
           "Last Name",
           "Phone Number"]

phonebook = [["Jurg", "Billeter", "555-0123"],
             ["Johannes", "Schmid", "555-1234"],
             ["Julita", "Inca", "555-2345"],
             ["Javier", "Jardon", "555-3456"],
             ["Jason", "Clinton", "555-4567"],
             ["Random J.", "Hacker", "555-5678"]]


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="My Phone Book", application=app)
        self.set_default_size(250, 100)
        self.set_border_width(10)

        listmodel = Gtk.ListStore(str, str, str)
        for i in range(len(phonebook)):
            listmodel.append(phonebook[i])


        view = Gtk.TreeView(model=listmodel)
        for i, column in enumerate(columns):
            cell = Gtk.CellRendererText()

            if i == 0:
                cell.props.weight_set = True
                cell.props.weight = Pango.Weight.BOLD

            col = Gtk.TreeViewColumn(column, cell, text=i)
            view.append_column(col)


        grid = Gtk.Grid()
        grid.attach(view, 0, 0, 1, 1)


        self.add(grid)


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)