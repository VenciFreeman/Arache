from scrapy import Spider,Request,FormRequest
import json
from lxml import etree

class TopicSpider(Spider):
    name = 'topic'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/topics']
    
    def parse(self, response):
        topics = response.xpath('.//div[@class="zm-topic-cat-page"]/ul/li')
        for topic in topics:
            topic_name = topic.xpath('./a/text()').extract_first()
            topic_id = topic.xpath('./@data-id').extract_first()

            topic_url = "https://www.zhihu.com/node/TopicsPlazzaListV2"
            yield FormRequest(url=topic_url,callback=self.parse_topic,dont_filter=True,meta={"offset":0,"topic_id":topic_id,"name":topic_name},
                        formdata={"method": "next","params": json.dumps({"topic_id":topic_id,"offset":0,"hash_id":""})})

    def parse_topic(self,response):
        offset = response.meta.get("offset")
        topic_id = response.meta.get("topic_id")
        topic_name = response.meta.get("name")
        json_info = json.loads(response.text)
        msg_info = json_info['msg']
        offset += len(msg_info)

        if not len(msg_info)<20: 
            yield FormRequest("https://www.zhihu.com/node/TopicsPlazzaListV2",callback=self.parse_topic,dont_filter=True,meta={"offset":offset,"topic_id":topic_id,"name":topic_name},
                    formdata={"method": "next","params": json.dumps({"topic_id":topic_id,"offset":offset,"hash_id":""})})
        else:
            print("name:{},topic_num:{}".format(topic_name,offset))



