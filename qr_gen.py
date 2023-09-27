import qrcode
from filestorage import FileStorage
from random import SystemRandom
secure_rand_gen = SystemRandom()


def generate(data):
    res = any(len(ele) == 0 for ele in data)
    if res is True:
        return

    fs = FileStorage()
    fs.reload()
    data1 =  dict()
    data1['id'] = ''.join([str(secure_rand_gen.randrange(10)) for i in range(5)])
    data1["first_name"] = data[0]
    data1["last_name"] = data[1]

    if data1:
        fs.new(data1)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data1)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"qr_pngs/{data1.get('first_name',None)}.png")

    fs.save()
    
#if __name__ == "__main__":
#    generate()

"""
#img = cv2.imread(f"qr_pngs/{data1.get('first_name',None)}.png")
#cv2.imshow(data1.get('first_name',None), img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
    wb = openpyxl.load_workbook("myfile.xlsx")
    ws = wb.active
    print(data1['id'],data1["first_name"],data1["last_name"])
    ws.append([data1['id'],data1["first_name"],data1["last_name"]])
    wb.save('myfile.xlsx')
"""