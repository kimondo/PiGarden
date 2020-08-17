#Raspberry Pi Garden version 1.0
#=======================================================================
# coding: utf8

# Import the modules needed to run the script.
import sys, os
import automationhat
import time

#Main definition - constants
menu_actions  = {}

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')
    print "Welcome, to the Raspberry Pi Garden Management System \n"
    print "Please choose the menu you want to start:"
    print "1. Start webcam"
    print "2. Stop webcam"
    print "3. Activate watering cycle"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Menu 1
def menu1():
    print "Start webcam\n"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# Menu 2
def menu2():
    print "Stop Webcam \n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Menu 3
def menu3():
    print "Activating watering cycle.. \n"
   #switch on relay 1 and wait 10 seconds

    automationhat.relay.one.on()
    time.sleep(10)
    automationhat.relay.one.toggle()
    print "Completed! \n"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '9': back,
    '0': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    #Launch main menu
    main_menu()
