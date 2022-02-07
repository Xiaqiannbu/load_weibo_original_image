import requests

# downloadDirRoot='D:/微博图片下载/'

def downloadImg(pidList, downloadDir):
    failList=[]
    for i,pid in enumerate(pidList):
        if loadImg(pid, downloadDir,i):
            failList.append(pid)
    print('Done!\nfailList:',failList)

def loadImg(pid, downloadDir,i):
    has_error=False
    try:
        url='https://wx3.sinaimg.cn/large/'+pid+'.jpg'
        res = requests.get(url=url)
        if res.status_code == 200:
            open(downloadDir + '/' + pid + '.jpg', 'wb').write(res.content)  # 将内容写入图片
            print('Picture',i,':',pid,'has been download!')
        else:
            has_error = True
    except Exception:
        try:
            url = 'https://wx3.sinaimg.cn/large/' + pid + '.bmp'
            res = requests.get(url=url)
            if res.status_code == 200:
                open(downloadDir + '/' + pid + '.bmp', 'wb').write(res.content)  # 将内容写入图片
                print('Picture:',pid,'has been download!')
            else:
                has_error = True
        except Exception:
            try:
                url = 'https://wx3.sinaimg.cn/large/' + pid + '.gif'
                res = requests.get(url=url)
                if res.status_code == 200:
                    open(downloadDir + '/' + pid + '.gif', 'wb').write(res.content)  # 将内容写入图片
                    print('Picture:',pid,'has been download!')
                else:
                    has_error = True
            except Exception:
                try:
                    url = 'https://wx3.sinaimg.cn/large/' + pid + '.png'
                    res = requests.get(url=url)
                    if res.status_code == 200:
                        open(downloadDir + '/' + pid + '.png', 'wb').write(res.content)  # 将内容写入图片
                        print('Picture:', pid, 'has been download!')
                    else:
                        has_error = True
                except Exception:
                    try:
                        url = 'https://wx3.sinaimg.cn/large/' + pid + '.jpg'
                        res = requests.get(url=url)
                        if res.status_code == 200:
                            open(downloadDir + '/' + pid + '.jpg', 'wb').write(res.content)  # 将内容写入图片
                            print('Picture:', pid, 'has been download!')
                        else:
                            has_error = True
                    except Exception:
                        print('Download', pid, 'fail!')
    # if res.status_code==200:
    #     open(downloadDir+'/'+pid+'.jpg', 'wb').write(res.content)  # 将内容写入图片
    #     print('Picture:',pid,'has been download!')
    # else:
    #     print('ERROR!')
    #     if res.status_code == 200:
    #         open(downloadDir + '/' + pid + '.jpg', 'wb').write(res.content)  # 将内容写入图片
    #     else:
    #         print('ERROR,TWICE!')
    del res
    return has_error

# def download_img(img_url, api_token):
#     print (img_url)
#     header = {"Authorization": "Bearer " + api_token} # 设置http header，视情况加需要的条目，这里的token是用来鉴权的一种方式
#     r = requests.get(img_url, headers=header, stream=True)
#     print(r.status_code) # 返回状态码
#     if r.status_code == 200:
#         open('C:\\Users\\cloudoxou\\Desktop\\img.png', 'wb').write(r.content) # 将内容写入图片
#         print("done")
#     del r

# loadImg('006lzsJGly1goifym5xuqj343c64whdy')
# os.mkdir('D:/微博图片下载/小哥吉吉')