
#!/bin/bash


# 1. Сохранение истории команд

history > ~/питомник/история_команд.txt

echo "История команд сохранена в ~/питомник/история_команд.txt"


# 2. Создание базы данных в MySQL

echo "Создание БД..."

mysql -e "CREATE DATABASE IF NOT EXISTS my_database;"


# 3. Настройка Git-репозитория

echo "Настройка Git репозитория..."

cd ~/питомник

git init

git add .

git commit -m "Initial commit"


echo "Все задачи выполнены!"


