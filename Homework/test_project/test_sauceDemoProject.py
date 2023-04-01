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





