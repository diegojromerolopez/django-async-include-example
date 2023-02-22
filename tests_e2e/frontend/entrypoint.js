import expect from 'expect-puppeteer'

describe('Django Async Include', () => {
  beforeAll(async () => {
    await page.goto('https://backend:8000');
  });

  it('Page h1 title', async () => {
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
    await page.goto('https://backend:8000')

    await expect(page).toSelect('h1', 'Shop lists')
  });
});