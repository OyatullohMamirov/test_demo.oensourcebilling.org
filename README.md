OpenSourceBilling Selenium Test
Overview
Automated tests for OpenSourceBilling demo application using Selenium WebDriver with Python.
Setup

Install requirements:

Copypip install selenium webdriver-manager html-testRunner

Project structure:

CopyProject/
├── config.py                 # WebDriver configuration
├── test_login.py             # Unit test script
├── simple_login.py           # Basic login script
├── Locators/
│   └── locators.py           # Element locators
├── Pages/
│   ├── loginPage.py          # Login page object
│   └── homePage.py           # Dashboard page object
└── Reports/                  # HTML reports directory
Running Tests
Using unittest:
Copypython test_login.py
Using simple script:
Copypython simple_login.py
Test Cases

Invalid Login: Tests error message with wrong credentials
Valid Login: Tests successful login, dashboard redirect, and logout

Troubleshooting

Element not found: Check locators
Browser crashes: Ensure ChromeDriver matches Chrome version
Timeouts: Increase wait times
Last edited just now
