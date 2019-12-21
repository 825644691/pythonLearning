# coding=utf8
import urllib.parse
import json
import time

s = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI04094339935171054&g_tk=5381&loginUin=825644691&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%2C%22singerList%22%3A%7B%22module%22%3A%22Music.SingerListServer%22%2C%22method%22%3A%22get_singer_list%22%2C%22param%22%3A%7B%22area%22%3A2%2C%22sex%22%3A-100%2C%22genre%22%3A-100%2C%22index%22%3A-100%2C%22sin%22%3A1520%2C%22cur_page%22%3A20%7D%7D%7D'
print(urllib.parse.unquote(s))

# try_begin: 80214,
# try_end: 106353,
# timeArray = time.localtime(106553-80214)
# print((106553-80214)%86400%3600)


# 官方歌单2 https://u.y.qq.com/cgi-bin/musicu.fcg?_=1574480448523&g_tk=1736564252&uin=825644691&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&ct=23&cv=0&data={"list":{"module":"playlist.PlayListCategoryServer","method":"get_category_content","param":{"cmd":0,"caller":"825644691","category_id":3317,"last_id":"7287825028","size":500}}}

# 网络歌曲3 https://u.y.qq.com/cgi-bin/musicu.fcg?_=1574483733246&g_tk=1736564252&uin=825644691&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&ct=23&cv=0&data={"list":{"module":"playlist.PlayListCategoryServer","method":"get_category_content","param":{"cmd":0,"caller":"825644691","category_id":3056,"last_id":"0","size":500}}}

# 情歌歌单4 https://u.y.qq.com/cgi-bin/musicu.fcg?_=1574484717972&g_tk=1736564252&uin=825644691&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&ct=23&cv=0&data={"list":{"module":"playlist.PlayListCategoryServer","method":"get_category_content","param":{"cmd":0,"caller":"825644691","category_id":71,"last_id":"0","size":500}}}

# KTV金曲5 https://u.y.qq.com/cgi-bin/musicu.fcg?data={"list":{"module":"playlist.PlayListCategoryServer","method":"get_category_content","param":{"caller":"825644691","category_id":64,"size":500}}}

# KTV金曲5 https://u.y.qq.com/cgi-bin/musicu.fcg?data={"list":{"module":"playlist.PlayListPlazaServer","method":"get_playlist_by_category","param":{"id":199,"size":120}}}

# 背景音乐6 https://u.y.qq.com/cgi-bin/musicu.fcg?_=1575040522290&g_tk=2066655610&uin=825644691&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&ct=23&cv=0&data={"list":{"module":"playlist.PlayListCategoryServer","method":"get_category_content","param":{"cmd":0,"caller":"825644691","category_id":107,"last_id":"0","size":500}}}

# 歌曲 http://122.226.161.24/amobile.music.tc.qq.com/C400003oGhuj0Nshlv.m4a?guid=00000000205c2f07fffffffff0fefa6d&vkey=3CECBC2934E19D1A805A2AD1EBEDB6F3999BDC52412132D5D7BD5EE2E45B301C384CD38E4026105D741A616123034F49D59F786830F1FCE7&uin=5779&fromtag=130


# 歌曲hq高清 http://ws.stream.qqmusic.qq.com/C4000044LVIg1ynEsr.m4a?guid=3687924649&vkey=DF679879086779DE71C188D0BD7C3A99B531167444F72EB8DFBDF09FD57729CA05B964E3512C7BF97E3902B51C5A0043B5887CAC8EC7F098&fromtag=66
#                                                                                                             909172EB11F40FAABCEBC0F58391F53CCEA2C63910BF016BAB4B791B77A836C65E2717D8465D7458F5B4F75FA8EE6EC22CE5B2A0D23223CA&uin=825644691&fromtag=133
# 歌曲普通   http://124.172.114.28/amobile.music.tc.qq.com/C400003mAan70zUy5O.m4a?guid=00000000205c2f07fffffffff0fefa6d&vkey=EB5E4442AB01F21D5E1090E2B9B37313A35812451045694F095073D79333DE61889D8848610990BD818ACC82E7F25D8DB325627D9A30364E&uin=5779&fromtag=66


# https://y.gtimg.cn/music/photo_new/T002R300x300M000000OzqkG3PTxG5.jpg

# https://y.gtimg.cn/music/photo_new/T002R300x300M000002jd4Jy2b68s6.jpg

#漫画 http://app.u17.com/v3/appV3_3/android/phone/comic/chapterNew?come_from=huawei&serialNumber=8BNDU17923003020&v=4900100&model=STF-AL00&chapter_id=466908&android_id=38b7bc55e274b6c5&key=28035a5a0c0590407393a07dcc5f1617588807bcce0bb8994da39a72d35bd80ab0457e9a086102aa99ac377f7c55182c231f88a7208c88ed87ad251e32650abb64a6702364cf4aee5dab1a871de74e9758fd2858c1778c80079c33f34df3e303e260f8a1c4367bb4edbe8f5ca58864c5cddd649d5392727d6b58f556b6b01628%253A%253A%253Aopen


