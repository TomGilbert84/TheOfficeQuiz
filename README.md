# The Office Quiz

A project which uses the [jxm/the_office_lines](https://huggingface.co/datasets/jxm/the_office_lines/blob/main/README.md) dataset to create a quiz based on the American version of The Office.

To run the quiz in the terminal, type `python officeTrivia.py`

To run the quiz in the front end, type `npm run app`. This will run the app here: http://127.0.0.1:5000.

To run the Playwright tests, type `npm run tests`.

The data for the Allure report will be created in the script above.

To generate the Allure report, type `npm run generate-allure`.

To open the report, type `npm run open-allure`.

The Allure report will also be published [here](https://tomgilbert84.github.io/TheOfficeQuiz/). 

Note: there is a slight time delay before the Allure report is updated on the link above.

If the token expires, do the following:

Solution:

Regenerate a new PAT from GitHub:
Go to GitHub Developer Settings.
Click Generate new token (classic) and give it the required permissions.
Save the token securely (you won't see it again).
Update the GitHub Actions secret with the new PAT:
In your GitHub repository, go to Settings > Secrets and variables > Actions.
Add or update a secret named GH_TOKEN or similar with the new PAT.

[![Playwright Tests](https://github.com/TomGilbert84/TheOfficeQuiz/actions/workflows/playwright.yml/badge.svg)](https://tomgilbert84.github.io/TheOfficeQuiz/)

# ToDo 

Try and add some tests which use mock data to check that the correct functionality occurs when a correct/incorrect answer is entered.

![The Office!](/the-office-handshake.jpg "Michael handshake")
