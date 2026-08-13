from actions import informations , applications , browser

class NormalMode:

    def open_chrome(self):
        applications.open_chrome()

    def open_youtube(self):
        applications.open_youtube

    def take_screenshot(self):
        print("Taking screenshot")

    def open_vscode():
        applications.open_vscode()

    def today_weather():
        informations.weathernow()

    def timenow():
        informations.timenow()

    def open_github():
        browser.openGithub()

    def open_leetcode():
        browser.openLeetcode()

    def open_insta():
        browser.openInsta()

    def open_facebook():
        browser.openFacebook()

    def default(self, command):
        print(f"Normal Mode: I don't know: {command}")
