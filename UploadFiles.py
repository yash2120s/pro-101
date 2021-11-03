import dropbox

class TransferData:
    def __init__(self,access_token) :
       self.access_token = access_token

    def  upload_file(self,file_from,file_to):
         dbx = dropbox.Dropbox(self.access_token)
         f = open(file_from,'rb')
         dbx.files_upload(f.read(),file_to)

def  main():
    access_token = 'sl.A7lOdNdT1Mx4IiABho8x_rbOxhV0KayxNJF2CkeGMS8YF4H7v2jLaoCy4xouqUKc83yRfOMTK2CyQGksEb4i2V18Pv64VwJhAAONvwhHeGnpyNkWpS1EKnQjN5K5GLmlodZgb3s'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer")
    file_to = input("enter the full path")

    transferData.upload_file(file_from,file_to)
    print("file uploaded")


# if __name__ =="__main__":
main()