import asyncio
from pathlib import Path
from unittest import TestCase

from pycdp import Chrome
from pycdp.extras import WebScraper

path = Path('tests/dependencies/static/website.html')


class TestWebScraper(TestCase):
    def test(self):
        async def _():
            chrome = Chrome.create().start()

            await asyncio.sleep(1)

            targets = chrome.get_targets()
            target = targets[0]

            await target.connect()
            await target.start_session()

            scraper = WebScraper.create(target)

            await scraper.navigate(path.absolute().as_uri())

            print(await scraper.get_current_url())

            result = await scraper.query_by_xpath(
                '//div[@id="queryAllByXPath"]'
            )

            print(result)

        asyncio.get_event_loop().run_until_complete(_())
