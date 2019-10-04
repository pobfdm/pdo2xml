<?php
  require("login.php");



  //Override all ! Only for testing
  /*$user="fabio";
  $pass="secret";
  $sql="select * from contacts";
*/


  //Login
  if (!login($user,$pass)) die();

  try{
      $dbh = new PDO($DSN, $DBUSER, $DBPASS);
      $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
      $sth = $dbh->prepare($sql);
      $sth->execute();
      $colcount = $sth->columnCount();
      ?>
<?xml version="1.0" encoding="UTF-8"?>
<query>
<fields>
<?php
      for ($i=0; $i< $colcount; $i++)
      {

            $meta = $sth->getColumnMeta($i);
            print "<field name=\"".$meta['name']."\"></field>\n"  ;

      }
      //records
      echo "</fields>\n<records>\n";
      $result = $sth->fetchAll();
      for ($i=0; $i<count($result); $i++)
      {
        echo "<record>";
        for ($j=0; $j <$colcount ; $j++) {
          print("<cell>".$result[$i][$j]."</cell>");
        }
        echo "</record>\n";
      }


  }catch(PDOException  $e ){
    print('<?xml version="1.0" encoding="UTF-8"?><error>Error:' .$e.'</error>');
    die();
  }

?>
</records>
</query>
