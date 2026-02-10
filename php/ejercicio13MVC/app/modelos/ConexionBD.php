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
            "mysql:host=$host; dbname=$dbname; charset=utf8mb4";
            self::$conexion=new PDO($dsn,$user,$pw);
            self::$conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            }catch(PDOException $e){
                $log=__DIR__."/../../storage/error.log";
                $errorMsg=$e->getMessage()."|". $e->getFile()."|".$e->getLine(). PHP_EOL;
                file_put_contents($log,$errorMsg,FILE_APPEND);
                die("Error en la conexion con la base de datos");
            }
            return self::$conexion;
        }
    }

}


?>