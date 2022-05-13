from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'C:\WebDriver\geckodriver.exe')

def test_launch_browser():
    assert driver.name == 'firefox'