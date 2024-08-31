from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.baseclass import BaseClass
from Pages.bulls_oh_sleeve_compression_top import Wrestling
from Assets.credentials import green_color, reset_color, blue_color, email_qx7, password_qx7
from Assets.styles import sleeve_compression_top, style
import random
import time


class Test_first_test(BaseClass):

    def test_click_wrestling(self):
        print(blue_color + f"\nNow Validating '{sleeve_compression_top}' where style is {style}\n" + reset_color)
        item2 = Wrestling(self.driver)
        click_wrestling = item2.click_wrestling_item()
        self.driver.execute_script("arguments[0].scrollIntoView();", click_wrestling)
        click_wrestling.click()

    def test_validate_wrestling_sport(self):
        item2 = Wrestling(self.driver)
        validate_wrestling = item2.check_wrestling_text().text.lower()
        print(green_color + f"Current page is: {validate_wrestling}" + reset_color)
        assert validate_wrestling == "wrestling", "You are not in wrestling page"
        time.sleep(3)
        item2.close_tips().click()

    def test_search_apparel(self):
        item2 = Wrestling(self.driver)
        input_apparel_details = item2.text_search()
        time.sleep(2)
        input_apparel_details.send_keys(sleeve_compression_top)
        time.sleep(2)
        assert input_apparel_details.text in sleeve_compression_top, f"Your search did not reflected on textbox '{sleeve_compression_top}'"
        print(green_color + f"'{sleeve_compression_top}' reflected on search text field" + reset_color)

    def test_gender_field(self):
        item2 = Wrestling(self.driver)
        select_field = item2.select_gender_field()
        self.driver.execute_script("arguments[0].scrollIntoView();", select_field)
        select_field.click()

    def test_male_field(self):
        item2 = Wrestling(self.driver)
        select_male = item2.select_male_gender()
        self.driver.execute_script("arguments[0].scrollIntoView();", select_male)
        select_male.click()

    def test_select_male_field(self):
        item2 = Wrestling(self.driver)
        select_male = item2.select_male_gender()
        self.driver.execute_script("arguments[0].scrollIntoView();", select_male)
        select_male.click()

    def test_bulls_existence(self):
        item2 = Wrestling(self.driver)
        style_text = item2.verify_style().text
        assert style_text in style, f"Style '{style}' doesn't exist"
        print(green_color + f"style '{style}' exist" + reset_color)

    def test_compare_info(self):
        item2 = Wrestling(self.driver)

        card_info = {
            "gender": item2.verify_gender().text[:3].lower(),
            "title": item2.verify_title().text.lower(),
            "adult_price": item2.verify_adult_price().text.split()[1].lower(),
            "style": item2.verify_style().text.lower(),
            "youth_price": item2.verify_youth_price().text.split()[1].lower(),
            "brand_item_code": item2.verify_brand_item_code().text.lower(),
        }

        time.sleep(2)
        click_i = item2.click_i_btn()
        bulls_loc = item2.card_loc()
        self.driver.execute_script("arguments[0].scrollIntoView();", bulls_loc)
        click_i.click()
        time.sleep(2)

        modal_info = {
            "gender": item2.verify_product_gender().text[:3].lower(),
            "title": item2.verify_product_title().text.lower(),
            "adult_price": item2.verify_product_adult_price().text.lower(),
            "style": item2.verify_product_style().text.lower(),
            "youth_price": item2.verify_product_youth_price().text.lower(),
            "brand_item_code": item2.verify_product_brand_item_code().text.lower(),
        }

        print("Card Info:", card_info, '\n')
        print("Modal Info:", modal_info, '\n')

        assert card_info == modal_info, (
            f"Mismatch found:\n"
            f"Card Info: {card_info}\n"
            f"Modal Info: {modal_info}"
        )
        print(green_color + "Card info and Modal info are matched" + reset_color)
        time.sleep(3)

    def test_verify_product_line(self):
        item2 = Wrestling(self.driver)
        product_line = item2.verify_product_line().text.lower()
        assert product_line == "quickturn", "product line doesn't exist"
        print(green_color + f"product line '{product_line}' existing" + reset_color)
        time.sleep(2)

    def test_select_sizing_chart(self):
        item2 = Wrestling(self.driver)
        original_window = self.driver.current_window_handle

        click_sizing_chart = item2.fetch_sizing_chart()
        self.driver.execute_script("arguments[0].scrollIntoView();", click_sizing_chart)
        click_sizing_chart.click()

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        windowLists = self.driver.window_handles

        for handle in windowLists:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break

        WebDriverWait(self.driver, 10).until(EC.url_to_be(
            "https://s3.us-west-2.amazonaws.com/qx7/uploaded_files/master_size_charts/20230502200503/g03BkGoIOh.pdf"))

        assert self.driver.current_url == "https://s3.us-west-2.amazonaws.com/qx7/uploaded_files/master_size_charts/20230502200503/g03BkGoIOh.pdf", "PDF URL not matched"
        print(green_color + "Passed: " + f"PDF URL matched: {self.driver.current_url}" + reset_color)
        time.sleep(3)
        self.driver.close()
        self.driver.switch_to.window(original_window)

    def test_access_inseam_chart(self):
        item2 = Wrestling(self.driver)
        click_inseam_chart = item2.fetch_inseam_chart()
        self.driver.execute_script("arguments[0].scrollIntoView();", click_inseam_chart)
        click_inseam_chart.click()
        time.sleep(2)
        item2.fetch_inseam_close().click()
        time.sleep(2)

    def test_how_to_measure(self):
        item2 = Wrestling(self.driver)
        original_window = self.driver.current_window_handle

        item2.fetch_measure_guide().click()

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        # Switch to the new window
        windowLists = self.driver.window_handles
        for handle in windowLists:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break

        WebDriverWait(self.driver, 10).until(EC.url_to_be(
            "https://s3.us-west-2.amazonaws.com/qx7/uploaded_files/master_resource_center/20230508170510/qgGX3pU4Ku.pdf"))

        assert self.driver.current_url == "https://s3.us-west-2.amazonaws.com/qx7/uploaded_files/master_resource_center/20230508170510/qgGX3pU4Ku.pdf", "Measure guide URL not matched"
        print(green_color + "Passed: " + f"Measure Guide URL matched: {self.driver.current_url}" + reset_color)

        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(original_window)

    def test_compare_price(self):
        time.sleep(2)
        item2 = Wrestling(self.driver)
        original_window = self.driver.current_window_handle

        brand_item_code = item2.verify_product_brand_item_code().text
        adult_price = item2.verify_product_adult_price().text.lower().replace('$', '')
        youth_price = item2.verify_product_youth_price().text.lower().replace('$', '')

        item2.fetch_measure_guide().click()

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        windowLists = self.driver.window_handles
        for handle in windowLists:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                self.driver.get("https://staging-qx7.prolook.com/login")
                break

        time.sleep(4)
        item2.email_bcknd().send_keys(email_qx7)
        item2.password_backnd().send_keys(password_qx7 + Keys.RETURN)
        time.sleep(3)

        action = ActionChains(self.driver)
        action.move_to_element(item2.hover_finance_tab()).perform()
        time.sleep(2)
        action.move_to_element(item2.click_price_items()).click().perform()

        time.sleep(2)

        Select(item2.brand_select_price_items()).select_by_visible_text("PROLOOK")
        time.sleep(2)
        item2.filter_pl_upgrade().click()
        item2.search_product().send_keys(brand_item_code)
        time.sleep(1)

        count_youth = sum(1 for item in item2.youth_prices() if item.text == youth_price)
        count_adult = sum(1 for item in item2.adult_prices() if item.text == adult_price)

        print(f"youth:{youth_price}, adult:{adult_price}")

        assert count_youth == 5 and count_adult == 9, "Either of the youth/adult have different price"
        print(green_color + "youth/adult price count is accurate" + reset_color)

        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(original_window)


    def test_go_to_builder(self):
        print(blue_color + "\nDirecting to builder page\n" + reset_color)
        item2 = Wrestling(self.driver)
        item2.close_modal().click()

        time.sleep(2)
        click_on_item = item2.click_item()
        self.driver.execute_script("arguments[0].scrollIntoView();", click_on_item)
        click_on_item.click()

        first_item_visibility = item2.load_first_item()

        assert first_item_visibility, "First item of in the builder did not load"
        print(green_color + "Apparel has been loaded" + reset_color)

        time.sleep(2)


    def test_validate_duplicate_info(self):
        item2 = Wrestling(self.driver)
        time.sleep(2)
        item2.select_builder_modal().click()
        time.sleep(1)
        product_details = item2.move_to_text_list()
        self.driver.execute_script("arguments[0].scrollIntoView();", product_details)

        product_info = item2.production_information()
        product_info_texts = [items.text for items in product_info]

        for items in product_info_texts:
            print(green_color + items + reset_color)

        self.check_duplicates(product_info_texts)

    def test_select_fabric_drpdwn(self):
        item2 = Wrestling(self.driver)
        item2.fabric_dropdown().click()
        time.sleep(2)
        item2.zoom_fabric().click()
        print(green_color + "Zoom fabric dropdown has been selected" + reset_color)
        time.sleep(2)
        item2.close_modal_fabric().click()
        print(green_color + "Close fabric dropdown has been selected" + reset_color)
        assert item2.load_fabric_image(), "Fabric image not loaded"
        print(green_color + "Fabric image loaded" + reset_color)


    def test_colors_tab(self):
        item2 = Wrestling(self.driver)
        time.sleep(1)
        self.bottom_thumbnails()

        self.scroll_into_view(item2.colors_tab())
        item2.colors_tab().click()

        time.sleep(2)
        select_first_color = item2.click_first_color()

        for items in select_first_color:
            items.click()
            time.sleep(0.3)
        time.sleep(1)
        self.bottom_thumbnails()
        time.sleep(2)
        item2.click_picker().click()
        time.sleep(1)
        item2.kelly_green().click()
        item2.black().click()
        item2.yellow().click()
        item2.click_save().click()

        time.sleep(2)

        select_body_color = item2.click_body_colors()
        select_sleeve_color = item2.click_sleeves_colors()
        select_collar_color = item2.click_collar_colors()
        select_front_graphic_color = item2.click_front_graphic_color()
        select_sleeve_stripe1_color = item2.click_sleeve_stripe_1_color()
        select_sleeve_stripe2_color = item2.click_sleeve_stripe_2_color()
        select_sleeve_end = item2.click_sleeve_end()

        for items1 in select_body_color:
            items1.click()
            time.sleep(0.2)

        if select_body_color:
            random_choice = random.choice(select_body_color)
            random_choice.click()

        #sleeve color
        for items3 in select_sleeve_color:
            items3.click()
            time.sleep(0.2)

        if select_sleeve_color:
            random_choice = random.choice(select_sleeve_color)
            random_choice.click()

        # colar color
        for items4 in select_collar_color:
            items4.click()
            time.sleep(0.2)

        if select_collar_color:
            random_choice = random.choice(select_collar_color)
            random_choice.click()

        # front graphic color
        for items5 in select_front_graphic_color:
            items5.click()
            time.sleep(0.2)

        if select_front_graphic_color:
            random_choice = random.choice(select_front_graphic_color)
            random_choice.click()

        # sleeve stripe 1 color
        for items6 in select_sleeve_stripe1_color:
            items6.click()
            time.sleep(0.2)

        if select_sleeve_stripe1_color:
            random_choice = random.choice(select_sleeve_stripe1_color)
            random_choice.click()

        # sleeve stripe 2 color
        for items7 in select_sleeve_stripe2_color:
            items7.click()
            time.sleep(0.2)

        if select_sleeve_stripe2_color:
            random_choice = random.choice(select_sleeve_stripe2_color)
            random_choice.click()


        # sleeve end color
        for items8 in select_sleeve_end:
            items8.click()
            time.sleep(0.2)

        if select_sleeve_end:
            random_choice = random.choice(select_sleeve_end)
            random_choice.click()

            time.sleep(3)

        time.sleep(1)
        self.bottom_thumbnails()

        time.sleep(2)
        brand_logo_drpdwn = item2.click_brand_logo_drpdwn()
        self.driver.execute_script("arguments[0].scrollIntoView();", brand_logo_drpdwn)
        brand_logo_drpdwn.click()

        time.sleep(1)

        brand_logo_loc = item2.click_brand_logo_loc()

        for index in range(len(brand_logo_loc.options)):
            brand_logo_loc.select_by_index(index)
            time.sleep(0.5)

        time.sleep(2)

        brand_logo_col = item2.click_brand_logo_color()

        # brand logo color
        for items9 in brand_logo_col:
            items9.click()
            time.sleep(0.2)

        if brand_logo_col:
            random_choice = random.choice(brand_logo_col)
            random_choice.click()

        time.sleep(2)

    def test_pattern_tab(self):
        item2 = Wrestling(self.driver)
        item2.click_pattern_tab().click()
        time.sleep(2)
        item2.click_turn_on().click()
        time.sleep(2)
        item2.select_arrow_camo().click()
        time.sleep(3)

#--------------------------------------------------------------------

    def check_duplicates(self, items, substring_length=5):

        item2 = Wrestling(self.driver)
        items = [item.strip().lower() for item in items if item.strip()]

        seen_substrings = set()
        duplicates = []

        for item in items:
            substring = item[:substring_length]
            if substring in seen_substrings:
                duplicates.append(item)
            else:
                seen_substrings.add(substring)

        print(items)
        assert not duplicates, f"Duplicates found: {duplicates}"
        print(green_color + "\nNo Duplicates Found in Product Info" + reset_color)
        item2.select_builder_modal().click()
        time.sleep(2)


    def bottom_thumbnails(self):
        item2 = Wrestling(self.driver)
        self.scroll_into_view(item2.second_image())
        item2.second_image().click()
        time.sleep(0.8)

        self.scroll_into_view(item2.third_image())
        item2.third_image().click()
        time.sleep(0.8)

        self.scroll_into_view(item2.fourth_image())
        item2.fourth_image().click()
        time.sleep(0.8)

        self.scroll_into_view(item2.first_image())
        item2.first_image().click()

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)



















