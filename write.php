<?php
  require("login.php");



  //Override all ! Only for testing
  /*$user="fabio";
  $pass="secret";
  $sql="INSERT INTO  `contacts` ( `surname` ,`name` , `email`, `phone` ) VALUES ( 'Cat' , 'Mone' , 'mone@email.com','9892346' );" ;
*/


  //Login
  if (!login($user,$pass)) die();

  try{
      $dbh = new PDO($DSN, $DBUSER, $DBPASS);
      $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
      $sth = $dbh->prepare($sql);
      $sth->execute();
      print('<?xml version="1.0" encoding="UTF-8"?><success>Record saved</success><lastid>'.$dbh->lastInsertId() .'</lastid>');

  }catch(PDOException  $e ){
    print('<?xml version="1.0" encoding="UTF-8"?><error>Error:' .$e.'</error>');
    die();
  }

?>
