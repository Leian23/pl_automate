from Utilities.baseclass import BaseClass
from Pages.color_picker_page_wrestling import ColorWheel
from Assets.credentials import green_color, reset_color
import time


class Test_first_test(BaseClass):

    def test_click_wrestling(self):
        item1_page = ColorWheel(self.driver) 
        click_wrestling = item1_page.click_wrestling_item() 
        self.driver.execute_script("arguments[0].scrollIntoView();", click_wrestling)
        click_wrestling.click()
    
    def test_validate_wrestling_sport(self):
        item1_page = ColorWheel(self.driver) 
        validate_wrestling = item1_page.check_wrestling_text().text.lower()
        print(green_color + f"Current page is: {validate_wrestling}" + reset_color)
        assert validate_wrestling == "wrestling", "You are not in wrestling page"
        item1_page.close_tips().click()
    

    def test_click_color_wheel(self):
        item1_page = ColorWheel(self.driver) 
        click_color_wheel = item1_page.c

        click_color_wheel.click()
        time.sleep(2)

    def test_click_color(self):
        item1_page = ColorWheel(self.driver) 

        turqouise = item1_page.select_turquoise()
        self.driver.execute_script("arguments[0].scrollIntoView();", turqouise )
        turqouise.click()

        usaf_royal = item1_page.select_usaf_royal()
        self.driver.execute_script("arguments[0].scrollIntoView();", usaf_royal)
        usaf_royal.click()

        yellow = item1_page.select_yellow()
        self.driver.execute_script("arguments[0].scrollIntoView();", yellow)
        yellow.click()

        brick_red = item1_page.select_brick_red()
        self.driver.execute_script("arguments[0].scrollIntoView();", brick_red)
        brick_red.click()

        natural = item1_page.select_natural()
        self.driver.execute_script("arguments[0].scrollIntoView();", natural)
        natural.click()

        heather_royal = item1_page.select_heather_royal()
        self.driver.execute_script("arguments[0].scrollIntoView();", heather_royal)
        heather_royal.click()

        assert (turqouise.is_displayed() and usaf_royal.is_displayed() and 
        yellow.is_displayed() and brick_red.is_displayed() and 
        natural.is_displayed() and heather_royal.is_displayed()), "One or more colors are not displayed correctly."
        print(green_color + f"All selected colors are available" + reset_color)

    def test_save_colors(self):
        item1_page = ColorWheel(self.driver)
        save_color_btn = item1_page.save_selected_color()
        self.driver.execute_script("arguments[0].scrollIntoView();", save_color_btn)
        save_color_btn.click()
        

    def test_validate_turqouise(self):
        item1_page = ColorWheel(self.driver) 
        check_turqouise = item1_page.selected_clr1()
        assert check_turqouise == "T", "Turquoise color not found in first order of selected colors"
        print(green_color + "Passed: " + f"Turquoise color code '{check_turqouise}' in 1st order matches to selected color" + reset_color)

    def test_validate_usaf_royal(self):
        item1_page = ColorWheel(self.driver) 
        check_usaf_royal = item1_page.selected_clr2()
        assert check_usaf_royal == "AR", "Usaf Royal color not found in 2nd order of selected colors"
        print(green_color + "Passed: " + f"Usaf Royal color code '{check_usaf_royal}' in 2nd order matches to selected color" + reset_color)

    def test_validate_yellow(self):
        item1_page = ColorWheel(self.driver) 
        check_yellow = item1_page.selected_clr3()
        assert check_yellow == "Y", "Usaf Royal color not found in 3rd order of selected colors"
        print(green_color + "Passed: " + f"Usaf Royal color code '{check_yellow}'in 3rd order matches to selected color" + reset_color)
    
    def test_validate_brick_red(self):
        item1_page = ColorWheel(self.driver) 
        check_brick_red = item1_page.selected_clr4()
        assert check_brick_red == "BRR", "Brick Red color not found in 4th order of selected colors"
        print(green_color + "Passed: " + f"Brick Red color code '{check_brick_red}' in 4th order matches to selected color" + reset_color)
        
    def test_validate_natural(self):
        item1_page = ColorWheel(self.driver) 
        check_natural = item1_page.selected_clr5()
        assert check_natural == "MNT", "Natural color not found in 5th order of selected colors"
        print(green_color + "Passed: " + f"Natural color code '{check_natural}' in 5th order matches to selected color" + reset_color)


    def test_validate_heather_royal(self):
        item1_page = ColorWheel(self.driver) 
        check_heather_royal = item1_page.selected_clr6()
        assert check_heather_royal == "MHRB", "Heather Royal color not found in 6th order of selected colors"
        print(green_color + "Passed: " + f"Header Royal color code '{check_heather_royal}' in 6th order matches to selected color" + reset_color)
        time.sleep(3)
    
    def test_validate_loaded_items(self):
        item1_page = ColorWheel(self.driver) 
        is_invisble = item1_page.items_loaded()
        assert is_invisble, "the modal loading did not become invisible"
        print(green_color + f"Items successfully loaded" + reset_color)
        

        #clear selected colors
        select_color_wheel = item1_page.reselect_color_wheel()
        self.driver.execute_script("arguments[0].scrollIntoView();", select_color_wheel)
        select_color_wheel.click()

        #select color wheel and clear colors
        reselect_wheel = item1_page.clear_selected_colors()
        self.driver.execute_script("arguments[0].scrollIntoView();", reselect_wheel)
        reselect_wheel.click()

        time.sleep(2)
        item1_page.confirm_clear().click()

    
        


      

    




        




       

  

    

    
    
    
