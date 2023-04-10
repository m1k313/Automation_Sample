from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


@given('the Speedbird Cafe product list page is open')
def step_open_product_list_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://highlifeshop.com/speedbird-cafe")


# Decline cookies
@when('I decline cookies')
def step_impl(context):
    driver = context.driver
    for i in range(10):
        try:
            driver.find_element(By.XPATH, "//*[text()='DECLINE ALL NON-ESSENTIAL COOKIES']").click()
            break
        except NoSuchElementException:
            time.sleep(1)


@when('the user clicks on the "Sort by" dropdown')
def step_click_sort_by_dropdown(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "sorter"))
    )
    context.driver.find_element(By.ID, "sorter").click()


@then('there are 4 sorting options available')
def step_verify_sorting_options(context):
    sorting_options = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//select[@id='sorter']/option"))
    )
    assert len(sorting_options) == 4, f"Expected 4 sorting options, but got {len(sorting_options)}"
    context.driver.quit()
