
2018.4.12
version 3.1
修改部分BUG


--------------------------------------------------------------------
2018.4.8
version 3.0
移除AES解密。
加入爬取全部普通评论。
多次测试后被网易云封IP，后期应考虑优化爬取策略。


--------------------------------------------------------------------
2018.3.27
version 2.0
修改歌手列表不完全。
完成热门评论的爬取，但是爬取全站的速度较慢，后期应优化爬取速度与缓存。
优化爬取专辑策略，将limit修改到200，避免考虑翻页问题。
--------------------------------------------------------------------
2017.12.20
version 1.0
完成代码，成功连接到数据库。


     def parse_comment_pre(self, response):#解决了逻辑问题，但是增加了一倍的网页缓存
        music_id = response.meta['id']
        music_name = response.meta['music_name']
        artist = response.meta['artist']
        album = response.meta['album']
        offset_num = 0
        result = json.loads(response.text)
        total = result['total']
        other_comments = []
        hot_comments = []
        while ( total > 0):
            comments_pages_url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_' + str(music_id) +'?limit=100&offset=' + str(100*offset_num)
            offset_num += 1
            total -= 100
            yield Request(url=comments_pages_url,
                          meta={'id': music_id, 'music_name': music_name, 'artist': artist, 'album': album,
                                'other_comments':other_comments,'hot_comments':hot_comments}, callback=self.parse_comment)



    def parse_comment(self, response):
        other_comments = response.meta['other_comments']
        hot_comments = response.meta['hot_comments']
        id = response.meta['id']
        #this_page = response.meta['this_page']
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
                time = comment['time']
                vip_Type = comment['user']['vipType']#我也不知道有什么用，先采集下来吧
                data = {
                    'nickname': hotcomment_author,
                    'content': hotcomment,
                    'likedcount': hotcomment_like,
                    'avatarurl': hotcomment_avatar,
                    'time' : time,
                    'vip_Type' : vip_Type,
                    'is_hot' : True
                }
                hot_comments.append(data)

        if 'comments' in result.keys():
            for comment in result.get('comments'):
                other_comments_author = comment['user']['nickname']
                othercomments = comment['content']
                other_comments_like = comment['likedCount']
                other_comments_avatar = comment['user']['avatarUrl']
                time = comment['time']
                vip_Type = comment['user']['vipType']#我也不知道有什么用，先采集下来吧
                data = {
                    'nickname': other_comments_author,
                    'content': othercomments,
                    'likedcount': other_comments_like,
                    'avatarurl': other_comments_avatar,
                    'time' : time,
                    'vip_Type' : vip_Type,
                    'is_hot' : False
                }
                other_comments.append(data)


        item = MusicItem()
        for field in item.fields:
            try:
                item[field] = eval(field)
            except:
                print('Field is not defined', field)
        yield item
