<?php

require_once __DIR__ . '/../modelos/RepositorioAlumnos.php';

class ControladorAlumnos
{

    private $repositorio;

    function __construct()
    {

        $this->repositorio = new RepositorioAlumnos();
    }


    function listar()
    {
        try {
            $alumnos = $this->repositorio->obtenerTodos();
            $this->renderizar('alumnos/listar', ['alumnos' => $alumnos]);
        } catch (Exception $e) {
            $this->registrarError('LISTAR', $e);
            $this->renderizar('alumnos/listar', [
                'alumnos' => [],
                'error' => 'No se pudieron cargar los alumnos.Revisa el error.log'
            ]);
        }
    }

    function crear()
    {
        $this->renderizar(
            'alumnos/crear',
            ['antiguos' => ['nombre' => '', 'email' => '', 'edad' => '',]]
        );
    }

    function guardar()
    {
        
       if ($_SERVER['REQUEST_METHOD']  !== "POST") {
            header("Location: index.php?accion=listar");
            throw new Exception("Aqui revienta");
            
        }
        
        $nombre = trim($_POST['nombre']) ?? '';
        $email = trim($_POST['email']) ?? '';
        $edad = trim($_POST['edad']) ?? '';

        try {
            $this->validar($nombre, $email, $edad);
            
            $alumno = new Alumno(
                null,
                $nombre,
                $email,
                (int)$edad, //nos aseguramos que sea int otra vez
                date('Y-m-d H:i:s')

            );
            $this->repositorio->insertar($alumno);

            header("Location: index.php?accion=listar");
            exit;
        } catch (Exception $e) {

            $this->registrarError('GUARDAR', $e);
            $this->renderizar('alumnos/listar', [
                'error' => [
                    $e->getMessage(),
                    'antiguos' => ['nombre' => $nombre, 'email' => $email, 'edad' => $edad]
                ]
            ]);
        }
    }

    function borrar()
    {
        $id = $_GET['id'] ?? '';

        try {
            if ($id === '' || !ctype_digit($id)) {
                throw new Exception(("Id invalido para borrar"));
            }
            $this->repositorio->borrarPorId($id);
        } catch (Throwable $e) {
            $this->registrarError('BORRAR', $e);
        }

        header("Location: index.php?accion=listar");
        exit;
    }

    function validar($nombre, $email, $edad)
    {
        if (strlen($nombre) < 3) {
            throw new Exception('El nombre debe tener al menos 3 caracteres');
        }
        if ($email !== '' && !filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Formato de email no valido");
        }
        if ($edad === '' || !ctype_digit($edad)) {
            throw new Exception("La edad debe ser un número");
        }
        $edadInt = (int)$edad;
        if ($edadInt < 1 || $edadInt > 120) {
            throw new Exception("La edad debe ser entre 1 y 120");
        }
    }


    function registrarError($contexto, $e) {
        $log=__DIR__.'/../../storage/error.log';
        $fecha=date('Y-m-d H:i:s');

        $linea="[$fecha]|$contexto|".$e->getMessage()."|".$e->getFile()."|". $e->getLine(). PHP_EOL;

        file_put_contents($log,$linea,FILE_APPEND);        
    }


    function renderizar($vista, $datos = []) {
        extract($datos);

        $archivoVista=__DIR__.'/../vistas/'.$vista.'.php';

        if(!file_exists($archivoVista)){
            echo 'Vista no encontrada: '. $vista;
            return;
        }
        $vistaContenido=$archivoVista;
        require_once __DIR__ . "/../vistas/layout.php";
    }

}
