QUERY_BY_XPATH_FUNCTION = '''
const queryByXPath = (xpath, contextNode = document) => {
    return document.evaluate(
        xpath,
        contextNode,
        null,
        XPathResult.FIRST_ORDERED_NODE_TYPE,
        null
    ).singleNodeValue
}
'''





async def evaluate(expression):
    pass


async def query_by_xpath(xpath: str):
    await evaluate(
        QUERY_BY_XPATH_FUNCTION
    )

    return await evaluate(
        f'queryByXPath(`{xpath}`)'
    )
