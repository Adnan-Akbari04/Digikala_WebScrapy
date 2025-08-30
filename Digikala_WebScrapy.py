import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests
import numpy as np
import pandas as pd


url = 'https://www.digikala.com/'
driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()
time.sleep(5)

button1 = driver.find_element(By.XPATH, '''//*[@id="base_layout_desktop_fixed_header"]/header/nav/div[1]/div[1]/div[1]/div/span''')
button1.click()
time.sleep(5)

button2 = driver.find_element(By.XPATH, '''//*[@id="base_layout_desktop_fixed_header"]/header/nav/div[1]/div[1]/div[1]/div/div/div/div[1]/a[3]''')
actions = ActionChains(driver)
actions.move_to_element(button2).perform()
time.sleep(5)

# TODO: To Get Data Of All Asus, Lenovo And Macbook Laptops, Uncomment Line 27 And Comment Line 28
# desired_laptop_list = [3,4,5,6,8,9,10,11,13,14,15,16,18
desired_laptop_list = [3]
desired_laptop_links = []
for item in desired_laptop_list:
    desired_laptop_xpath = f'''//*[@id="base_layout_desktop_fixed_header"]/header/nav/div[1]/div[1]/div[1]/div/div/div/div[2]/div[3]/div/ul/div[1]/a[{item}]'''
                           # ''' //*[@id="base_layout_desktop_fixed_header"]/header/nav/div[1]/div[1]/div[1]/div/div/div/div[2]/div[3]/div/ul/div[1]/a[2]'''
    try:
        laptop_link = driver.find_element(By.XPATH, desired_laptop_xpath).get_attribute('href')
        desired_laptop_links.append(laptop_link)


    except Exception as e:
        desired_laptop_links.append(np.nan)
        print(e)

