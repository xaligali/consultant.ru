import pytest
from selenium import webdriver
from pages import *

@pytest.fixture(scope = "session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.implicitly_wait(10) # seconds
    driver.maximize_window()
    mainpage = BasePage(driver).go_to_site()

    #createmeetingpage = mainpage.go_to_create_meeting_page()
    #constructormeetingpage = createmeetingpage.go_to_constructor_meeting_page()
    #print('print',constructormeetingpage)
    yield mainpage

    #yield driver
    #driver.quit()


@pytest.fixture(scope='function', autouse=True)
def testcase_result(request):
    print("Test '{}' STARTED".format(request.node.nodeid))
    def fin():
        print("Test '{}' COMPLETED".format(request.node.nodeid))
        print("Test '{}' DURATION={}".format(request.node.nodeid, request.node.rep_call.duration))
        request.addfinalizer(fin)


def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep
