# LT
создать любую папку например test

cd test

git clone https://github.com/Zarbul/LT.git

python3 -m venv LT

source LT/bin/activate

pip install django

pip install django_adminlte2

python LT/LT/manage.py migrate

python LT/LT/manage.py runserver 9000

перейти в браузере по аресу 127.0.0.1:9000

на данный момент данные фильтруются в коде, а не берутся нужные из БД

замечен баг с отображение графика (при разных выборах графики накладываются друг на друга)

данные в БД вносил вручную (за 2017 и 2018 года для восточно-сибирского филиала) в дальнейшем возможно сделать загрузку файла

