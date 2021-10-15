![Python Email Parser](./repository-image.png)

# Парсер писем

### 1. Открываем доступ по IMAP к почтовому ящику:
[Link to Google HOW-TO](https://support.google.com/mail/answer/7126229?hl=ru#zippy=%2C%D1%88%D0%B0%D0%B3-%D0%B2%D0%BA%D0%BB%D1%8E%D1%87%D0%B8%D1%82%D0%B5-imap-%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF)
**Шаг 1. Включите IMAP-доступ:**
  + Откройте Gmail на компьютере.
  + В правом верхнем углу нажмите на значок "`Настройки`" Настройки затем `Все настройки`.
  + Откройте вкладку `Пересылка и POP/IMAP`.
  + В разделе "`Доступ по протоколу IMA`P" выберите `Включить IMAP`.
  + Нажмите Сохранить изменения.

**Шаг 2. Включить доступ небезопасным приложениям по** [ссылке](https://myaccount.google.com/lesssecureapps):
  + Заходим в настройки аккаунта Google.
  + Открываем [вкладку `Безопасность`](https://myaccount.google.com/u/5/security?nlr=1).
  + `Управление устройствами`.
  + Разрешаем действия от `подозрительного аккаунта`.

### 2. Устанавливаем окружение:
```
sudo apt install python3.9-venv
python3.9 -m pip install --user --upgrade pip
python3.9 -m pip install --user virtualenv
python3.9 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install --upgrade -r requirements.txt  # upgrade all packages
deactivate
```

### 3. Создаём **.env** файл с переменными огружения:
```
EMAIL_USER=<USERNAME>@gmail.com
PASSWORD=<PASSWORD>
RECIEVED_FROM_EMAIL=<EMAIL_RECIEVED_FROM_EXAMPLE=helloworld@gmail.com>
IMAP_URL=imap.gmail.com
FILENAME=codes.csv
```
