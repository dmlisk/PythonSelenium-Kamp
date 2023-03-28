from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_sauceDemo:

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        #screenshot date
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    def test_emptyInfo(self):
        
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(self.folderPath+"/test_emptyInfo.png")
        assert errorMessage.text == "Epic sadface: Username is required"
        
    def test_emptyPassword(self):

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(self.folderPath+"/test_emptyPassword.png")
        assert errorMessage.text == "Epic sadface: Password is required"

    def test_lockedUser(self):
        
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("locked_out_user")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(self.folderPath+"/test_lockedUser.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        
    def test_closingMessage(self):
        
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()

        messageButton = self.driver.find_element(By.CLASS_NAME, "error-button")
        messageButton.click()
        self.driver.save_screenshot(self.folderPath+"/test_closingMessage.png")

    def test_validLogin(self):
    
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.driver.save_screenshot(self.folderPath+"/test_validLogin.png")

    def test_countOfProduct(self):
       
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()

        listOfProducts = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(self.folderPath+"/test_countOfProduct.png")
        print(f"There are {len(listOfProducts)} products in total.")

   
    def test_addToCart(self):

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
        productOne = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        productOne.click()

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-bike-light")))
        productTwo = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        productTwo.click()

        shoppinCart = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a")
        shoppinCart.click()
        self.driver.save_screenshot(self.folderPath+"/test_addToCart.png")

    def test_deleteFromCart(self):

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
        productOne = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        productOne.click()

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-bike-light")))
        productTwo = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        productTwo.click()

        shoppinCart = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a")
        shoppinCart.click()

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "remove-sauce-labs-backpack")))
        deleteProduct = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        deleteProduct.click()
        self.driver.save_screenshot(self.folderPath+"/test_deleteFromCart.png")

    @pytest.mark.parametrize("username, password", [("abc", "123") , ("xyz", "abc"), ("123", "345")])
    def test_invalidLogin(self, username, password):

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys(username)
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys(password)

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(self.folderPath+"/test_invalidLogin.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"




