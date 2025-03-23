import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QVBoxLayout, QWidget
from PyQt5.QtCore import QDate

class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Blacks Calendar")
        self.setGeometry(100, 100, 400, 300)

        # Main layout
        layout = QVBoxLayout()

        # Calendar widget
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setSelectedDate(QDate.currentDate())

        # Connect to a date change event
        self.calendar.selectionChanged.connect(self.print_selected_date)

        # Add calendar to layout
        layout.addWidget(self.calendar)

        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def print_selected_date(self):
        selected_date = self.calendar.selectedDate()
        print("Selected date:", selected_date.toString())

# Main entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CalendarApp()
    main_window.show()
    sys.exit(app.exec_())
