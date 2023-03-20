from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Test_sauceDemo:

    def emptyInfo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        loginButton = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginButton.click()

        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Test Result Is: {testResult}")

        while True:
            continue
    
    def emptyPassword(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        userName = driver.find_element(By.ID, "user-name")
        sleep(2)
        userName.send_keys("standard_user")
        loginButton = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginButton.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Result Is: {testResult}")

        while True:
            continue

    def lockedUser(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        userName = driver.find_element(By.ID, "user-name")
        sleep(2)
        userName.send_keys("locked_out_user")
        userPassword = driver.find_element(By.ID, "password")
        sleep(2)
        userPassword.send_keys("secret_sauce")
        loginButton = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginButton.click()

        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Result Is: {testResult}")

        while True:
            continue

    def closingMessage(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        loginButton = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginButton.click()

        messageButton = driver.find_element(By.CLASS_NAME, "error-button")
        sleep(2)
        messageButton.click()

        while True:
            continue

    def validLogin(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        userName = driver.find_element(By.ID, "user-name")
        sleep(2)
        userName.send_keys("standard_user")
        userPassword = driver.find_element(By.ID, "password")
        sleep(2)
        userPassword.send_keys("secret_sauce")

        loginButton = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginButton.click()

        while True:
            continue
    
    def countOfProduct(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        userName = driver.find_element(By.ID, "user-name")
        sleep(2)
        userName.send_keys("standard_user")
        userPassword = driver.find_element(By.ID, "password")
        sleep(2)
        userPassword.send_keys("secret_sauce")

        loginButton = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginButton.click()
        sleep(2)

        listOfProducts = driver.find_elements(By.CLASS_NAME, "inventory_item")
        sleep(2)
        print(f"There are {len(listOfProducts)} products in total.")
        
        while True:
            continue



testClass = Test_sauceDemo()
#testClass.emptyInfo()
#testClass.emptyPassword()
#testClass.lockedUser()
#testClass.closingMessage()
#testClass.validLogin()
#testClass.countOfProduct()
