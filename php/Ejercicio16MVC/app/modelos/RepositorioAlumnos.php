<?php

require_once __DIR__ . "/Alumnos.php";
require_once __DIR__ . "/ConexionBD.php";

class RepositorioAlumnos
{

    private $conexion;

    function __construct()
    {
        $this->conexion = ConexionBD::obtenerConexion();
    }

    function obtenerTodos()
    {

        $sql = "SELECT * FROM alumnos ORDER BY id ASC;";
        $stmt = $this->conexion->query($sql); //usamos el metodo query de conexion
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

    function obtenerPorID($id)
    {

        $sql = "SELECT * FROM alumnos WHERE id=:id"; //no ponemos variables directamente en la sentencia sql
        $stmt = $this->conexion->prepare($sql); //preparamos la sentencia
        $stmt->execute([':id' => $id]); //la ejecutamos
        $datos = $stmt->fetch(PDO::FETCH_ASSOC); //capturamos el resultado para devolverlo
        $alumno=new Alumno(
            $datos['id'],
            $datos['nombre'],
            $datos['email'],
            $datos['edad'],
            $datos['fecha_creacion']
            );
        return $alumno;
    }

    function guardarCambios($alumno)
    {

        $sql = "UPDATE alumnos SET
         nombre =:nombre,
         email=:email,
         edad=:edad
         WHERE id=:id;"; //sentencia sql
        $stmt = $this->conexion->prepare($sql); //preparamos la sentencia sin parametros
        $stmt->execute([':id' => $alumno->id, ':nombre' => $alumno->nombre, ':email' => $alumno->email, ':edad' => $alumno->edad]); //Ejecutamos la sentencia dando los valores

    }
}
