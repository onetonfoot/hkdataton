
const puppeteer = require('puppeteer')
const fs = require('fs')

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


async function scrape_resturant(page) {

    let item = page.evaluate(() => {
        let item = {}
        //Address
        item['address'] = document.querySelector('.address-info-section .content').innerText
        //Telephone
        item['tele'] = document.querySelector('.telephone-section .content')
        //Opening Hours
        item['opening_hours'] = document.querySelector('.opening-hours-time .current').innerText
        let taste_scores = [...document.querySelectorAll('.header-score-details-right-item')]
        for (score of taste_scores) {
            let divs = document.querySelectorAll('div')
            item[divs[0].innerText] = item[divs[1].innerText]
        }
        return item
    })
    await page.close()
    return item
}


(async () => {

    //Start Url
    let start_url = 'https://www.openrice.com/en/hongkong/chart/best-rating'
    //Browser setup
    const browser = await puppeteer.launch({headless:false});
    const page = await browser.newPage();
    //Go to Page
    await page.goto(start_url)
    await page.waitForSelector('.chart-listing li')

    let [items,hrefs] = await page.evaluate(() => {
        let resturant_cards = [...document.querySelectorAll('.chart-listing li')]
        let items = []
        let hrefs = []
        for (card of resturant_cards) {
            let item = {}
            item['rank'] = card.querySelector('.chart-detail-rank').innerText
            item['name'] = card.querySelector('.chart-poi-name').innerText
            let ratings = card.querySelectorAll('.rating-number')
            item['likes'] = ratings[0].innerText
            item['dislikes'] = ratings[1].innerText
            item['bookmarks'] =  card.querySelector('.js-bookmark-count').innerText
            item['movement'] = card.querySelector('.chart-detail-rank + div').className
            items.push(item)
            hrefs.push(card.querySelector('.chart-poi-name').href)
            }
        return [items,hrefs]
    })

    //Buggy need to fix!
    // let page_items = []
    // for (href of hrefs) {
    //         let new_tab = await browser.newPage(href)
    //         sleep(1000)
    //         let page_item = await scrape_resturant(new_tab)
    //         console.log(page_item)
    //         page_items.push(page_item)
    // }

    // console.log('hrefs',hrefs)
    fs.writeFileSync('open-rice.json', JSON.stringify(items))
    await browser.close();

})();

