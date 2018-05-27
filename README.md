# Hkdataton

Various different langauges have been used, bellow are breif install instructions and the logic behind using each.

## Python

Install pandas via anaconda. Bellow are the libraies used 

* Scrapy - Web scraping framework
* Pandas - Data for data cleaning

Scrapy was used to handle those sites that didn't use javascript to dynamically load the content with XHR request.

## Node


Install the node > 8.0,  easiest way is probaly [nvm](https://github.com/creationix/nvm) The headless chorme library [puppeteer](https://github.com/GoogleChrome/puppeteer) was used. Install it globaly using:

```
npm i puppeteer -g
```

Puppeteer was used to handle javascript heavy sites, those in which content is dynamically loaded via XHR request.

## Julia

Install julia > 0.6 and the following libraries:

*  Cascadia - CSS Selector Libary
*  Gumbo - HTML Parsing Library
*  Request - HTTP Request
*  AbstractTrees - Defininting tree like structrues
*  IJulia - Julia kerenl for jupyter notebooks

Julia was used to reverse engginer the [bus](https://mobile.nwstbus.com.hk/) websites api. 


# Results

The results can be found in the results folder. The scripts used to generate them are in the own respective folders.
The follower also contains a simple bash script which is used to convert the tsv files into the double \t\t format.

