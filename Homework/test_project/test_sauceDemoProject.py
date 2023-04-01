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

class Test_Project():

  def setup_method(self):

    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.maximize_window()
    self.driver.get("https://www.saucedemo.com/")
  
  def teardown_method(self, method):

    self.driver.quit()
  
  def test_emptyUsername(self):

    WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
    password = self.driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    loginButton = self.driver.find_element(By.ID, "login-button")
    loginButton.click()

    errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
    assert errorMessage.text == "Epic sadface: Username is required"

  def test_emptyPassword(self):

    WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
    username = self.driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    loginButton = self.driver.find_element(By.ID, "login-button")
    loginButton.click()

    errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
    assert errorMessage.text == "Epic sadface: Password is required"

  def test_lockedOutUser(self):

    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "user-name")))
    username = self.driver.find_element(By.ID, "user-name")
    username.send_keys("locked_out_user")

    WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
    password = self.driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    loginButton = self.driver.find_element(By.ID, "login-button")
    loginButton.click()

    errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
    assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

  def test_validLogin(self):

    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "user-name")))
    username = self.driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
    password = self.driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    loginButton = self.driver.find_element(By.ID, "login-button")
    loginButton.click()

  def test_logout(self):

    username = self.driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = self.driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    loginButton = self.driver.find_element(By.ID, "login-button")
    loginButton.click()
    hamburgerButton = self.driver.find_element(By.ID, "react-burger-menu-btn")
    hamburgerButton.click()

    WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "logout_sidebar_link")))
    logoutButton = self.driver.find_element(By.ID, "logout_sidebar_link")
    logoutButton.click()

  def test_addToCart(self):

    username = self.driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = self.driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    loginButton = self.driver.find_element(By.ID, "login-button")
    loginButton.click()

    productOne = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    productOne.click()
    productTwo = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    productTwo.click()
    productThree = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    productThree.click()

  def test_deleteFromCart(self):
    username = self.driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = self.driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    loginButton = self.driver.find_element(By.ID, "login-button")
    loginButton.click()

    productOne = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    productOne.click()
    productTwo = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    productTwo.click()

    shoppinCart = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a")
    shoppinCart.click()
    deleteProduct = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
    deleteProduct.click()

  def test_invalidCheckOut(self):
    username = self.driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = self.driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    loginButton = self.driver.find_element(By.ID, "login-button")
    loginButton.click()

    productOne = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    productOne.click()
    productTwo = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    productTwo.click()
    productThree = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    productThree.click()

    WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a")))
    shoppinCart = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a")
    shoppinCart.click()
    checkoutButton = self.driver.find_element(By.ID, "checkout")
    checkoutButton.click()

    WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "continue")))
    continueButton = self.driver.find_element(By.ID, "continue")
    continueButton.click()
    errorMessage = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/form/div[1]/div[4]/h3")
    assert errorMessage.text == "Error: First Name is required"

  def test_validCheckOut(self):

    username = self.driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = self.driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    loginButton = self.driver.find_element(By.ID, "login-button")
    loginButton.click()
    productOne = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    productOne.click()
    productTwo = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    productTwo.click()
    productThree = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    productThree.click()
    WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a")))
    shoppinCart = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a")
    shoppinCart.click()
    checkoutButton = self.driver.find_element(By.ID, "checkout")
    checkoutButton.click()

    WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "first-name")))
    firstname = self.driver.find_element(By.ID, "first-name")
    firstname.send_keys("username")
    lastname = self.driver.find_element(By.ID, "last-name")
    lastname.send_keys("last-name")
    zCode = self.driver.find_element(By.ID, "postal-code")
    zCode.send_keys("665")
    continueButton = self.driver.find_element(By.ID, "continue")
    continueButton.click()

    WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "finish")))
    finishButton = self.driver.find_element(By.ID, "finish")
    finishButton.click()


    





    

  









