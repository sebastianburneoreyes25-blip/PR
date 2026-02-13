<?php

class ConexionBD{
    
    static $conexion=null;

    static function obtenerConexion(){

        if(self::$conexion===null){
            $host='localhost';
            $dbname='centro';
            $user='root';
            $pw='root123';
            try{
            $dsn=
            "mysql:host=$host;dbname=$dbname;charset=utf8mb4";
            self::$conexion=new PDO($dsn,$user,$pw);
            self::$conexion->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);//Cambiamos modo de error de la base de datos a excepciones

            }catch(PDOException $e){
                $log=__DIR__."/../../storage/error.log";
                $fecha=date('Y-m-d H:i:s');
                $msgError="[$fecha]|ConexionBD|". $e->getMessage()."|". $e->getFile(). "|". $e->getLine(). PHP_EOL;
                file_put_contents($log,$msgError,FILE_APPEND);
            }
        }
        return self::$conexion;
    }

}


?>