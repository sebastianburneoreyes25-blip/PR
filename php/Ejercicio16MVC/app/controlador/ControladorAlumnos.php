<?php

require_once __DIR__ . "/../modelos/RepositorioAlumnos.php";

class ControladorAlumnos
{

    private $repositorio;

    function __construct()
    {
        $this->repositorio = new RepositorioAlumnos;
    }

    function render($vista, $datos = [])
    { //Funcion para renderizar la vista con los datos a mostrar
        extract($datos);
        $archivoVista = __DIR__ . "/../vistas/" . $vista . ".php";
        if (!file_exists($archivoVista)) {
            echo "Vista no encontrada";
            throw new Exception("VISTA NO ENCONTRADA");
        }
        $contenidoVista = $archivoVista;
        require __DIR__ . "/../vistas/layout.php";
    }
    function registrarError($contexto, $e)
    { //Funcion para registrat el error automaticamente dandole un contexto y el error/excepcion
        $log = __DIR__ . "/../../storage/error.log";
        $fecha = date('Y-m-d H:i:s');
        $msgError = "[$fecha]|$contexto|" . $e->getMessage() . "|" . $e->getFile() . "|" . $e->getLine() . PHP_EOL;
        file_put_contents($log, $msgError, FILE_APPEND);
    }

    function listar(){
        try {
            $alumnos = $this->repositorio->obtenerTodos();
            $this->render('alumnos/listar', ['alumnos' => $alumnos]);
        } catch (Throwable $e) {
            $this->registrarError('Listar', $e);
            $this->render('alumnos/listar', ['alumnos' => '', 'error' => 'No se pudo cargar la lista. Comprueba el log de errores.']);
        }
    }

    function editar()
    {
        try {
        $id = $_GET['id'];
        if (!ctype_digit($id)) { //confirmamos que es numerico
            throw new Exception('Id no valido. No es numerico');
        }
        $id = (int)$id; //convertimos el string obteneido del get en int.
        
            $alumno = $this->repositorio->obtenerPorID($id);
            $this->render('alumnos/editar', ['alumno' => $alumno]);
        } catch (Throwable $e) {
            $this->registrarError('Editar', $e);
            $this->render('alumnos/editar', ['alumno' => '', 'error' => 'No se pudo cargar el alumno a editar']); //En caso de que falle el obtenerPorID() debera darnos un mensaje amistoso
        }
    }

    function enviar()
    { //Funcion para enviar los nuevos datos
        try {
            if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
                throw new Exception('No se ha detectado POST');
            }
            $id = $_POST['id'];
            $nombre = $_POST['nombre'];
            $email = $_POST['email'];
            $edad = $_POST['edad'];
            $fecha = $_POST['fecha_creacion'];
            if (!ctype_digit($edad)) {
                throw new Exception('La edad no es numerica');
            }
            $alumno = new Alumno(
                (int)$id,
                $nombre,
                $email,
                (int)$edad,
                $fecha
            );
            $this->repositorio->guardarCambios($alumno);
            $this->render('alumnos/cambioCorrecto', ['alumno' => '']);
        } catch (Throwable $e) {
            $this->registrarError('Enviar Cambios', $e);
            $this->render('alumnos/editar', ['alumno' => '', 'error' => 'No se pudo editar, operación cancelada']);
        }
    }
}
