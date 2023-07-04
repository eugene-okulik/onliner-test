from pages.cars import CarsPage
import pytest


@pytest.mark.parametrize('option_id', list(range(1, 8)))
def test_click_dropdown(driver, option_id):
    cars_page = CarsPage(driver)
    cars_page.open()
    text_before_sort = cars_page.first_car_name_text()
    cars_page.click_sort_dropdown()
    cars_page.select_option(option_id)
    text_after_sort = cars_page.first_car_name_text()
    assert text_before_sort == text_after_sort
