<?php 

require_once "class_email.php";

$mail=new Email("Hola", "pepito@mail.com");
$mail->enviar();


?>