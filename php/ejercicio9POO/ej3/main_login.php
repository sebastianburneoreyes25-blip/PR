<?php
require_once "class_login.php";


try{
    $user1=new Login("Lope",4567);
    $user2=new Login("Taki",1234);
    $user1->comprobar();
    $user2->comprobar();
    $user3= new Login("hola",);//dara error y se guaradara en error.log
    


}catch (Throwable $e){//Al estar vacio uno de los campos en user3, daba error(no excepcion) asi que necesitamos Throwable para capturarlo y evitar que falle el codigo
    $fecha = date("Y-m-d H:i:s");
    $msgError = "[$fecha] Error:" . $e->getMessage() . PHP_EOL;
    file_put_contents("error.log", $msgError, FILE_APPEND);
}

?>