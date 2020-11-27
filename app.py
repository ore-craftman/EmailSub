from selenium import webdriver
import time
import random
import string

#Generate Random emails
chars_after_at = 8
letters_list = [string.digits, string.ascii_lowercase, string.ascii_uppercase]
letters_list_to_str = "".join(letters_list)
email_format = "@gmail.com"
email_generated = "".join(random.choices(letters_list_to_str, k=chars_after_at)) + email_format

#Initiate Automation
web = webdriver.Chrome()
web.get('http://riseupcapitalpartners.com/')
time.sleep(2)


# Loop this shit
x = 1
while x < 2000:
    input_email = web.find_element_by_id('forminator-field-email-1')
    input_email.send_keys(email_generated)
    time.sleep(2)

    #Subscribe
    subscribe = web.find_element_by_xpath('//*[@id="submit"]/button')
    subscribe.click()
    time.sleep(50)
    x += 1


#Call me cRaftman, I build with Javascript, Automate with Python and Womanize with...