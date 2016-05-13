# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
import os,sys,time
reload(sys)
sys.setdefaultencoding('utf-8')


class Pyse(object):
    '''
        Pyse framework for the main class, the original 
    selenium provided by the method of the two packaging,
    making it easier to use.
    '''

    def __init__(self, browser='ff'):
        '''
        Run class initialization method, the default is proper
        to drive the Firefox browser. Of course, you can also
        pass parameter for other browser, Chrome browser for the "Chrome", 
        the Internet Explorer browser for "internet explorer" or "ie".
        '''
        if browser == "firefox" or browser=="ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "internet explorer" or browser=="ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        try:
            self.driver = driver
        except Exception:
            print "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'phantomjs' or 'chrome'." %browser

    def open(self, url):
        '''
        open url.

        Usage:
        driver.open("https://www.baidu.com")
        '''
        self.driver.get(url)

    def max_window(self):
        '''
        Set browser window maximized.

        Usage:
        driver.max_window()
        '''
        self.driver.maximize_window()

    def set_window(self, wide, high):
        '''
        Set browser window wide and high.

        Usage:
        driver.set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)

    def type(self, css, text):
        '''
        Operation input box.

        Usage:
        driver.type("#el","selenium")
        '''
        self.driver.find_element_by_css_selector(css).clear()
        self.driver.find_element_by_css_selector(css).send_keys(text)

    def click(self, css):
        '''
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..
        
        Usage:
        driver.click("#el")
        '''
        self.driver.find_element_by_css_selector(css).click()

    def right_click(self, css):
        '''
        Right click element.

        Usage:
        driver.right_click("#el")
        '''
        element = self.driver.find_element_by_css_selector(css)
        ActionChains(self.driver).context_click(element).perform()

    def move_to_element(self, css):
        '''
        Mouse over the element.

        Usage:
        driver.move_to_element("#el")
        '''
        element = self.driver.find_element_by_css_selector(css)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, css):
        '''
        Double click element.

        Usage:
        driver.double_click("#el")
        '''
        element = self.driver.find_element_by_css_selector(css)
        ActionChains(self.driver).double_click(element).perform()

    def drag_and_drop(self, el_css, ta_css):
        '''
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("#el","#ta")
        '''
        element = self.driver.find_element_by_css_selector(el_css)
        target = self.driver.find_element_by_css_selector(ta_css)
        ActionChains(driver).drag_and_drop(element, target).perform()

    def click_text(self, text):
        '''
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        '''
        aa = self.driver.find_elements_by_tag_name("a")
        for a in aa:
            try:
                if str(a.text) == text:
                    a.click()
            except StaleElementReferenceException:
                pass

    def close(self):
        '''
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        '''
        self.driver.close()

    def quit(self):
        '''
        Quit the driver and close all the windows.
        
        Usage:
        driver.quit()
        '''
        self.driver.quit()

    def submit(self, css):
        '''
        Submit the specified form.

        Usage:
        driver.submit("#el") 
        '''
        self.driver.find_element_by_css_selector(css).submit()

    def F5(self):
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):
        '''
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)

    def get_attribute(self, css, attribute):
        '''
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("#el","type")
        '''
        return self.driver.find_element_by_css_selector(css).get_attribute(attribute)

    def get_text(self, css):
        '''
        Get element text information.

        Usage:
        driver.get_text("#el")
        '''
        return self.driver.find_element_by_css_selector(css).text

    def get_display(self, css):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("#el")
        '''
        return self.driver.find_element_by_css_selector(css).is_displayed()

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        return self.driver.title

    def get_url(self):
        '''
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        '''
        return self.driver.current_url

    def get_windows_img(self, file_path):
        '''
        Get the current window screenshot.

        Usage:
        driver.get_windows_img()
        '''
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, secs):
        '''
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)

    def element_wait(self, css, secs):
        '''
        Waiting for an element to display.
        
        Usage:
        driver.element_wait("#el",10)
        '''
        for i in range(secs):
            try:
                el = self.driver.find_element_by_css_selector(css).is_displayed()
                print el
                print type(el)
                print type(True)
                if el:
                    break
            except: pass
            time.sleep(1)
        else: print "time out"

    def accept_alert(self):
        '''
        Accept warning box.

        Usage:
        driver.accept_alert()
        '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.
        
        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):
        '''
        Switch to the specified frame.
        
        Usage:
        driver.switch_to_frame("#el")
        '''
        xf = self.driver.find_element_by_css_selector(css)
        self.driver._switch_to.frame(xf)

    def switch_to_frame_out(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        
        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver._switch_to.default_content()

    def open_new_window(self, css):
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        '''
        driver = self.driver
        original_windows = driver.current_window_handle
        driver.find_element_by_css_selector(css).click()
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                driver._switch_to.window(handle)


if __name__ == '__main__':
    driver = Pyse("chrome")
