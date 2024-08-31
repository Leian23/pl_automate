from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Pages.access_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


wrestling = (By.XPATH, "//*[@id='qx-sports-con']/div[17]/div/div[3]/div/div[1]/a")
close_tips = (By. XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[1]/div[3]/div/div/div/div/p/div/div[2]/div/button/span")
wrestling_text = (By.XPATH, "//*[@id='section-design-type']/div[1]/div[1]/div")
color_wheel = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[1]/div[2]/a/span/img")

# *Select color
turquoise = (By.XPATH, "//*[@id='design-page-modal-color-library']/div/div/div[2]/div/div/div[71]/label")
usaf_royal = (By.XPATH, "//*[@id='design-page-modal-color-library']/div/div/div[2]/div/div/div[92]/label")
yellow = (By.XPATH, "//*[@id='design-page-modal-color-library']/div/div/div[2]/div/div/div[50]/label")
brick_red = (By.XPATH, "//*[@id='design-page-modal-color-library']/div/div/div[2]/div/div/div[40]/label")
natural = (By.XPATH, "//*[@id='design-page-modal-color-library']/div/div/div[2]/div/div/div[5]/label")
heather_royal = (By.XPATH, "//*[@id='design-page-modal-color-library']/div/div/div[2]/div/div/div[3]/label")
save_color = (By.XPATH, "//*[@id='design-page-modal-color-library']/div/div/div[3]/div/div[2]/button")

# * Validate selected color
sld_color_1 = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/a/div[2]")
sld_color_2 = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/a/div[2]")
sld_color_3 = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/a/div[2]")
sld_color_4 = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[4]/a/div[2]")
sld_color_5 = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/a/div[2]")
sld_color_6 = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[6]/a/div[2]")

# loaded items
reselect_color_wheel = (By.XPATH, "//*[@id='section-design-type']/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/a[1]/span/img")
loading_time = (By.XPATH, "//*[@id='alert-message-container']/div/div[1]/div/div[2]/div[1]")
clear_selected_colors = (By.XPATH, "//*[@id='design-page-modal-color-library']/div/div/div[3]/div/div[1]/button")
confirm_clear = (By.XPATH, "//*[@id='confirmation-modal']/div/div/div[2]/div/div[1]/button")





class ColorWheel(BasePage):
        
    def click_wrestling_item(self):
       return self.wait_driver(wrestling)
    def check_wrestling_text(self):
        return self.wait_driver(wrestling_text)
    def close_tips(self):
        return self.wait_click_driver(close_tips)
    def color_picker(self):
        return self.wait_driver(color_wheel)
    
    #colors
    def selected_clr1(self):
        return self.wait_driver(sld_color_1).text
    def selected_clr2(self):
        return self.wait_driver(sld_color_2).text
    def selected_clr3(self):
        return self.wait_driver(sld_color_3).text
    def selected_clr4(self):
        return self.wait_driver(sld_color_4).text
    def selected_clr5(self):
        return self.wait_driver(sld_color_5).text
    def selected_clr6(self):
        return self.wait_driver(sld_color_6).text
    
    #validate colors
    def select_turquoise(self):
        return self.wait_driver(turquoise)
    def select_usaf_royal(self):
        return self.wait_driver(usaf_royal)
    def select_yellow(self):
        return self.wait_driver(yellow)
    def select_brick_red(self):
        return self.wait_driver(brick_red)
    def select_natural(self):
        return self.wait_driver(natural)
    def select_heather_royal(self):
        return self.wait_driver(heather_royal)
    
    
    #save_colors
    def save_selected_color(self):
        return self.wait_driver(save_color)
    def reselect_color_wheel(self):
     return self.wait_driver(reselect_color_wheel)
    def clear_selected_colors(self):
     return self.wait_driver(clear_selected_colors)
    def confirm_clear(self):
     return self.wait_driver(confirm_clear)

    #loaded items
    def items_loaded(self):
        return self.wait_invisibility(loading_time)

    

        
    
    
    
    