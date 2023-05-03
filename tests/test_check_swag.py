from pages.swag_labs import SwagLabs


def test_check_elements(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    assert swag_labs.exist_icon()
    assert swag_labs.exist_input_name()
    assert swag_labs.exist_input_password()

