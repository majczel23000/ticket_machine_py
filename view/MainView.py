from PyQt5 import QtWidgets

from view.ConfirmationView import ConfirmationView
from view.TicketsView import TicketsView
from view.PaymentView import PaymentView


class MainView(QtWidgets.QMainWindow):
    """
    Main view class of QMainWindow type
    """

    def __init__(self):
        """
        The constructor of main view class which set up: current_view, tickets_view, confirmation_view, payment_view
        """
        super(MainView, self).__init__()
        self.current_view = "tickets_view"
        self.tickets_view = TicketsView()
        self.payment_view = PaymentView()
        self.confirmation_view = ConfirmationView()
        self.setCentralWidget(self.tickets_view)
        self.setWindowTitle("Biletomat razpin")
        self.setStyleSheet("QMainWindow {background: 'white';}")
        self.resize(950, 732)
        self.show()

    def change_view(self, view):
        """
        Change view based on parameter view
        :param view: view name to change
        """
        if view == "payment":
            if self.current_view == "tickets_view":
                self.tickets_view.deleteLater()
            self.setCentralWidget(self.payment_view)
            self.current_view == "payment_view"
        if view == "confirmation":
            if self.current_view == "payment":
                self.payment_view.deleteLater()
            self.setCentralWidget(self.confirmation_view)
            self.current_view == "confirmation_view"
