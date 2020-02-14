from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from locators import *

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://base.consultant.ru/cons/"

    def go_to_site(self):
        self.driver.get(self.base_url)
        return MainPage(self.driver)

    def wait_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message = f"Can't find element by locator {locator}")
    def switch_to_window(self):
        return self.switch_to_window(self.driver.current_window_handle)

    def window_handles(self,index):
        return self.window_handles()

class MainPage(BasePage):
    def input_text(self, locator, input):
        self.driver.find_element(*locator).send_keys(input)

    def input_with_enter(self, locator, input):
        self.driver.find_element(*locator).send_keys(input + Keys.ENTER + Keys.ENTER)

    def check_elapse_time(self):
        self.input_text(MainPageLocators.LOCATOR_SEARCH_FIELD_XPATH, "G")
        #self.driver.find_element(MainPageLocators.LOCATOR_SEARCH_FIELD_XPATH).send_keys(Keys.ENTER)
       #self.driver.find_element(*MainPageLocators.LOCATOR_SEARCH_BUTTON_CSS).click()
        #self.driver.find_element(*MainPageLocators.LOCATOR_RESULT_CSS).click()
        #self.wait_element(ResultPageLocators.LOCATOR_BUTTON_HELP_XPATH)
        #print('switch_to_window' + self.switch_to_window())
        #self.switch_to_window(1)
        #self.driver.implicitly_wait(30)  # secon
        #search_text = self.driver.find_element(*MainPageLocators.LOCATOR_SEARCH_FIELD_RESULT_PAGE_XPATH).get_attribute("value")
        #return search_text

    def go_to_create_meeting_page(self):
        self.driver.find_element(*MainPageLocators.LOCATOR_SEARCH_FIELD_XPATH).click()
        return CreateMeetingPage(self.driver)

class CreateMeetingPage(BasePage):
    def go_to_constructor_meeting_page(self):
        self.driver.find_element(*CreateMeetingPageLocators.LOCATOR_CHOOSE_TEMPLATE_CSS).click()
        self.driver.find_element(*CreateMeetingPageLocators.LOCATOR_OVERHAUL_CSS).click()
        return ConstructorMeetingPage(self.driver)

class ConstructorMeetingPage(BasePage):
    def input_text(self, locator, input):
        self.driver.find_element(*locator).send_keys(input)

    def check_name_and_number_apartment(self):
        self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_button_form_archive_css).click()
        name_xpath = self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_name_xpath).text
        number_apartment_xpath = self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_number_apartment_xpath).text
        return (name_xpath, number_apartment_xpath)

    def check_download_form_archive(self):
        self.input_text(ConstructorMeetingPageLocators.LOCATOR_input_name_css, ConstructorMeetingPageLocators.name)
        self.input_text(ConstructorMeetingPageLocators.LOCATOR_input_number_apartment_css,
                        ConstructorMeetingPageLocators.number_apartment)
        self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_button_form_archive_css).click()
        self.wait_element(ConstructorMeetingPageLocators.LOCATOR_link_css)
        return self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_success_mesg_css).text

    def check_address_and_email(self):
        self.input_text(ConstructorMeetingPageLocators.LOCATOR_input_address_xpath,
                        ConstructorMeetingPageLocators.name_address)
        self.input_text(ConstructorMeetingPageLocators.LOCATOR_input_email_xpath, ConstructorMeetingPageLocators.email)
        self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_register_line_xpath).click()
        address_xpath = self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_address_xpath).get_attribute("value")
        email_css = self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_email_css).get_attribute("value")
        return (address_xpath, email_css)
