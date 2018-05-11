# -*- coding: utf-8 -*-
import json

from scrapy import Spider, Request, FormRequest
from ..settings import DEFAULT_REQUEST_HEADERS
from ..items import MusicItem
import time

class MusicSpider(Spider):
    name = "musictest"
    allowed_domains = ["163.com"]
    base_url = 'https://music.163.com'


    def start_requests(self):
        # for id in self.ids:
        #     for initial in self.initials:
        #         url = '{url}/discover/artist/cat?id={id}&initial={initial}'.format(url=self.base_url, id=id,initial=initial)
        #         yield Request(url, callback=self.parse_index)
        music_url = 'http://music.163.com/#/song?id=210049'
        yield Request(music_url, meta={'id': 210049},callback=self.parse_music)
    # 获得所有歌手的url


    # version 2.0
    def parse_music(self, response):  # 接收到歌曲ID
        music_id = response.meta['id']
        music_name = response.xpath('//div[@class="tit"]/em[@class="f-ff2"]/text()').extract_first()
        artist = response.xpath('//div[@class="cnt"]/p[1]/span/a/text()').extract_first()
        album = response.xpath('//div[@class="cnt"]/p[2]/a/text()').extract_first()
        comments_pages_url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_' + str(music_id) #+ \
                                # '?limit=100&offset=' + str(100*i)
        yield Request(url = comments_pages_url, meta={'id': music_id, 'music_name': music_name, 'artist': artist,'album': album},callback=self.parse_comment_pre)




    def parse_comment_pre(self, response):  # 解决了逻辑问题，但是增加了一倍的网页缓存
        music_id = response.meta['id']
        music_name = response.meta['music_name']
        artist = response.meta['artist']
        album = response.meta['album']
        offset_num = 0
        result = json.loads(response.text)
        total = result['total']
        other_comments = []
        hot_comments = []
        while (total > 0):
            comments_pages_url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_' + str(
                music_id) + '?limit=100&offset=' + str(100 * offset_num)
            offset_num += 1
            total -= 100
            yield Request(url=comments_pages_url,
                          meta={'id': music_id, 'music_name': music_name, 'artist': artist, 'album': album,
                                'other_comments': other_comments, 'hot_comments': hot_comments},
                          callback=self.parse_comment)

    def parse_comment(self, response):
        other_comments = response.meta['other_comments']
        hot_comments = response.meta['hot_comments']
        id = response.meta['id']
        music = response.meta['music_name']
        artist = response.meta['artist']
        album = response.meta['album']
        result = json.loads(response.text)
        total = result['total']

        if 'hotComments' in result.keys():
            for comment in result.get('hotComments'):
                hotcomment_author = comment['user']['nickname']
                hotcomment = comment['content']
                hotcomment_like = comment['likedCount']
                hotcomment_avatar = comment['user']['avatarUrl']
                t = comment['time']
                real_date = time.strftime('%Y-%m-%d', time.localtime(t*0.001))
                vip_Type = comment['user']['vipType']  # 我也不知道有什么用，先采集下来吧
                data = {
                    'nickname': hotcomment_author,
                    'content': hotcomment,
                    'likedcount': hotcomment_like,
                    'avatarurl': hotcomment_avatar,
                    'time': real_date,
                    'vip_Type': vip_Type,
                    'is_hot': True
                }
                hot_comments.append(data)

        if 'comments' in result.keys():
            for comment in result.get('comments'):
                other_comments_author = comment['user']['nickname']
                othercomments = comment['content']
                other_comments_like = comment['likedCount']
                other_comments_avatar = comment['user']['avatarUrl']
                t = comment['time']
                real_date = time.strftime('%Y-%m-%d', time.localtime(t * 0.001))
                vip_Type = comment['user']['vipType']
                data = {
                    'nickname': other_comments_author,
                    'content': othercomments,
                    'likedcount': other_comments_like,
                    'avatarurl': other_comments_avatar,
                    'time': real_date,
                    'vip_Type': vip_Type,
                    'is_hot': False
                }
                other_comments.append(data)

        item = MusicItem()
        for field in item.fields:
            try:
                item[field] = eval(field)
            except:
                print('Field is not defined', field)
        yield item
