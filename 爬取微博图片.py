from load_info import loadImgInfo,get_district,load_userName
from download_img import downloadImg
import os

# uid='5815551992'
# userName='小哥吉吉'
def loadUserInfo():
    file=open('userinfo','r',encoding='utf-8')
    for line in file.readlines():
        # if line.startswith('userName='):
        #     userName=line.strip()[9:]
        if line.startswith('uid='):
            uid=line.strip()[4:]
        # if line.startswith('referer='):
        #     referer=line.strip()[8:]
        if line.startswith('cookie='):
            cookie=line.strip()[7:]
        if line.startswith('downloadDirRoot='):
            downloadDirRoot=line.strip()[16:]
    print('\nuid:',uid,'\ncookie:',cookie,'\ndownloadDirRoot:',downloadDirRoot)
    return (uid,cookie,downloadDirRoot)

(uid,cookie,downloadDirRoot)=loadUserInfo()
userName=load_userName(uid,cookie)
downloadDir=downloadDirRoot+'/'+userName
if not os.path.isdir(downloadDir):
    os.makedirs(downloadDir)
pidList, since_id=get_district(loadImgInfo(uid,cookie,'0&has_album=true'))
while since_id!=0:
    pidList, since_id = get_district(loadImgInfo(uid,cookie,since_id),pidList)
print('Num:',len(pidList))
downloadImg(pidList, downloadDir)
