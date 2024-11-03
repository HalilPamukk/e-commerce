E-commerce Backend

## Description
İlk Olarak Projeyi local'inize kopyalayın.
    - git clone git@github.com:HalilPamukk/e-commerce.git
Proje dizinine gidin.
Sanal ortamı yükleyin. 
    - python3 -m venv venv
Sanal ortamı aktif edin.
    - source venv/bin/activate
.env.example dosyasını .env olarak ekleyin ve doldurun.

Eğer docker Desktop yüklü değilse yükleyin.
    - https://www.docker.com/products/docker-desktop
Docker Desktop'u açın.

terminalden projenin bulunduğu yere gidin ve docker-compose up --build komutunu çalıştırın.
    - docker-compose up --build -> Projeyi ilk defa çalıştırırken bu komutu kullanabilirsiniz. Bu işlem biraz zaman alabilir.
    - docker-compose up -> Projeyi daha önce çalıştırdıysanız bu komutu kullanabilirsiniz.
    - docker-compose up -d -> Projeyi arka planda çalıştırmak için bu komutu kullanabilirsiniz.

Proje çalıştıktan sonra http://localhost:8000/docs adresine giderek API'yi test edebilirsiniz.