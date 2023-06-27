# Firewall Indicator

Firewall Indicator is a simple GTK application that displays a tray icon representing the status of the Ubuntu firewall (UFW). It provides a right-click menu with options to show an about dialog and quit the application.

## Features

- Displays a tray icon representing the status of the Ubuntu firewall (UFW)
- Right-click menu with options:
  - About: Displays an about dialog with information about the application
  - Quit: Quits the application

## Requirements

- Python 3
- GTK 3
- AppIndicator3
- UFW (Ubuntu Firewall)

## Installation

1. Clone the repository:

   ```shell
   git clone <repository-url>
   ```

2. Install the required dependencies:

   ```shell
   # Ubuntu/Debian
   sudo apt-get install python3-gi gir1.2-appindicator3-0.1 ufw
   
   # Fedora
   sudo dnf install python3-gobject gir1.2-appindicator3-0.1 ufw
   ```

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the following command to start the Firewall Indicator:

   ```shell
   sudo python3 firewall_indicator.py
   ```

   The application will start running and display a tray icon in the system tray.

3. Right-click on the tray icon to access the menu and select the desired options.

## License

This project is licensed under the [MIT License](LICENSE).
