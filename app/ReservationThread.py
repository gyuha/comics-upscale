from PySide6.QtCore import QThread
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import MainWindow


class ReservationThread(QThread):
    def __init__(self, parent: MainWindow, retry_count: int = 5):
        super().__init__(parent)
        self.parent = parent
        self.retry_count = retry_count
        self.config = self.parent.config
    
    def run(self):
        self.driver = self.parent.driver
        self.retry_count = 5
        self.check_reserve_date()
    
    def retry(self):
        self.parent.log("[{0}] 예약 할 시간이 없습니다. 다시 시도 합니다.".format(self.retry_count))
        self.retry_count -= 1
        self.check_reserve_date()

    
    def check_reserve_date(self):
        self.parent.log("예약 조회 시작")
        self.driver.get('https://www.namyeoju.co.kr/Reservation/Reservation.aspx')
        # self.driver.get("file://C:\\Users\gyuha\\Desktop\\n01.html")
        self.driver.implicitly_wait(5)

        days = self.driver.find_elements(By.CLASS_NAME, 'reserved')
        if len(days) == 0 and self.retry_count > 0:
            self.retry();
            return
        
        if len(days) == 0:
            self.parent.log("예약을 종료 합니다.")
            self.parent.stop()
            return;
        
        target_date = self.config.setting["reserve_date"].strip()
        day = None
        for d in days:
            href = d.get_attribute("href")
            if target_date in href:
                print('📢[ReservationThread.py:53]: ', d.text)
                day = d
                break
        
        if day == None:
            self.retry()
            return
        
        day.click()
        



        