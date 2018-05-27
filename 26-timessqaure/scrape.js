const puppeteer = require('puppeteer')
const fs = require('fs')

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {

    //Start Url
    let start_url = 'http://www.timessquare.com.hk/eng/shopping_list.php'
    //Browser setup
    const browser = await puppeteer.launch({headless:false});
    const page = await browser.newPage();
    //Go to Page
    await page.goto(start_url)
    await page.waitForSelector('#content_shoplist > table')

    let table = await page.evaluate(() => {
        return document.querySelector('#content_shoplist > table').outerHTML
    })
    fs.appendFileSync('table.html',table)
    await browser.close();

})();