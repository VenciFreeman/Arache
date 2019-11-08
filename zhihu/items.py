from scrapy import Item,Field


class ZhihuspiderItem(Item):
    question = Field()
    name = Field()    
    follower = Field()
    voteup_count = Field()
    comment_count = Field()
    content = Field()
    created_time = Field()

