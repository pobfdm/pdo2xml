<?php

//Users enabled
$validUsers = array(
    //User  and password
    "fabio" => "secret",
    "trip" => "verysecret",
);




//Preferences

//Server side
$DSN="sqlite:./examples/db.sqlite";
//$DSN="pgsql:dbname=mydb;host=localhost";
$DBUSER='fabio';
$DBPASS='';


//Client side
$sql=$_POST["sql"];
$user=$_POST["user"];
$pass=$_POST["pass"];

?>
