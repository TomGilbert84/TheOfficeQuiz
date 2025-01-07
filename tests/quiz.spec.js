// @ts-check
const { test, expect } = require('@playwright/test');

let page;

test.beforeAll(async ({ browser }) => {
  page = await browser.newPage();
  await page.goto('http://127.0.0.1:5000');
});

test.afterAll(async () => {
  await page.close();
});

test('should display the correct title in the browser', async () => {
  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(/The Office Quiz/);
});

test('should display a question and 4 answer options', async () => {
  // Verify that a question is displayed
  const question = await page.getByTestId('question');
  expect(question).toBeTruthy();

  // Verify that there are 4 answer options
  const answerOptions = await page.$$eval('input[type="radio"][name="answer"]', options => options.length);
  expect(answerOptions).toEqual(4);
});

test('should have a submit button with correct value', async () => {
  // Expect page to have a submit button.
  const submitButton = await page.getByRole('button', { name: 'Submit' });
  expect(submitButton).toBeTruthy();

  // Find the submit button value
  const submitButtonValue = await submitButton.getAttribute('value');

  // Assert that the submit button value includes the word "Submit"
  expect(submitButtonValue).toContain('Submit');
});
