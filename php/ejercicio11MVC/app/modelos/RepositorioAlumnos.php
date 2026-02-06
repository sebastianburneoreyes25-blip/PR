<?php

require_once __DIR__ . '/ConexionBD.php';
require_once __DIR__ . '/Alumno.php';

class RepositorioAlumnos
{

    private $conexion;

    function __construct()
    { //siempre que se cree un objeto RepositorioAlumno se obtendra la conexion a la base de datos

        $this->conexion = ConexionBD::obtenerConexion();
    }

    function insertar($alumno){
  
    try {
        echo "ENTRÓ A INSERTAR<br>";

        $sql = 'INSERT INTO alumnos (nombre,email,edad,fecha_creacion)
                VALUES (:nombre, :email, :edad, :fecha)';

        $stmt = $this->conexion->prepare($sql);

        $stmt->execute([
            ':nombre' => $alumno->nombre,
            ':email' => $alumno->email,
            ':edad' => $alumno->edad,
            ':fecha' => $alumno->fechaCreacion
        ]);
        echo "EJECUTÓ EL INSERT<br>";

        echo "INSERT OK";
    } catch (PDOException $e) {
        echo "ERROR SQL: " . $e->getMessage();
        exit;
    }
    }


    function obtenerTodos()
    {
        $sql =
            "SELECT * FROM alumnos ORDER BY fecha_creacion DESC";

        $stmt = $this->conexion->query($sql);
        $alumnos = [];

        while ($fila = $stmt->fetch(PDO::FETCH_ASSOC)) {
            $alumnos[] = new Alumno(
                $fila['id'],
                $fila['nombre'],
                $fila['email'],
                $fila['edad'],
                $fila['fecha_creacion']
            );
        }
        return $alumnos;
    }


    function borrarPorId($id)
    {
        $sql = 'DELETE FROM alumnos WHERE id=:id';
        $stmt = $this->conexion->prepare($sql);
        $stmt->execute([':id' => $id]);
    }
}
