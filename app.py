# Import graphics libraries
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi
# Import system modules
import sys
import os
# Import data management library
from pyntree import Node

# For hints only
from ui.main import Ui_MainWindow
from ui.summary import Ui_Summary

# Store static information for later use
REQUIRED_FIELDS = ("first_name", "last_name", "phone", "email", "plan", "coverage", "payment")
OPTIONAL_FIELDS = ("address", "city", "state", "zip")
TO_CALCULATE = ("subtotal", "tax", "total", "monthly")
PLAN_PRICES = {
    "gold": 36,
    "silver": 30,
    "bronze": 20
}
PRICE_PER_CAR = [1, 1.5, 1.75]
TAX_RATE = .07

data = Node()  # Create a new Node instance - a type of data manager
for field in REQUIRED_FIELDS + OPTIONAL_FIELDS:  # Pre-set every field to None on program start
    data.set(field, None)


class MainWindow(QMainWindow, Ui_MainWindow):  # Create the main window class from the base QMainWindow class
    def __init__(self, parent=None):
        super().__init__(parent)  # Run the QMainWindow class' configuration
        loadUi('ui/main.ui', self)  # Load the ui (made with QT Designer) into the window
        self.connect()

    def connect(self):  # Connect the buttons and other events to their proper functions
        # Connect buttons
        self.btnCalculate.clicked.connect(self.calculate)
        self.btnClear.clicked.connect(self.clear)
        self.btnExit.clicked.connect(app.exit)
        # Connect actions
        self.actCalculate.triggered.connect(self.calculate)
        self.actClear.triggered.connect(self.clear)
        self.actExit.triggered.connect(app.exit)
        # Connect miscellaneous events
        self.sbxCars.valueChanged.connect(self.update_discount)

    def get_data_from_screen(self):  # Grab the text from the screen
        data.first_name = self.txtFirstName.text()
        data.last_name = self.txtLastName.text()
        data.phone = self.txtPhone.text()
        data.email = self.txtEmail.text()
        data.plan = self.cbxPlan.currentText().split(" ")[0].lower()  # Get the first word and make it lowercase
        data.coverage = self.sbxCars.value()
        data.payment = self.cbxPaymentModel.currentText().split(" ")[0].lower()
        data.address = self.txtAddress.text()
        data.city = self.txtCity.text()
        data.state = self.txtState.text()
        data.zip = self.txtZip.text()

    def calculate(self):
        # Grab data from the screen
        self.get_data_from_screen()
        # Calculate remaining data
        paying_months = 12 if data.payment._val == "monthly" else 11
        # List indexes start at 0
        data.subtotal = PLAN_PRICES[data.plan._val] * PRICE_PER_CAR[data.coverage._val-1] * paying_months
        data.tax = round(data.subtotal._val * TAX_RATE, 2)
        data.total = data.subtotal._val + data.tax._val
        data.monthly = round(data.total._val / 12, 2)
        # Check that all required fields are filled
        for field in REQUIRED_FIELDS:
            if not data.get(field)._val:
                QMessageBox.critical(self, "Error", "Please complete all required fields")
                return

        # Show results if there are no errors
        summary_window.populate_data()
        summary_window.show()

    def clear(self):
        """
        Reset the main window - the summary window is generated based on it and will simply be re-populated
        """
        # First clear the optional fields, since they may not be overwritten
        summary_window.lblAddress.setText("")

        for field in REQUIRED_FIELDS + OPTIONAL_FIELDS:  # Reset all fields
            data.set(field, None)

        for attr in dir(self):  # Check all attributes
            obj = getattr(self, attr)  # Get attribute
            if attr.startswith('txt'):  # Check if attribute is prefixed as a text box
                obj.setText("")  # Reset all text boxes
            elif attr.startswith('cbx'):  # Check if attribute is prefixed as a dropdown menu
                obj.setCurrentIndex(0)  # Reset all dropdown menus
            elif attr.startswith('sbx'):  # Check if attribute is prefixed as a numerical input box
                obj.setValue(1)  # Reset all numerical input boxes

    def update_discount(self):  # Update the price information next the selector for the number of cars
        if self.sbxCars.value() == 1:
            # Remove price notification and fix plurality
            self.lblDiscount.setText("")
            self.lblPluralCars.setText("car")
        else:
            # Determine cost modifier and fix plurality
            # Lists start at index 0, so subtract 1
            self.lblDiscount.setText(f"{str(PRICE_PER_CAR[self.sbxCars.value()-1]*100)}% of plan price")
            self.lblPluralCars.setText("cars")


class Summary(QWidget, Ui_Summary):  # Create the main window class from the base QMainWindow class
    def __init__(self, parent=None):
        super().__init__(parent)  # Run the QWidget class' configuration
        loadUi('ui/summary.ui', self)  # Load the ui (made with QT Designer) into the window
        self.connect()

    def connect(self):  # Connect the buttons and other events to their proper functions
        self.btnDone.clicked.connect(self.close)

    def populate_data(self):  # Fill the fields on the window with the data provided
        self.lblName.setText(f"{data.first_name} {data.last_name}")
        self.lblPhone.setText(data.phone._val)
        self.lblEmail.setText(data.email._val)
        self.lblPlan.setText(data.plan._val)
        self.lblCars.setText(str(data.coverage._val))  # Convert int to string
        self.lblSubtotal.setText("$" + str(data.subtotal._val))  # Format as currency
        self.lblTax.setText("$" + str(data.tax._val))
        self.lblTotal.setText("$" + str(data.total._val))
        self.lblMonthlyPayment.setText("$" + str(data.monthly._val))
        # Don't fill the optional fields (Address) if any of them are empty
        any_left_empty = False
        for i in OPTIONAL_FIELDS:
            if not data.get(i)._val:  # If the data for the field is 0, None, False, etc. then treat it as nonexistent
                any_left_empty = True
        if any_left_empty:
            self.lblAddress.setText("The address was not provided or missing a city/state/zip.")
        else:
            self.lblAddress.setText(f"{data.address}, {data.city}, {data.state}, {data.zip}")


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Initialize the application object
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"  # Account for high-DPI displays
    win = MainWindow()  # Initialize the main window
    summary_window = Summary()  # Initialize the summary window
    win.show()  # Show the main window
    app.exec()  # Run the application
