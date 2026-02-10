<?php

class ConexionBD{

    private static $conexion=null;

    public static function obtenerConexion(){
        if(self::$conexion===null){

            $host='localhost';
            $dataBase= 'curso';
            $user='root';
            $password='root123';
            try{
                $dsn=
                "mysql:host=$host;dbname=$dataBase;charset=utf8mb4";
                self::$conexion= new PDO($dsn,$user,$password);
                self::$conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            }catch(PDOException $e){
                $log=__DIR__."/../../storage/error.log";
                $errorMsg=$e->getMessage()."|". $e->getFile()."|".$e->getLine(). PHP_EOL;
                file_put_contents($log,$errorMsg,FILE_APPEND);
                die("Error en la conexion con la base de datos");
            }
        }
        return self::$conexion;
    }

}


?>