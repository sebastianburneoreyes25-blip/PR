<?php


class ConexionBD{

    private static $conexion=null;

    public static function obtenerConexion(){

        if(self::$conexion===null){
            //Declaramos los atributos de la base de datos
            $host='localhost';
            $baseDatos='centro';
            $usuario='root';
            $password='root123';

            try{
                $dsn=
                "mysql:host=$host;dbname=$baseDatos;charset=utf8mb4";
                
                self::$conexion=new PDO($dsn,$usuario,$password);

                self::$conexion->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);

            }catch (PDOException $e){
                die('Error de conexión con la base de datos.');
            }
        }
        return self::$conexion;

    }


}


?>