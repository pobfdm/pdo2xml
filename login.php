<?php
require("conf.php");


function login($user,$pass)
{
  global $validUsers;

  if ($validUsers[$user]==$pass)
  {
    return True;
  }else{
    print('<?xml version="1.0" encoding="UTF-8"?>
    <error>Login Error</error>');
    return false;
  }



}


 ?>
