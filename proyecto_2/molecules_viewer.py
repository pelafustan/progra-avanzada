import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from os import listdir, system
import subprocess
from biopandas.pdb import PandasPdb


class View():  # Ventana principal
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('./ui/main_win.ui')
        self.viewer = self.builder.get_object('Viewer')
        self.viewer.set_default_size(1024, 768)
        self.viewer.connect('destroy', Gtk.main_quit)
        self.viewer.show_all()

        self.image = self.builder.get_object('image')

        self.info = self.builder.get_object('info')

        self.mol_info = self.builder.get_object('mol_info')

        self.open_folder = self.builder.get_object('open_folder')
        self.open_folder.connect('file-set', self.get_folder)

        self.about = self.builder.get_object('about')
        self.about.connect('activate', self.about_on)

        self.content = self.builder.get_object('content')
        self.content.connect('cursor-changed', self.selected_file)

        self.files = []

        self.folder = ""

        self.gen_table()

    def about_on(self, btn=None):
        AboutDialog()

    def get_folder(self, btn=None):
        self.folder = self.open_folder.get_filename()
        self.info.set_text('Folder: ' + self.folder)
        files_in_dir = listdir(self.folder)
        files = []

        for name in files_in_dir:
            if "." not in name:
                continue

            format = name.split('.')[-1]
            if format == 'pdb':
                files.append(name)

        self.remove_all_data()

        for file in files:
            self.model.append([file])

    def remove_all_data(self):
        if len(self.model) != 0:
            for k in range(len(self.model)):
                iter = self.model.get_iter(0)
                self.model.remove(iter)

    def selected_file(self, btn=None):
        model, it = self.content.get_selection().get_selected()
        if model is None or it is None:
            return

        selected = model.get_value(it, 0)
        self.show_info(selected)
        self.show_image(selected)

    def show_image(self, selected):
        system('pymol ' + self.folder + '/' + selected
               + ' -x -g mol.png -c -Q')

        self.image.set_from_file('mol.png')

    def show_info(self, selected):
        ppdb = PandasPdb()
        ppdb.read_pdb(self.folder + '/' + selected)

        info = '\nRaw PDB file contents:\n\n%s\n...' % ppdb.pdb_text[:1000]

        self.mol_info.set_text(info)
        return

    def gen_table(self):
        self.content = self.builder.get_object('content')
        self.model = Gtk.ListStore(str)
        self.content.set_model(model=self.model)

        cell = Gtk.CellRendererText()
        col = Gtk.TreeViewColumn('Name', cell, text=0)
        self.content.append_column(col)


class AboutDialog():
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('./ui/main_win.ui')

        self.dialog = self.builder.get_object('about_dialog')
        self.dialog.show_all()


if __name__ == "__main__":
    window = View()
    Gtk.main()
