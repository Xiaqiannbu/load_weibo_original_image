from load_info import loadImgInfo,get_district
from download_img import downloadImg
import os

# uid='5815551992'
# userName='小哥吉吉'
def loadUserInfo():
    file=open('userinfo','r',encoding='utf-8')
    for line in file.readlines():
        if line.startswith('userName='):
            userName=line.strip()[9:]
        if line.startswith('uid='):
            uid=line.strip()[4:]
        if line.startswith('referer='):
            referer=line.strip()[8:]
        if line.startswith('cookie='):
            cookie=line.strip()[7:]
        if line.startswith('downloadDirRoot='):
            downloadDirRoot=line.strip()[16:]
    print('userName:',userName,'\nuid:',uid,'\nreferer:',referer,'\ncookie:',cookie,'\ndownloadDirRoot:',downloadDirRoot)
    return (userName,uid,referer,cookie,downloadDirRoot)

(userName,uid,referer,cookie,downloadDirRoot)=loadUserInfo()
downloadDir=downloadDirRoot+'/'+userName
if not os.path.isdir(downloadDir):
    os.makedirs(downloadDir)
pidList, since_id=get_district(loadImgInfo(uid,referer,cookie,'0&has_album=true'))
while since_id!=0:
    pidList, since_id = get_district(loadImgInfo(uid,referer,cookie,since_id),pidList)
print('Num:',len(pidList))
downloadImg(pidList, downloadDir)
