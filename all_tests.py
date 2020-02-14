

def test_check_time(browser):
    res = browser.check_elapse_time()
    #assert "нк ч2" == res

# def test_check_form_archive_negative(browser,testcase_result):
#     result = browser.check_name_and_number_apartment()
#     assert "Фамилия и имя являются обязательными" == result[0]
#     assert "Поле является обязательным" == result[1]
#
# def test_check_form_archive_positive(browser):
#     assert "Ваш архив с документами сформирован и доступен по этой ссылке" == browser.check_download_form_archive()
#
# def test_check_address_and_email_positive(browser):
#     result = browser.check_address_and_email()
#     assert "Москва, улица Скульптора Мухиной" == result[0]
#     assert "xgr@mailinator.com" ==  result[1]