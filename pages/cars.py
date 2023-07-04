from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


sort_dropdown = (
    By.XPATH,
    '//*[@class="vehicle-form__link vehicle-form__link_other vehicle-form__link_base vehicle-form__link_arrow_bottom"]'
)
first_car_name = (
    By.CLASS_NAME,
    'vehicle-form__offers-part_title'
)
options_list = (
    By.XPATH,
    (
        '//*[@class="dropdown-style__container"]'
    )
)


class CarsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://ab.onliner.by/')

    def click_sort_dropdown(self):
        self.find(sort_dropdown).click()

    def first_car_name_text(self):
        return self.find(first_car_name).text

    def select_option(self, option_id):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(options_list))
        self.find(options_list).find_element(By.XPATH, '//*[@class="dropdown-style__item dropdown-style__item_active"]').click()

