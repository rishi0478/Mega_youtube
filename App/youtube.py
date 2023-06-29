import yt_dlp



def Youtube_conveter(url):

    link = url

    ydl_opts = {
        'format': 'best',
        'outtmpl': '~/Downloads/%(title)s.%(ext)s',  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        a =ydl.download([link])
        print(a,"=======")


    # print("Downloaded", link, "to default download folder")
    return True
