from src.view.MainView import MainView
from src.pattern.singleton import Singleton


class TicketMachine(metaclass=Singleton):
    """
    Ticket Machine class
    """

    def __init__(self):
        """
        The constructor of ticket machine class which initializes the field: gui
        """
        self.gui = MainView()

    def get_gui(self):
        """
        Get graphical interface object
        :return: graphical interface object
        """
        return self.gui
