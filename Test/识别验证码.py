import base64
import ddddocr
data = 'data:image/jpeg;base64,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'
data = data.replace("data:image/jpeg;base64,","")
data = data.replace(' ', '+')
imgdata = base64.b64decode(data)

ocr = ddddocr.DdddOcr()
res = ocr.classification(imgdata)
print(res)

