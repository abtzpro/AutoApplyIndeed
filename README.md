# AutoApplyIndeed
AutoApplyIndeed an attempt to automate the indeed jobs application process

## What is AutoApplyIndeed ?
This script is designed to help you automatically apply for job listings on the Indeed website. It uses a tool called Selenium WebDriver, which essentially acts as a web browser that can be controlled by code.

Here’s how the script works:

	1.	It starts by setting up the Selenium WebDriver to use Google Chrome as the browser. You’ll need to provide the path to the Chrome driver on your computer.
	2.	The script then opens the Indeed website.
	3.	It looks for job listings on the page using specific patterns in the website’s code.
	4.	For each job listing found, the script does the following:
	•	Extracts important details like the job title, company name, and a link to apply for the job.
	•	Clicks on the apply button for that job.
	•	Waits for a short time for the application form to load.
	•	Fills in the form with your name and email address.
	•	Attaches your resume file to the application.
	•	Submits the application by clicking the submit button.
	•	Waits for a short time before moving on to the next job listing (to be considerate and avoid spamming).
	5.	Once all the job listings have been processed, the script closes the web browser.

## Usage Notes
Please note that you still need to replace 'path_to_chromedriver' with the actual path to your chromedriver executable, and 'path_to_resume.pdf' with the actual path to your resume file.

## Credits
Adam Rivers, Hello Security LLC, AI Automation

