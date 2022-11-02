
https://www.jetbrains.com/help/pycharm/markdown.html#preview

#Acceptance Test for My Store 

---
##Introduction

This acceptance test with Selenium is a project aiming to improve my technical skills. It is written in python, adopts a data-driven approach using data feed via Google Sheet API, and can be displayed on the allure report.This project includes two main tests, a registration test and a login test.
<br/><br/>
####The Registration Test
The purpose of the registration test is to test if the user can fill the registration form and register successfully, aßnd to test if the personal information the user fills on the registration page is consistent with the information displayed on the personal information page. 
<br/><br/>
####The Login Test
The purpose of the login test is to test if the user can fill the login form and login successfully using the personal information that is filled on the registration form. 

---




Generating Allure report using pytest
In your project directory, you first need to generate a folder to save the allure reports, you can automatically generate this with a command
allure generate
This will create a folder named allure-report in your project directory.

You are now set to run your test with pytest runner by specifying the directory path to save your allure report, for example :
pytest --alluredir=allure-report/
Once test execution completes, all the test results would get stored in allure-report directory.

You can now view the allure-report in the browser with the command –
allure serve allure-report/


