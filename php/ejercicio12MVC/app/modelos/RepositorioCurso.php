<?php

require_once __DIR__ . "/ConexionBD.php";
require_once __DIR__ . "/Curso.php";


class RepositorioCurso
{

    private $conexion;

    function __construct()
    {
        $this->conexion = ConexionBD::obtenerConexion();
    }

    function insertar($curso)
    {

        $sql = 'INSERT INTO cursos(nombre, horas, fecha_creacion) 
            VALUES (:nombre,:horas,:fecha_creacion)';

        $stmt = $this->conexion->prepare($sql);//prepara el insert sin hacerla
        //ejecuta la query
        $stmt->execute([
            ':nombre' => $curso->nombre,
            ':horas' => $curso->horas,
            ':fecha_creacion' => $curso->fecha_creacion
        ]);
    }

    function obtenerTodas()
    {
        $sql = "SELECT * FROM cursos ORDER BY fecha_creacion DESC";

        $stmt = $this->conexion->query($sql);
        $cursos = [];

        while ($fila = $stmt->fetch(PDO::FETCH_ASSOC)) {//cogemos con el fetch(PDO::FETCH_ASSOC) de una en una linea de la query
            $cursos[] = new Curso(
                $fila['id'],
                $fila['nombre'],
                $fila['horas'],
                $fila['fecha_creacion']
            );
        }
        return $cursos;//devolvemos array de objetos
    }

    
}
?>