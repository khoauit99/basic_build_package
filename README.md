# Basic_Build_Package
## Tutorial build package


#### Sẽ có khá nhiều cách để install các package cần thiết cho một cái project 
+ Install bên trong setup.py như được thiết kế như trong file tmp.py
+ Install bên trong terminal bằng lệnh với tệp requirements.txt
+ Install bên trong install_sh cú pháp cũng giống như bên trong terminal nhưng lúc này chúng ta sẽ quản lí được hết
+ Install bên trong setup.py nhưng thông qua tệp requirements.txt

```
 Vì trong ví dụ này chỉ nói về cơ bản cách xài nên không install những package quá phức tạp
```

## Step for run this package

```
B1 : run file install_all.sh with command: bash install_all.sh
B2 : active virtualven : source vendors/bin/activate
B3 : Test command :     
    khoa_hello 
    khoa_plus -number_1 10 -number_2 20
```    

## Attention
```
Đối với mỗi folder chúng ta phải có file __init.py__ để package có thể nhận diện được folder 
```
