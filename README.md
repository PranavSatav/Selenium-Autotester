# Selenium-Autotester
This code automates the login process on a web page by entering the username "123" and password "abc" into the respective input fields and clicking the submit button. It then locates and clicks a login button using an XPath expression. Finally, it waits for 5 seconds before closing the browser window.

How to Run -
1. Open the app.py code in visual studio.
2. Make sure you have 'Chrome' web browser installed in your system.
3. Check your Chrome version from settings >> eg. Version 114.0.5735.199 (Official Build) (64-bit)
4. https://chromedriver.chromium.org/downloads using this link, get yourself a ChromeWebDriver.exe
5. Paste this driver near ur app.py file
6. Run the app.py and it will automatically perform tasks

How to Configure Tasks-
1. driver.get("https://x7propranav.000webhostapp.com/auto/")
   This opens a website which ive created as a start point.
   
2.   username_field = driver.find_element(By.ID, "username")
     username_field.send_keys("123")

     password_field = driver.find_element(By.ID, "password")
     password_field.send_keys("abc")

     This code finds the HTML ELEMENT from the whole WEBSITE and automatically inserts the given values.

3.   submit_button = driver.find_element(By.ID, "submit")
     submit_button.click()

     This code AUTOMATICALLY Clicks the SUBMIT BUTTON.

4. Example - After login, there is a PDF File you want to download, here
   i've used,
       login_button = driver.find_element(By.XPATH, "/html/body/button")
       login_button.click()

   This code finds the specific element 'BUTTON' using XPATH method
   (you can find specific XPATH just by rightclicking any element and there is option to "COPY XPATH", its that simple)

5. Additionally, i've used time.sleep(2) for 2 seconds delay between eah process so i can seee everything slowly.