#用mid获取vkey https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=678733985&jsonpCallback=MusicJsonCallback8015407264426806&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8¬ice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback8015407264426806&songmid=0044LVIg1ynEsr&filename=C4000044LVIg1ynEsr.m4a&guid=00000000205c2f07fffffffff0fefa6d
#用mid获取vkey https://u.y.qq.com/cgi-bin/musicu.fcg?data={"comm":{"ct":24,"cv":10000},"singerList":{"module":"Music.SingerListServer","method":"get_singer_list","param":{"area":-100,"sex":-100,"genre":-100,"index":-100,"sin":0,"cur_page":1}}}


# media_mid=001OJvNw2OlpHQ


#
#https://dl.stream.qqmusic.qq.com/C400003mAan70zUy5O.m4a?guid=00000000205c2f07fffffffff0fefa6d&vkey=3609E4838E0345A37EA7346507411A4D6EB2AC807D238703E3EFAF2FF516EB78187290063AFFE344DFA7D97600600B9FE42E72B67BD8DDB8&uin=5779&fromtag=3
#
#http://124.172.114.28/amobile.music.tc.qq.com/M8000044LVIg1ynEsr.mp3?guid=00000000205c2f07fffffffff0fefa6d&vkey=30225F2F510A99A48AA3B57053D02AA3E62BF6DE84B8A22FA525108E4A05F2FA1B4AF531106DABE24318D0B61852A96787C86FF1AF50C102&uin=825644691&fromtag=133
#
#
#enquote 改mid得到purl和http://ws.stream.qqmusic.qq.com/结合：   https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"3687924649","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"3687924649","songmid":["002hfZ6D0kwZlM"],"songtype":[0],"uin":"825644691","loginflag":1,"platform":"20"}}}


# https://y.gtimg.cn/music/photo_new/T002R300x300M000000NFmo02hb0yA.jpg
# https://y.gtimg.cn/music/photo_new/T002R300x300M0000011WhAg0I4Bst.jpg
# https://y.gtimg.cn/music/photo_new/T002R300x300M000001rBvhz2ebQSZ.jpg?max_age=2592000
#
#
#                                                    000NFmo02hb0yA


# 歌手 https://u.y.qq.com/cgi-bin/musicu.fcg?data={"singerList":{"module":"Music.SingerListServer","method":"get_singer_list","param":{"area":-100,"sex":-100,"genre":-100,"index":-100,"sin":0,"cur_page":1}}}
# 歌手 https://u.y.qq.com/cgi-bin/musicu.fcg?data={"singerList":{"module":"Music.SingerListServer","method":"get_singer_list","param":{"area":-100,"sex":-100,"genre":-100,"index":-100,"sin":160,"cur_page":3}}}
# 歌手 https://u.y.qq.com/cgi-bin/musicu.fcg?data={"comm":{"ct":24,"cv":0},"singerList":{"module":"Music.SingerListServer","method":"get_singer_list","param":{"area":-100,"sex":-100,"genre":-100,"index":-100,"sin":80,"cur_page":2}}}
# 分类


# 歌词 https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg?-=MusicJsonCallback_lrc&pcachetime=1576220672010&songmid=000XdmgO2ZcvTP&g_tk=5381&loginUin=825644691&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0


# import librosa
# t = librosa.get_duration(filename='f:/qqMusic/1000090.m4a')
# print(t)
import json
import subprocess
#
# from pydub.utils import mediainfo
# song = mediainfo("F:/qqMusic/1882.m4a")
# print(song)


# from pymediainfo import MediaInfo
# media_info = MediaInfo.parse('f:/qqMusic/1000090.m4a')
# data = media_info.to_json()
# print(json.loads(data)['tracks'][0]['duration'])


# 评论 https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?biztype=3&topid=4265835817&cmd=8&pagesize=100


BaseUrl = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"singerList":{"module":"Music.SingerListServer","method":"get_singer_list","param":{"area":%s,"sex":-100,"genre":%d,"index":-100,"sin":'
EndUrl = ',"cur_page":1}}}'
offset = 40
current_area = 1
current_tag = 1
start_urls = [(BaseUrl + str(offset) + EndUrl)]
singer_tag = {1: '流行', 6: '嘻哈', 2: '摇滚', 4: '电子', 3: '民谣', 8: 'R&B', 10: '民歌', 9: '轻音乐', 5: '爵士', 14: '古典', 25: '乡村', 20: '蓝调'}
for t in list(singer_tag.keys())[1:]:
    print(t)
