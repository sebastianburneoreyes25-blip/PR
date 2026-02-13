<?php

require_once __DIR__."/Alumnos.php";
require_once __DIR__."/ConexionBD.php";

class RepositorioAlumnos{

    private $conexion;

    public function __construct()
    {
        $this->conexion=ConexionBD::obtenerConexion();//obtenemos la conexion a la base de datos con la funcion static
    }

    public function insertar($alumno){
        $sql='INSERT INTO alumnos(nombre, email,edad,fecha_creacion)
        VALUES (:nombre,:email,:edad,:fecha_creacion)';

        $stmt=$this->conexion->prepare($sql);//Prepara el insert sin meter ningun dato aun
        $stmt->execute([//Ejecuta el insert con los datos del alumno
            ':nombre'=>$alumno->nombre,
            ':email'=>$alumno->email,
            ':edad'=>$alumno->edad,
            ':fecha_creacion'=>$alumno->fechaCreacion

        ]);

    }
}
?>