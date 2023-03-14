1.get age
```python
    def get_age(self):
        now = datetime.datetime.now()
        return self.yob - now.year
```
Вычитание неверное
```python
    return self.yob - now.year
```
Правильный вариант
```python
    return now.year - self.yob
```

2. set name

Неверное присваивание
```python
    def set_name(self, name):
        self.name = self.name
```
Правильный вариант
```python
    def set_name(self, name):
        self.name = name
```

3. set address

Лишний знак равенства, выполняется сравнение, а не присваивание
```python
    def set_address(self, address):
        self.address == address
```
Правильный вариант
```python
    def set_address(self, address):
        self.address = address
```
4. is homeless

По умолчанию, при инициализации, адресс равен пустой строке, не None, некорректная проверка
```python
    def is_homeless(self):
        '''
        returns True if address is not set, false in other case
        '''
        return address is None
```
Правильнай вариант
```python
    def is_homeless(self):
        '''
        returns True if address is not set, false in other case
        '''
        return self.address == ''
```