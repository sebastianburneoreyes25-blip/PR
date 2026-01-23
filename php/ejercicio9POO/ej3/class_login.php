<?php

class Login{

    private $usuario;
    private $password;

    public function __construct($user,$pw){
           
            $this->usuario=$user;
            $this->password=$pw;
        if(empty($user)|| empty($pw)){//Le damos la condicion para lanzar la excepcion, si no, siempre cortara la funcion sin crear el objeto.
            throw new \Exception('Usuario no creado.');
        }
            
    }
    public function comprobar(){//comprobamos que las credenciales sean las correcras
        if ($this->password==1234){
            echo "Contraseña correcta. Acceso concedido a ". $this->usuario.PHP_EOL;

        }else{
            echo "Credenciales incorrectas. Acceso denegado.\n";

        }
    }


}

?>