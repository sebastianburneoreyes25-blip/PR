<?php
require_once __DIR__."/ConexionBD.php";
require_once __DIR__."/Alumno.php";

class RepositorioAlumno{

    private $conexion;

    function __construct(){
        $this->conexion=ConexionBD::obtenerConexion();

    }

    function obtenerTodos(){
        $sql='SELECT * FROM alumnos ORDER BY id ASC;';
        $stmt=$this->conexion->query($sql);
        $alumnos=[];
        while($fila=$stmt->fetch(PDO::FETCH_ASSOC)){//usamosun bule while(mientras exista una fila de la consulta seguira el bucle.)

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

    function borrarPorId($id){
        
        $sql="DELETE  FROM alumnos WHERE id=:id";
        $stmt=$this->conexion->prepare($sql);
        $stmt->execute([':id'=>$id]);

    }

}



?>