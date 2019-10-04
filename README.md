# Pdo2xml

A simple "proxy" from php-pdo to xml file.
Pdo2xml produces a representation of your query in xml. Here is an example:
````
<?xml version="1.0" encoding="UTF-8"?>
<query>
 <fields>
   <field name="id"></field>
   <field name="surname"></field>
   <field name="name"></field>
   <field name="email"></field>
   <field name="phone"></field>
 </fields>

<records>
  <record><cell>1</cell><cell >Di Matteo</cell> <cell >Fabio</cell><cell >fabio@localhost</cell><cell >87329487</cell></record>
  <record><cell>2</cell><cell >Di Matteo</cell> <cell >Chester</cell><cell >chester@localhost</cell><cell >0000</cell></record>
  ...
</records>
</query>

````



Look at the "examples" folder for more details.

Run from this folder:
```
php -S 0.0.0.0:8080
```

Edit 'conf.php' according to your needs.
