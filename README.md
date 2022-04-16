# **CPU Benchmarks scrapping program**


## Goal of the project

The goal of the project is to get information about the different Prices and rankings of the CPUs on the *"userbenchmarks"* website. The ranking system is based on the price and features the CPUs offer.

## Technologies used

* **Python.**
* **Selenium Library.**
* **Excel Spreadsheets.**
* **Pandas library.**

## Description of the scrapping process

In the beginning, the most important variables are defined, note that we are using the *Chrome web driver*, therefore it's completely necessary to have *chromedriver.exe* installed.
 
Next, the driver gets to the *UserBenchmarks URL*, where once loaded the page, the function **Save** is called with the return of the **GetData** function as the parameter.

The **GetData** function gets the information about all CPUs on the page. Since they are ==dynamically generated with javascript==, the program makes use of the features of the *Selenium library* to click the *next button* to change the page dynamically once the information of all the 50 CPUs is presented on each page is retrieved.

Finally, the **Save** function exports all the data to the *CPUs.xls* Excel File.