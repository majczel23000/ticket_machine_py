import sys
from factory.MoneyFactory import MoneyFactory
from model.Order import *
from model.TicketMachine import *
from factory.TicketFactory import TicketFactory
from pattern.singleton import Singleton
from view.MainView import *


class Controller(metaclass=Singleton):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.ticket_machine = TicketMachine()
        self.view_helper = ViewHelper()
        self.order = Order()
        self.ticketFactory = TicketFactory()
        self.moneyFactory = MoneyFactory()
        self.assing_ticket_actions()
        sys.exit(app.exec_())

    # przypisanie clicków do poszczególnych buttonów
    def assing_ticket_actions(self):
        # Normalne I Strefa
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_20_plus').clicked.connect(lambda: self.add_ticket(1, 2.00, 'normal', 'btn_normal_20_count', 'n20'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_40_plus').clicked.connect(lambda: self.add_ticket(1, 3.60, 'normal', 'btn_normal_40_count', 'n40'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_oneway_plus').clicked.connect(lambda: self.add_ticket(1, 4.00, 'normal', 'btn_normal_oneway_count',
                                                                                                                                                   'none'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_twoway_plus').clicked.connect(lambda: self.add_ticket(1, 7.00, 'normal', 'btn_normal_twoway_count',
                                                                                                                                                   'ntwo'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_20_minus').clicked.connect(lambda: self.remove_ticket('n20', 'btn_normal_20_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_40_minus').clicked.connect(lambda: self.remove_ticket('n40', 'btn_normal_40_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_oneway_minus').clicked.connect(lambda: self.remove_ticket('none', 'btn_normal_oneway_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_twoway_minus').clicked.connect(lambda: self.remove_ticket('ntwo', 'btn_normal_twoway_count'))
        #Normalne II Strefa
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_20_2_plus').clicked.connect(lambda: self.add_ticket(2, 2.50, 'normal', 'btn_normal_20_2_count', 'n20_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_40_2_plus').clicked.connect(lambda: self.add_ticket(2, 4.00, 'normal', 'btn_normal_40_2_count', 'n40_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_oneway_2_plus').clicked.connect(lambda: self.add_ticket(2, 4.80, 'normal', 'btn_normal_oneway_2_count',
                                                                                                                                                  'none_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_twoway_2_plus').clicked.connect(lambda: self.add_ticket(2, 7.50, 'normal', 'btn_normal_twoway_2_count',
                                                                                                                                                  'ntwo_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_20_2_minus').clicked.connect(lambda: self.remove_ticket('n20_2', 'btn_normal_20_2_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_40_2_minus').clicked.connect(lambda: self.remove_ticket('n40_2', 'btn_normal_40_2_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_oneway_2_minus').clicked.connect(lambda: self.remove_ticket('none_2', 'btn_normal_oneway_2_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_normal_twoway_2_minus').clicked.connect(lambda: self.remove_ticket('ntwo_2', 'btn_normal_twoway_2_count'))
        # Ulgowe I Strefa
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_20_plus').clicked.connect(lambda: self.add_ticket(1, 1.00, 'reduced', 'btn_reduced_20_count', 'r20'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_40_plus').clicked.connect(lambda: self.add_ticket(1, 1.80, 'reduced', 'btn_reduced_40_count', 'r40'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_oneway_plus').clicked.connect(lambda: self.add_ticket(1, 2.00, 'reduced', 'btn_reduced_oneway_count',
                                                                                                                                                 'rone'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_twoway_plus').clicked.connect(lambda: self.add_ticket(1, 3.50, 'reduced', 'btn_reduced_twoway_count',
                                                                                                                                                 'rtwo'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_20_minus').clicked.connect(lambda: self.remove_ticket('r20', 'btn_reduced_20_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_40_minus').clicked.connect(lambda: self.remove_ticket('r40', 'btn_reduced_40_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_oneway_minus').clicked.connect(lambda: self.remove_ticket('rone', 'btn_reduced_oneway_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_twoway_minus').clicked.connect(lambda: self.remove_ticket('rtwo', 'btn_reduced_twoway_count'))
        # Ulgowe II Strefa
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_20_2_plus').clicked.connect(lambda: self.add_ticket(2, 1.20, 'reduced', 'btn_reduced_20_2_count',
                                                                                                                                                    'r20_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_40_2_plus').clicked.connect(lambda: self.add_ticket(2, 2.00, 'reduced', 'btn_reduced_40_2_count',
                                                                                                                                                    'r40_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_oneway_2_plus').clicked.connect(lambda: self.add_ticket(2, 2.50, 'reduced',
                                                                                                                                                       'btn_reduced_oneway_2_count', 'rone_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_twoway_2_plus').clicked.connect(lambda: self.add_ticket(2, 4.00, 'reduced',
                                                                                                                                                       'btn_reduced_twoway_2_count', 'rtwo_2'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_20_2_minus').clicked.connect(lambda: self.remove_ticket('r20_2', 'btn_reduced_20_2_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_40_2_minus').clicked.connect(lambda: self.remove_ticket('r40_2', 'btn_reduced_40_2_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_oneway_2_minus').clicked.connect(lambda: self.remove_ticket('rone_2', 'btn_reduced_oneway_2_count'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'btn_reduced_twoway_2_minus').clicked.connect(lambda: self.remove_ticket('rtwo_2', 'btn_reduced_twoway_2_count'))

        # przejście do płatności
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'payment').clicked.connect(lambda: self.change_view("payment"))

    def assign_payment_actions(self):
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_1_gr').clicked.connect(lambda: self.add_money("0.01", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_2_gr').clicked.connect(lambda: self.add_money("0.02", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_5_gr').clicked.connect(lambda: self.add_money("0.05", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_10_gr').clicked.connect(lambda: self.add_money("0.10", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_20_gr').clicked.connect(lambda: self.add_money("0.20", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_50_gr').clicked.connect(lambda: self.add_money("0.50", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_1_zl').clicked.connect(lambda: self.add_money("1.00", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_2_zl').clicked.connect(lambda: self.add_money("2.00", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_5_zl').clicked.connect(lambda: self.add_money("5.00", 'coin'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_10_zl').clicked.connect(lambda: self.add_money("10.00", 'banknote'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_20_zl').clicked.connect(lambda: self.add_money("20.00", 'banknote'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_50_zl').clicked.connect(lambda: self.add_money("50.00", 'banknote'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_100_zl').clicked.connect(lambda: self.add_money("100.00", 'banknote'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_200_zl').clicked.connect(lambda: self.add_money("200.00", 'banknote'))
        self.view_helper.find_button_by_object_name(self.ticket_machine.get_gui(), 'button_500_zl').clicked.connect(lambda: self.add_money("500.00", 'banknote'))

    def add_ticket(self, zone_number, price, type, label, code):
        counter = self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(), label)
        counter_int = int(counter.text())
        counter_int += 1
        counter.setText(str(counter_int))
        t = self.ticketFactory.createTicket(type, zone_number, price, code)
        self.order.add_ticket(t)
        self.update_informations()

    def update_informations(self):
        self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(), "label_tickets_count_value").setText(str(len(self.order.get_tickets())))
        self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(), "label_total_cost_value").setText(str(self.order.get_cost()))

    def remove_ticket(self, code, label):
        # search for specific ticket in list
        if any(x.code == code for x in self.order.get_tickets()):
            object_to_remove = next((x for x in self.order.get_tickets() if x.code == code))
            self.order.tickets.remove(object_to_remove)
            self.order.set_cost(self.order.get_cost() - object_to_remove.price)
            self.order.set_cost(float(round(Decimal(self.order.get_cost()), 2)))
            self.update_informations()
            # reduce counter
            counter = self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(), label)
            counter_int = int(counter.text())
            if counter_int > 0:
                counter_int -= 1
            counter.setText(str(counter_int))

    def change_view(self, view_name):
        if view_name == "payment" and len(self.order.get_tickets()) > 0:
            self.ticket_machine.get_gui().change_view(view_name)
            self.assign_payment_actions()
            self.view_helper.find_label_by_object_name(self.ticket_machine.get_gui(), "label_payment_left_value").setText(str(self.order.get_cost()) + " zł")

    def add_money(self, value, money_type):
        money = self.moneyFactory.createMoney(money_type, value)
        self.order.insert_money(money)
        if self.order.get_inserted_amount() >= self.order.get_cost():
            self.change_view("confirmation")

