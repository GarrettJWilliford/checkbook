import threading
import pickle
import checkbook_animation_files as caf
import time
import os
import datetime
import re

#####################RESET_SAVE_FILES#########################################
def save_file_reset():
    try:
        pickle.dump(0, open('account_inf.p', 'wb'))
        pickle.dump({}, open('recent_transactions.p', 'wb'))
        print('task_completed')
    except:
        error_code = input('error code 4 : error while reseting info')


#save_file_reset()
#############################################################################

def header_animation():
    ani = threading.Thread(target = caf.checkbook_animation_files)
    ani.start()

def checkbook_ui_repeat():
    print('____________________-=====CHECKBOOK=====-____________________')



def recents():
    rt = [
         "+                                                            +",
         "+  RECENT Transactions                                       +",
         "+  -------------------                                       +",
         "+ >> %1s | %20s | $%8s              +",
         "--------------------------------------------------------------"]
    try:
        recent = pickle.load(open('recent_transactions.p', 'rb'))
    except:
        error_code = input('error code 5 : recent transaction ledger not found')
        return
    checkbook_ui_repeat()
    #print(recent)
    print('%s\n%s\n%s\n' % (rt[0], rt[1], rt[2]))
    for i in range(0, 9):
        #print(recent[str(len(recent)(])
        try:
            print(rt[3] % (recent[str(len(recent) - i)][0], recent[str(len(recent) - i)][1], recent[str(len(recent) - i)][2]))
        except:
            print(rt[0])
    print(rt[4])
    


def checkbook_ui(is_stagnant = False):
    checks = [
              "+                                                            +",
              "+  1) view current balance                                   +",
              "+                                                            +",
              "+                                                            +",
              "+  2) record a debit (withdraw)                              +",
              "+                                                            +",
              "+                                                            +",
              "+  3) record a credit (deposit)                              +",
              "+                                                            +",
              "+                                                            +",
              "+  4) exit                                                   +",
              "--------------------------------------------------------------"]
    for c in checks:
        print(c)
        if is_stagnant == False:
            time.sleep(.04)

def display_amount():
    checkbook_ui_repeat()
    print("""+                                                            +
+                                                            +
+   AMOUNT                                                   +
+   -------------------                                      +
+    $%10s                                             +
+                                                            +
+                                                            +
+                                                            +
+                                                            +
+                                                            +
+                                                            +
+                                                            +
--------------------------------------------------------------

""" % (pickle.load(open('account_inf.p', 'rb'))))

def add_or_withdraw(isdeposit, inp):
    try:
        account_info = pickle.load(open('account_inf.p', 'rb'))
        transactions = pickle.load(open('recent_transactions.p', 'rb'))
    except:
        error_code = input('error code 3 : banking info not found')
        return
    dorw = 'D'
    if isdeposit == False:
        inp = '-' + str(inp)
        dorw = 'W'
    try:
        account_info += round(float(inp), 2)
        if account_info < 0:
            return
        pickle.dump(account_info, open('account_inf.p', 'wb'))
        transactions[str(len(transactions) + 1)] = [dorw, datetime.datetime.now(), inp]
        pickle.dump(transactions, open('recent_transactions.p', 'wb'))
    except:
        error_code = input('error code 2 : invalid command')
        return

        



def the_whole_bannana():
    try:
        pickle.load(open('account_inf.p', 'rb'))
        pickle.load(open('recent_transactions.p', 'rb'))
    except:
        pickle.dump(0, open('account_inf.p', 'wb'))
        pickle.dump({}, open('recent_transactions.p', 'wb'))
    os.system('clear')
    header_animation()
    time.sleep(2.1)
    checkbook_ui()
    while True:
        os.system('clear')
        checkbook_ui_repeat()
        checkbook_ui(is_stagnant = True)        
        inp = input('>>|ENTER COMMAND|>> ')
        commands = ['1', '2', '3', '4']
        if inp not in commands:
            os.system('clear')
            checkbook_ui_repeat()
            checkbook_ui(is_stagnant = True)
            inp = input('<<|UNKOWN COMMAND(press enter to continue)|>>')
        if inp == commands[0]:
            caf.flush()
            os.system('clear')
            display_amount()
            inp = input('<<|PRESS ENTER TO CONTINUE|>>')
        if inp == commands[1]:
            caf.flush()
            os.system('clear')
            recents()
            inp = input('>>|AMOUNT|>> ' )
            add_or_withdraw(False, inp)
            os.system('clear')
            output = recents()
            try:
                if pickle.load(open('account_inf.p','rb')) - float(inp) < 0.0:
                    inp = input('<<|INSUFFUCIENT FUNDS(press enter to continue)|>>')
                else:
                    inp = input('<<|DEBIT RECORDED(press enter to continue)|>>')
            except:
                continue
        if inp == commands[2]:
            caf.flush()
            os.system('clear')
            recents()
            inp = input('>>|AMOUNT|>> ')
            add_or_withdraw(True, inp)
            os.system('clear')
            recents()
            inp = input('<<|CREDIT RECORDED(press enter to continue)|>>')
        if inp == commands[3]:
            caf.exit_animation()
            os.system('clear')
            return
the_whole_bannana()