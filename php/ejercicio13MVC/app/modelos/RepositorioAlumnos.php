<?php

require_once __DIR__ . "/Alumnos.php";
require_once __DIR__ . "/ConexionBD.php";

class RepositorioAlumnos
{

    private $conexion;

    function __construct()
    {

        $this->conexion = ConexionBD::obtenerConexion();//obtenemos la conexion con el servidor para realizar las consultas sql
    }

    function obtenerTodos(){
        $sql="SELECT * FROM alumnos ORDER BY fecha_creacion DESC";

        $stmt=$this->conexion-> query($sql);
        $alumnos=[];
        while($fila=$stmt->fetch(PDO::FETCH_ASSOC)){
            $alumnos[]=new Alumno(
                $fila['id'],
                $fila['nombre'],
                $fila['email'],
                $fila['edad'],
                $fila['fecha_creacion']
            );
        }
        return $alumnos;
    }

}
?>