
https://www.jetbrains.com/help/pycharm/markdown.html#preview



Generating Allure report using pytest
In your project directory, you first need to generate a folder to save the allure reports, you can automatically generate this with a command
allure generate
This will create a folder named allure-report in your project directory.

You are now set to run your test with pytest runner by specifying the directory path to save your allure report, for example :
pytest --alluredir=allure-report/
Once test execution completes, all the test results would get stored in allure-report directory.

You can now view the allure-report in the browser with the command –
allure serve allure-report/


