# get_updated_directories_and_files

## description
this program is created when I wanted to copy only the updated files to the usb storage. So I have computers, one at home and one at workplace. and I have many files under one directory in computer at my workplace. I want to bring every file to home as well. But I don't want to copy everything to the usb memory every time I want to bring to home. But I want to copy only updated ones to the usb memory. so when I move everything on the usb memory to home computer, they will have all updated ones overwritten and all files and folders are exactly the same as the one in workplace.

![explain](https://user-images.githubusercontent.com/56218301/209745922-2be4f5c5-52f9-4368-b08d-0fc8853209fe.png)

![folder top](https://user-images.githubusercontent.com/56218301/209749278-6e8d03f2-7d9d-42c8-bd60-fb3ac67ab709.png)

![directory structure1](https://user-images.githubusercontent.com/56218301/209749292-01d07bc5-42fa-4d63-b73f-65bfcf6873a1.png)

![chemistry folder](https://user-images.githubusercontent.com/56218301/209749310-d92d3f2b-a59a-4281-899f-454ce01d75f7.png)

![potassium chloride folder](https://user-images.githubusercontent.com/56218301/209749352-7b4f537a-86f2-4e54-a8f5-2073e12871b4.png)

![sodium hydroxide folder](https://user-images.githubusercontent.com/56218301/209749358-653401b2-1f7c-4dc2-95b3-3bd6c6d09202.png)

![folder with space folder](https://user-images.githubusercontent.com/56218301/209749382-c82f9308-5b3b-48f6-8f85-e91692fe2131.png)

![magnetic fields folder](https://user-images.githubusercontent.com/56218301/209749414-e9fca632-3e11-4b00-b2a4-77b327d75b7e.png)

![ferromagnetic material folder](https://user-images.githubusercontent.com/56218301/209749418-91194d4b-bd6d-4d21-8ef3-216728bfbb11.png)

![field interactions folder](https://user-images.githubusercontent.com/56218301/209749423-e328d509-4761-49ea-9610-a3453554dec9.png)

![field strength folder](https://user-images.githubusercontent.com/56218301/209749436-7a55b2b9-7552-4ee1-9880-c549ba08855c.png)


~~~
top directory ( experiments )
|
-> chemistry
  -new file
  -sample file1
  -sample file2
  -sodium hydroxide
    - aluminum oxide
    - heating it
  -potassium chloride
   - aluminum oxide
   - new file
   - sodium hydroxide
  
  
  
get_updated_files.py

-> folder with space
  - file with space
  - file with space2
  -> magnetic fields
     -> ferromagnetic material
      - image1
      - measuring its strength
      - video1
     
     -> field interactions
     -> field strength
     
~~~

## running example
** first time running it **
test folder ( where I want to copy all files and folders ) is empty

![first time running  test empty](https://user-images.githubusercontent.com/56218301/209750583-80b9563d-ab01-40e0-8b0a-fc5f47959c8d.png)

![first time running2](https://user-images.githubusercontent.com/56218301/209750915-48285bab-40f6-413a-a57e-5fe632f8c391.png)

then it copied all directories and files

![created top directory](https://user-images.githubusercontent.com/56218301/209751050-208168d8-8368-4576-82f8-a344218b75eb.png)

![created experiments folder](https://user-images.githubusercontent.com/56218301/209751151-79ed67f8-4791-4486-9f37-2e1e2b2d32ff.png)

![created chemistry folder](https://user-images.githubusercontent.com/56218301/209751245-a607cbfe-e274-4aef-8db0-ddaf3a48f234.png)

![created sodium hydroxide folder](https://user-images.githubusercontent.com/56218301/209751327-a04afe5e-c21c-42d0-822c-52148fd74bdf.png)

![created magnetic fields folder](https://user-images.githubusercontent.com/56218301/209751619-2147a1fb-b114-40f0-8c4b-d4ec8c805698.png)

above shows that it did not create two folders under magnetic fields folder. this is ok because they are empty folder. Once you add files to it. they will be copied.

** after modying **

![modified1](https://user-images.githubusercontent.com/56218301/209752035-7294d137-49ce-4c5b-aec8-9cb92e4ddee7.png)

![modified2](https://user-images.githubusercontent.com/56218301/209752152-bc531292-0559-412b-b0f3-ba4014f186c1.png)

![modified3](https://user-images.githubusercontent.com/56218301/209752279-5554b636-5f2a-4677-b89a-5dec8c876f97.png)

![modified4](https://user-images.githubusercontent.com/56218301/209752335-5949d102-5149-41b2-bc8b-ad7bf0f2d25f.png)

then delete all files and folders at the destination.
![delete at destination](https://user-images.githubusercontent.com/56218301/209752476-d787d0c2-89f7-4705-8e2a-b9c89e0943b9.png)

![execute](https://user-images.githubusercontent.com/56218301/209752619-326bd704-c42d-44e8-9dda-4012a1edc840.png)

then you can see that only updated files are copid!!!

![result1](https://user-images.githubusercontent.com/56218301/209752819-cc952f76-a507-46ee-b7a8-f9760f940ddd.png)

![result2](https://user-images.githubusercontent.com/56218301/209752873-32404242-72a8-46b3-858a-9493a427464e.png)

























