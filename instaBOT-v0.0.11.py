#!C:\Users\Hamouda\AppData\Local\Programs\Python\Python39\python.exe

from selenium import webdriver as swd
from selenium.webdriver.common.by import By
from time import sleep
import random as rn
import stdiomask

chrome_options = swd.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driv= swd.Chrome(executable_path=r"F:\SelenINSTA\chromedriver.exe", options=chrome_options)
driv.get("https://www.instagram.com")
sleep(0.5)
driv.minimize_window()

# Random wating perids taken from three different timers
t1 = [5, 3.9201, 2.5785, 3.12, 4, 5.5027, 2.0, 4.825, 7, 6]
t2 = [1, 1.5, 3, 2, 1.05, 2, 3, 2.5, 8]
t3 = rn.randint(1, 5)
sleep(2)

# Target website automated login function
def Login(us, ps):
    driv.find_element_by_name('username').send_keys(us)
    driv.find_element_by_name('password').send_keys(ps)
    driv.find_element_by_xpath("//button[@type=\'submit\']").click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//button[text()="Not Now"]').click()
    sleep(rn.choice(t1))

# Target website automating reporting function 1 (Drug Related Report)
def Target_Drugs(tar_acc):
    driv.find_element_by_xpath("//div[@class='AFWDX']/button").click()
    sleep(rn.choice(t2))
    driv.find_element_by_xpath('//button[text()="Report User"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//*[text()="It\'s inappropriate"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//*[text()="Report Account"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//*[text()="It\'s posting content that shouldn\'t be on Instagram"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//*[text()="Sale of illegal or regulated goods"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath("//input[@id='igCoreRadioButtontag-0']").click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//button[text()="Submit Report"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//button[text()="Close"]').click()
    sleep(rn.choice(t2))

# Target website automating reporting function 2 (SPAM-Report)
def Target_Spam(tar_acc):
    driv.find_element_by_xpath("//div[@class='AFWDX']/button").click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//button[text()="Report User"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//*[text()="It\'s spam"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//button[text()="Close"]').click()
    sleep(rn.choice(t2))

# Target website automating reporting function 3 (Suicide-Report)
def Target_Suicide(tar_acc):
    driv.find_element_by_xpath("//div[@class='AFWDX']/button").click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//button[text()="Report User"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//*[text()="It\'s inappropriate"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//*[text()="Report Account"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//*[text()="It\'s posting content that shouldn\'t be on Instagram"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//*[text()="Suicide, self-injury or eating disorders"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//button[text()="Submit Report"]').click()
    sleep(rn.choice(t1))
    driv.find_element_by_xpath('//button[text()="Close"]').click()
    sleep(rn.choice(t2))

# Obtaining the user login and cerdentials
sleep(4)
print('\n')
print('\n#--------------------------------------------------------------#\n')
uname = input('Enter Your Username: ')
passc = stdiomask.getpass(prompt='Enter Your Password: ', mask='')
tar_acc = input('Enter Your Target Account Name: ')
rept = 1000
print("#============ Wait for 10 Seconds for instaBOT to Boot ============#")
sleep(1)

Login(uname, passc)
sleep(3)

# Main loop
driv.get("https://instagram.com/" + tar_acc)
driv.minimize_window()
sleep(3)

choice = ''
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n *-----------Welcome to instinstaBOTv0.0.11-----------*")
    print("[1] Enter 1 to  Report Drug-Sell-Account.")
    print("[2] Enter 2 to  Report Spam-Account.")
    print("[3] Enter 3 to  Report Suicide-Account.")
    print("[q] Enter q to  Quit.")

    choice = input("\nWhat would you like to do: ")

    if choice == '1':
        for i in range(1, int(rept) + 1):
            sleep(rn.choice(t2))
            Target_Drugs(tar_acc)
            sleep(rn.choice(t1))
            print(f'Report: {str(i).zfill(4)} --> {tar_acc} Reported as Drug Seller..!')
            sleep(rn.choice(t2))
    elif choice == '2':
        for i in range(1, int(rept) + 1):
            sleep(rn.choice(t2))
            Target_Spam(tar_acc)
            sleep(rn.choice(t2))
            print(f'Report: {str(i).zfill(4)} --> {tar_acc} Reported as Spam..!')
            sleep(rn.choice(t1))
    elif choice == '3':
        for i in range(1, int(rept) + 1):
            sleep(rn.choice(t2))
            Target_Suicide(tar_acc)
            sleep(rn.choice(t2))
            print(f'Report: {str(i).zfill(4)} --> {tar_acc} Reported as Suicidal..!')
            sleep(rn.choice(t1))
    elif choice == 'q':
        print("Thanks for using this amazing instaBOT. See you later.")
    else:
        print("Invalid choice, please try again.")

# Print the Bot termination message.
print("instaBOT is Terminated See You Soon.")
