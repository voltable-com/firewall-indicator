import subprocess
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

try:
    gi.require_version('AppIndicator3', '0.1')
    from gi.repository import AppIndicator3 as AppIndicator
except ValueError:
    gi.require_version('AyatanaAppIndicator3', '0.1')
    from gi.repository import AyatanaAppIndicator3 as AppIndicator

APPINDICATOR_ID = 'firewall-indicator'
PROGRAM_NAME = 'Firewall Indicator'
PROGRAM_VERSION = '1.0'
PROGRAM_DESCRIPTION = 'A simple indicator for the UFW firewall'
PROGRAM_AUTHORS = ['@VoltableCom']
PROGRAM_WEBSITE = 'https://www.voltable.com'
PROGRAM_WEBSITE_LABEL = 'www.voltable.com'


def show_about_dialog(widget):
    """
    Show the About dialog when the About menu item is activated.
    """
    about_dialog = Gtk.AboutDialog()
    about_dialog.set_icon_name('security-high')
    about_dialog.set_program_name(PROGRAM_NAME)
    about_dialog.set_version(PROGRAM_VERSION)
    about_dialog.set_authors(PROGRAM_AUTHORS)
    about_dialog.set_website(PROGRAM_WEBSITE)
    about_dialog.set_website_label(PROGRAM_WEBSITE_LABEL)
    about_dialog.run()
    about_dialog.destroy()


def quit_app(widget):
    """
    Quit the application when the Quit menu item is activated.
    """
    Gtk.main_quit()


def build_menu():
    """
    Build the right-click menu for the indicator.
    """
    menu = Gtk.Menu()

    # About menu item
    about_item = Gtk.MenuItem(label='About')
    about_item.connect('activate', show_about_dialog)
    menu.append(about_item)

    # Separator
    separator = Gtk.SeparatorMenuItem()
    menu.append(separator)

    # Quit menu item
    quit_item = Gtk.MenuItem(label='Quit')
    quit_item.connect('activate', quit_app)
    menu.append(quit_item)

    menu.show_all()
    return menu


def tray_icon_activate(icon, event):
    """
    Show the menu when the tray icon is activated.
    """
    menu = build_menu()
    menu.popup(None, None, None, None, event.button, event.time)


def get_ufw_status():
    """
    Get the status of the Ubuntu firewall (UFW).
    Returns:
        str: The status of the firewall.
    """    
    try:
        output = subprocess.check_output(['ufw', 'status'])
        output = output.decode('utf-8').strip()
        if 'Status: active' in output:
            return 'security-high'
        elif 'Status: inactive' in output:
            return 'security-low'
        else:
            return 'dialog-warning'
    except subprocess.CalledProcessError:
        return 'dialog-error'


def check_status(indicator):
    """
    Update the status and icon of the indicator based on the firewall status.
    Args:
        indicator (AppIndicator3.Indicator): The indicator object.
    Returns:
        bool: True to keep the status update running.
    """    
    status = get_ufw_status()
    indicator.set_icon_full(status, 'Firewall Status')
    return True


"""
The main entry point of the application.
"""
status = get_ufw_status()
indicator = AppIndicator.Indicator.new(
    APPINDICATOR_ID,
    status,
    AppIndicator.IndicatorCategory.SYSTEM_SERVICES
)
indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
indicator.set_menu(build_menu())
indicator.connect('notify', tray_icon_activate)

GLib.timeout_add_seconds(1, check_status, indicator)
Gtk.main()
