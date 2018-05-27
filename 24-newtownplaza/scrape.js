const puppeteer = require('puppeteer')
const fs = require('fs')

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {

    //Start Url
    let start_url = 'http://www.newtownplaza.com.hk/shopping'
    //Browser setup
    const browser = await puppeteer.launch({headless:false});
    const page = await browser.newPage();
    //Go to Page
    await page.goto(start_url)
    await page.waitForSelector('.shop-list__list-item__info')
    await sleep(10)

    let items = await page.evaluate(() =>{
        let  items = []
        let divs = [...document.querySelectorAll('.shop-list__list-item__info')]
        for (let div of divs) {
            let item ={}
            item['name'] = div.querySelector('.shop-list__list-item__name').innerText
            item['location'] = div.querySelector('.shop-list__list-item__location').innerText
            item['open_time'] = div.querySelector('.shop-list__list-item__time').innerText
            item['tele'] = div.querySelector('.shop-list__list-item__tel').innerText
            items.push(item)
        }
        return items
    })

    fs.appendFileSync('newtownplaza.json',JSON.stringify(items))
    await browser.close();

})();