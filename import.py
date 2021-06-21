import os
import logging
from notion_client import Client, APIErrorCode, APIResponseError
from pprint import pp, pprint

parent_page_id = os.environ["NOTION_PAGE_ID"]
notion = Client(auth=os.environ["NOTION_TOKEN"], log_level=logging.DEBUG)

try:
    res = notion.pages.create(
        parent={
            "page_id": parent_page_id,
        },
        properties={
            "title": {
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": "First page created by Notion API!",
                        },
                    },
                ],
            },
        },
    )
except APIResponseError as error:
    pprint(error)

pprint(res)

result = notion.search()
pprint(result)
