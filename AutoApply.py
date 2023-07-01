import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('path_to_chromedriver')
driver.get('https://www.indeed.com')

job_listings = driver.find_elements_by_xpath('//div[@class="jobsearch-SerpJobCard"]')

for listing in job_listings:
    job_title = listing.find_element_by_xpath('.//h2[@class="jobTitle"]')
    company_name = listing.find_element_by_xpath('.//span[@class="companyName"]')
    apply_link = listing.find_element_by_xpath('.//a[@class="jobLink"]')
    
    apply_button = listing.find_element_by_xpath('.//button[@class="jobsearch-SerpJobCard-footerActions--apply-button"]')
    apply_button.click()
    
    time.sleep(2)
    
    name_input = driver.find_element_by_xpath('//input[@id="applicant.name"]')
    name_input.send_keys("Your Name")
    
    email_input = driver.find_element_by_xpath('//input[@id="applicant.email"]')
    email_input.send_keys("example@example.com")
    
    resume_input = driver.find_element_by_xpath('//input[@id="resume"]')
    resume_input.send_keys("path_to_resume.pdf")
    
    submit_button = driver.find_element_by_xpath('//button[@id="vjs-apply-button"]')
    submit_button.click()
    
    time.sleep(2)

driver.quit()