# To Get Details Out Of The Links
for link in desired_laptop_links:
    driver.execute_script(f"window.open('{link}')")
    driver.switch_to.window(driver.window_handles[-1])
    file_name = link.split('/')[-2]
    time.sleep(5)

    scroll_height = []
    while True:
        driver.execute_script("window.scrollBy(0,800)")
        time.sleep(5)
        current_height = driver.execute_script("return document.body.scrollHeight")
        scroll_height.append(current_height)
        if scroll_height.count(current_height) > 5:
            break

    container_div = driver.find_element(By.XPATH, '''//*[@id="ProductListPagesWrapper"]/section[1]/div[2]''')
    container_div_items = container_div.find_elements(By.CLASS_NAME, 'product-list_ProductList__item__LiiNI')

    ID_list, title_list, price_list, rating_list, off_list, price_before_off_list, details_link_list = [], [], [], [], [], [], []
    cpu_list, gpu_list, ram_list = [], [], []
    if len(container_div_items) > 0:

        # TODO: To Get Data Of All Laptops On Web Page Uncomment Line 66 And Comment Line 67. Line 67 Gets Data Of Just The First 25 Laptops!
        # for i in range(1, len(container_div_items)+1):
        for i in range(1, 26):

            ID_list.append(i)
            box_item_xpath = f'''//*[@id="ProductListPagesWrapper"]/section[1]/div[2]/div[{i}]'''
            box_item = driver.find_element(By.XPATH, box_item_xpath)

            # Title
            try:
                title = box_item.find_element(By.TAG_NAME, 'h3').text
                title_list.append(title)
            except:
                title_list.append(np.nan)

            # Price
            try:
                price = box_item.find_element(By.CSS_SELECTOR, '''[data-testid="price-final"]''').text
                price_list.append(int(price.replace(',', '')))
            except:
                price_list.append(np.nan)

            # Rating
            try:
                rating = box_item.find_element(By.XPATH, f'''{box_item_xpath}/a/div/article/div[2]/div[2]/div[3]/div[2]/p''').text
                rating_list.append(float(rating))
            except:
                rating_list.append(np.nan)

            # Off
            try:
                off = box_item.find_element(By.CSS_SELECTOR, '''[data-testid="price-discount-percent"]''').text
                off_list.append(off)
            except:
                off_list.append(np.nan)

            #  Price Before Off
            try:
                price_before_off = box_item.find_element(By.CSS_SELECTOR, '''[data-testid="price-no-discount"]''').text
                price_before_off_list.append(int(price_before_off.replace(',', '')))
            except:
                price_before_off_list.append(np.nan)

            # Picture
            try:
                picture_link = box_item.find_element(By.XPATH, f'''{box_item_xpath}/a/div/article/div[2]/div[1]/div/div/div[1]/div/picture/img''').get_attribute('src')
                response = requests.get(picture_link).content
                with open(f'photo/{i}.png', 'wb') as f:
                    f.write(response)

            except:
                pass

            # Details
            try:
                details_link = box_item.find_element(By.XPATH, f'''{box_item_xpath}/a''').get_attribute('href')
                # details_link_list.append(details_link)
                details_link_list.append(details_link if details_link else i)

                driver.execute_script(f'window.open("{details_link})")')
                driver.switch_to.window(driver.window_handles[2])
                time.sleep(5)
                features_button = driver.find_element(By.XPATH,
                                                      '''//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/button''')
                features_button.click()
                time.sleep(3)

                flag = True
                if flag:
                    try:
                        features_ellipses_xpath = '''//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[6]/div[2]/div[1]/section'''
                        features_ellipses = driver.find_element(By.XPATH, f'{features_ellipses_xpath}/span')
                        features_ellipses.click()
                        time.sleep(5)

                        cpu = driver.find_element(By.XPATH,
                                                  '''//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[6]/div[2]/div[1]/section/div[3]/div/div[1]/div''').find_element(
                            By.TAG_NAME, 'p').text
                        cpu_list.append(cpu)

                        gpu = driver.find_element(By.XPATH,
                                                  '''//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[6]/div[2]/div[1]/section/div[4]/div/div[1]/div''').find_element(
                            By.TAG_NAME, 'p').text
                        gpu_list.append(gpu)

                        ram = driver.find_element(By.XPATH,
                                                  '''//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[6]/div[2]/div[1]/section/div[5]/div/div[1]/div''').find_element(
                            By.TAG_NAME, 'p').text
                        ram_list.append(ram)
                        flag = False
                        driver.close()
                        driver.switch_to.window(driver.window_handles[1])
                    except:
                        pass

                if flag:
                    try:
                        features_ellipses_xpath = '''//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[7]/div[2]/div[1]/section'''
                        features_ellipses = driver.find_element(By.XPATH, f'{features_ellipses_xpath}/span')
                        features_ellipses.click()
                        time.sleep(5)

                        cpu = driver.find_element(By.XPATH,
                                                  '''//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[7]/div[2]/div[1]/section/div[3]/div/div[1]/div''').find_element(
                            By.TAG_NAME, 'p').text
                        cpu_list.append(cpu)

                        gpu = driver.find_element(By.XPATH,
                                                  '''//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[7]/div[2]/div[1]/section/div[4]/div/div[1]/div''').find_element(
                            By.TAG_NAME, 'p').text
                        gpu_list.append(gpu)

                        ram = driver.find_element(By.XPATH,
                                                  '''//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[7]/div[2]/div[1]/section/div[5]/div/div[1]/div''').find_element(
                            By.TAG_NAME, 'p').text
                        ram_list.append(ram)
                        flag = False
                        driver.close()
                        driver.switch_to.window(driver.window_handles[1])
                    except:
                        pass

                if flag:
                    try:
                        features_ellipses_xpath = '''//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[8]/div[2]/div[1]/section'''
                        features_ellipses = driver.find_element(By.XPATH, f'{features_ellipses_xpath}/span')
                        features_ellipses.click()
                        time.sleep(5)

                        cpu = driver.find_element(By.XPATH,
                                                  '''//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[8]/div[2]/div[1]/section/div[3]/div/div[1]/div''').find_element(
                            By.TAG_NAME, 'p').text
                        cpu_list.append(cpu)

                        gpu = driver.find_element(By.XPATH,
                                                  '''//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[8]/div[2]/div[1]/section/div[4]/div/div[1]/div''').find_element(
                            By.TAG_NAME, 'p').text
                        gpu_list.append(gpu)

                        ram = driver.find_element(By.XPATH,
                                                  '''//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[8]/div[2]/div[1]/section/div[5]/div/div[1]/div''').find_element(
                            By.TAG_NAME, 'p').text
                        ram_list.append(ram)
                        flag = False
                        driver.close()
                        driver.switch_to.window(driver.window_handles[1])
                    except:
                        pass
                if flag:
                    driver.close()
                    driver.switch_to.window(driver.window_handles[1])
            except:
                cpu_list.append(np.nan)
                gpu_list.append(np.nan)
                ram_list.append(np.nan)

    print("List lengths:")
    print(f"ID: {len(ID_list)}")
    print(f"Title: {len(title_list)}")
    print(f"Price: {len(price_list)}")
    print(f"Rating: {len(rating_list)}")
    print(f"Off: {len(off_list)}")
    print(f"PriceBeforeOff: {len(price_before_off_list)}")
    print(f"Cpu: {len(cpu_list)}")
    print(f"Gpu: {len(gpu_list)}")
    print(f"RAM: {len(ram_list)}")
    print(f"DetailsLink: {len(details_link_list)}")

    digikala_result_dict ={
        'ID': ID_list,
        'Title': title_list,
        'Price': price_list,
        'Rating': rating_list,
        'Off': off_list,
        'PriceBeforeOff': price_before_off_list,
        'Cpu': cpu_list,
        'Gpu': gpu_list,
        'RAM': ram_list,
        'DetailsLink': details_link_list
    }

    digikala_result_df = pd.DataFrame(digikala_result_dict)
    digikala_result_df.to_csv(f'{file_name}.csv', encoding='utf-8', index=False,
                              columns=['ID', 'Title', 'Price', 'Rating', 'Off', 'PriceBeforeOff', 'Cpu', 'Gpu', 'RAM', 'DetailsLink'])

    driver.close()
    driver.switch_to.window(driver.window_handles[-1])