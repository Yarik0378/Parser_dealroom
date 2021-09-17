from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
import csv
import re

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 3)

email = 'larise3094@activesniper.com'
password = 'BusinessEmail'


def logination():
    driver.get(
        'https://app.dealroom.co/companies.startups/f/company_status/not_acquired/income_streams/anyof_subscription/revenues/anyof_saas/slug_locations/anyof_europe?row_index=52')
    time.sleep(3)
    driver.find_element_by_css_selector("button[data-testid='nav-button-login']").click()
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
    driver.find_element_by_css_selector("input[name='email']").send_keys(email)
    driver.find_element_by_css_selector("input[name='password']").send_keys(password)
    driver.find_element_by_css_selector("button[data-testid='login-button-submit']").click()
    time.sleep(5)


def get_data():
    x = 0
    for i in range(0, 500):

        driver.get(
            f'https://app.dealroom.co/companies.startups/f/company_status/not_acquired/income_streams/anyof_subscription/revenues/anyof_saas/slug_locations/anyof_europe?row_index={x}')
        time.sleep(7)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        table_list = soup.select('div.table-list-item')
        # next_page = soup.find('a', id='next-page').get('href')
        # print(next_page)
        for table in table_list:
            try:
                name = table.find('div', class_='table-list-columns-fixed hbox').select_one(
                    'a[data-testid="internal"]').text
            except:
                name = ' '
            try:
                sub_name = table.find('div', class_='type-element type-element--p6 entity-name__tagline no-wrap').text
            except:
                sub_name = ' '
            try:
                market = table.find('div', class_='markets-column').text
            except:
                market = ' '
            try:
                type_ = table.find('div', class_='table-list-column type has-dropdown').text
            except:
                type_ = ' '
            try:
                growth_signal = table.find('div', class_='growth-line-chart__hover-content vbox').text.replace('%',
                                                                                                               '% ')
            except:
                growth_signal = ' '
            try:
                launch_date = table.find('div', class_='table-list-column launchDate has-dropdown').text
            except:
                launch_date = ' '
            try:
                valuation = table.find('div', class_='table-list-column valuation has-dropdown').text
            except:
                valuation = ' '
            try:
                funding = table.find('div', class_='table-list-column totalFunding has-dropdown').text
            except:
                funding = ' '
            try:
                location = table.find('div', class_='table-list-column hqLocations has-dropdown').text
            except:
                location = ' '
            try:
                last_round = table.find('div', class_='table-list-column lastFunding has-dropdown').text
            except:
                last_round = ' '
            try:
                no_of_job_openings = table.find('div', class_='table-list-column totalJobsAvailable has-dropdown').text
            except:
                no_of_job_openings = ' '
            try:
                job_opening = table.find('div', class_='table-list-column jobRoles has-dropdown').text
            except:
                job_opening = ' '
            try:
                tech_sta = table.find(
                    'div', class_='table-list-column techStacks has-dropdown').find('ul').find_all('li')
                tech_stack = ''
                for li in tech_sta:
                    tech_stack += str(li.text) + ', '
                    tech_stack = tech_stack.replace('more,', 'more')
            except:
                tech_stack = ' '
            try:
                revenue = table.find('div', class_='table-list-column revenue').text
            except:
                revenue = ' '
            try:
                status = table.find('div', class_='table-list-column companyStatus').text
            except:
                status = ' '
            try:
                growth_stage = table.find('div', class_='table-list-column growthStage').text
            except:
                growth_stage = ' '
            try:
                monthly_web_visit_ = table.find_all('div', class_='growth-line-chart__hover-content vbox')[1].find_all('span')
                monthly_web_visit = ''
                for span in monthly_web_visit_:
                    monthly_web_visit += str(span.text) + ' '
            except:
                monthly_web_visit = ' '
            try:
                monthly_web_visit_2 = table.find('div', class_='table-list-column companyWebVisits has-dropdown lineChartColumn').find('span', class_='growth-line-chart__value vbox fadein').text
            except:
                monthly_web_visit_2 = ' '
            try:
                alumni_who_became_founders = table.find('div', class_='table-list-column pastFoundersRaised10m').text
            except:
                alumni_who_became_founders = ' '
            try:
                web_visits_change_in_rank = table.find('div',
                                                       class_='table-list-column companyWebVisitsRank has-dropdown deltaColumn').text
            except:
                web_visits_change_in_rank = ' '
            try:
                employees_change_in_rank = table.find('div',
                                                      class_='table-list-column companyEmployeesRank has-dropdown deltaColumn').text
            except:
                employees_change_in_rank = ' '
            try:
                share_price = table.find('div', class_='table-list-column tradingMultipleSharePrice').text
            except:
                share_price = ' '
            try:
                equity_value = table.find('div', class_='table-list-column tradingMultipleMarketEquity').text
            except:
                equity_value = ' '
            try:
                firm_value = table.find('div', class_='table-list-column tradingMultipleMarketFirm').text
            except:
                firm_value = ' '
            inf = {
                'name': name,
                'sub_name': sub_name,
                'market': market,
                'type_': type_,
                'growth_signal': growth_signal,
                'launch_date': launch_date,
                'valuation': valuation,
                'funding': funding,
                'location': location,
                'last_round': last_round,
                'no_of_job_openings': no_of_job_openings,
                'job_opening': job_opening,
                'tech_stack': tech_stack,
                'revenue':revenue,
                'status': status,
                'growth_stage': growth_stage,
                'monthly_web_visit': monthly_web_visit,
                'monthly_web_visit_2': monthly_web_visit_2,
                'alumni_who_became_founders': alumni_who_became_founders,
                'web_visits_change_in_rank': web_visits_change_in_rank,
                'employees_change_in_rank': employees_change_in_rank,
                'share_price': share_price,
                'equity_value': equity_value,
                'firm_value': firm_value
            }
            write_csv(inf)
        x += 20
        if x > 8800:
            break


def write_csv(inf):
    with open('NEW_DATA.csv', 'a', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow((
            inf['name'],
            inf['sub_name'],
            inf['market'],
            inf['type_'],
            inf['growth_signal'],
            inf['launch_date'],
            inf['valuation'],
            inf['funding'],
            inf['location'],
            inf['last_round'],
            inf['no_of_job_openings'],
            inf['job_opening'],
            inf['tech_stack'],
            inf['revenue'],
            inf['status'],
            inf['growth_stage'],
            inf['monthly_web_visit'],
            inf['monthly_web_visit_2'],
            inf['alumni_who_became_founders'],
            inf['web_visits_change_in_rank'],
            inf['employees_change_in_rank'],
            inf['share_price'],
            inf['equity_value'],
            inf['firm_value']
        ))


def main():
    logination()
    get_data()


if __name__ == '__main__':
    main()
