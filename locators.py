from selenium.webdriver.common.by import By

class MainPageLocators:
    """"A class for main page locators. All main page locators should come here"""
    LOCATOR_SEARCH_FIELD_XPATH = (By.XPATH, "//*[@id='dictFilter']")
    LOCATOR_SEARCH_FIELD_CSS = (By.CSS_SELECTOR, "[class ='filterContainer']")
    SEARCH_TEXT = "нк ч2"
    LOCATOR_SEARCH_BUTTON_CSS =(By.CSS_SELECTOR, "[class='runsearch flat']")
    LOCATOR_RESULT_CSS =(By.CSS_SELECTOR, "[class='row current']")
    LOCATOR_SEARCH_FIELD_RESULT_PAGE_XPATH = "(//*[@id='dictFilter'])[1]"

class ResultPageLocators:
    """A class for create meeting page locators. All search results locators should come here"""
    LOCATOR_BUTTON_HELP_XPATH = (By.XPATH, "//*[text() = 'Справка']")


class CreateMeetingPageLocators:
    """A class for create meeting page locators. All search results locators should come here"""
    LOCATOR_CHOOSE_TEMPLATE_CSS = (By.CSS_SELECTOR, "[class='act tt_choose_template']")
    LOCATOR_OVERHAUL_CSS = (By.CSS_SELECTOR, "[class='btn btn-blue btn-sm tt_overhaul']")

class ConstructorMeetingPageLocators:
    """A class for constructor meeting page locators. All search results locators should come here"""

    LOCATOR_button_form_archive_css = (By.CSS_SELECTOR, "[class='download-link tt_form_archive']")
    LOCATOR_name_xpath = (By.XPATH, "(//*[@class='error__text'])[1]")
    LOCATOR_number_apartment_xpath = (By.XPATH, "(//*[@class='error__text'])[2]")
    LOCATOR_input_name_css = (By.CSS_SELECTOR, "[name = 'full_name']")
    LOCATOR_input_number_apartment_css = (By.CSS_SELECTOR, "[name = 'apartment']")
    LOCATOR_link_css = (By.CSS_SELECTOR, "[class='link tt_download_link']")
    LOCATOR_success_mesg_css = (By.CSS_SELECTOR, "[class='sub-info']")
    LOCATOR_input_email_xpath = (By.XPATH, "//*[@id='eid_meeting_creator_email']")
    LOCATOR_email_css = (By.CSS_SELECTOR, "[class='field4 filled ']")
    LOCATOR_input_address_xpath = (By.XPATH, "//*[@name='long_name']")
    LOCATOR_address_xpath = (By.XPATH, "(//*[@name='long_name'])[2]")
    LOCATOR_register_line_xpath = (By.XPATH, "//*[text()='Заказать реестр']")
    error_mesg_name = "Фамилия и имя являются обязательными"
    error_mesg_number = "Поле является обязательным"
    name = "Ivanov Ivan"
    number_apartment = "15"
    success_mesg = "Ваш архив с документами сформирован и доступен по этой ссылке"
    email = "xgr@mailinator.com"
    name_address = "Москва, улица Скульптора Мухиной"