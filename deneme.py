from gi.repository import Gtk

class Example:
    def __init__(self):
        window = Gtk.Window()
        window.connect('delete-event', Gtk.main_quit)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        notebook = Gtk.Notebook()
        button = Gtk.Button('Get text')
        button.connect('clicked', self.on_button_clicked)

        self.entry1 = Gtk.Entry()
        self.entry2 = Gtk.Entry()
        self.entry2.set_input_purpose(Gtk.InputPurpose.NUMBER)

        notebook.append_page(self.entry1)
        notebook.append_page(self.entry2)

        box.pack_end(button, True, True, 0)
        box.pack_start(notebook, True, True, 0)
        window.add(box)
        window.show_all()

    def on_button_clicked(self, widget):
        self.try_conversion(self.entry1.get_text())
        self.try_conversion(self.entry2.get_text())

    def try_conversion(self, text):
        try:
            print('Float: {}'.format(float(text)))
        except ValueError:
            print('String: ' + text)


if __name__ == '__main__':
    Example()
    Gtk.main()