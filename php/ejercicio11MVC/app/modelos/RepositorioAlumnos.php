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

    function insertar($alumno)
    {
        $sql =
            'INSERT INTO alumnos (nombre,email,edad,fecha_creacion
                VALUES (:nombre, :email, :edad, :fecha)';

        $stmt = $this->conexion->prepare($sql);
        //consulta preparada

        $stmt->execute([
            ':nombre' => $alumno->nombre,
            ':email' => $alumno->email,
            'edad' => $alumno->edad,
            'fecha' => $alumno->fechaCreacion
        ]);
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
