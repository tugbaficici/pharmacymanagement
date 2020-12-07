#!/usr/bin/env python3

from gi.repository import Gtk, GLib, Gio

class Test(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        store = Gtk.ListStore(str)
        self.tree = Gtk.TreeView(store)
        for i in range(0,10):
            store.append(["test " + str(i)])
        self.connect("delete-event", Gtk.main_quit)
        self.tree.connect("button_press_event", self.mouse_click)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Title", renderer, text=0)
        self.tree.append_column(column)
        self.add(self.tree)

    def mouse_click(self, tv, event):
        if event.button == 3:
            # Begin added code
            pthinfo = self.tree.get_path_at_pos(event.x, event.y)
            if pthinfo != None:
                path,col,cellx,celly = pthinfo
                self.tree.grab_focus()
                self.tree.set_cursor(path,col,0)
            # End added code

            selection = self.tree.get_selection()
            (model, iter) = selection.get_selected()
            print(model[iter][0])

win = Test()
win.show_all()
Gtk.main()