# -*- coding: utf-8 -*-

## Convert string Base64 Images

def convertBase64String(base64Img,uploadfolder):
    if base64Img.startswith("data:image/png;base64,"):
        import base64
        import uuid
        base64Img = base64Img[22:]
        image = base64.b64decode(base64Img)
        filename = "auth_user.avatar.%s.%s.png" %(uuid.uuid4().hex, uuid.uuid4().hex)

        with open(uploadfolder+filename, 'wb') as imgFile:
            imgFile.write(image)

        return filename

    else:
        return False
