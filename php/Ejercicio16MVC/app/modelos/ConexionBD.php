<?php


class ConexionBD{

    static $conexion=null;

    public static function obtenerConexion(){//Funcion que usaremos luego para obtener la conexion desde otros archivos sin crear el objeto
        if(self::$conexion===null){//si la conexion es nula, hara el enlace con la base
            $host='localhost';
            $dbname='centro';
            $user='root';
            $pw='root123';
            
            try{
                $dsn=
                "mysql:host=$host;dbname=$dbname;charset=utf8mb4";
                self::$conexion=new PDO($dsn,$user,$pw);
                self::$conexion->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);//Hacemos que el formato de error sea excepcion para capturarlo

            }catch(PDOException $e){
                die('Error al conectar con la base de datos');
            }
        }
        return self::$conexion;
    }
}