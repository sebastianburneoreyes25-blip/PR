<?php

require_once __DIR__ . "/../modelos/RepositorioCurso.php";

class ControladorCursos
{

    private $repositorio;

    function __construct()
    {
        $this->repositorio = new RepositorioCurso;
    }


    function listar()
    {
        try {
            $cursos = $this->repositorio->obtenerTodas();
            $this->render('cursos/listar', ['cursos' => $cursos]);
        } catch (Throwable $e) {
            $this->registarErrores('Listar', $e);
            $this->render('cursos/listar', ['cursos' => '', 'error' => 'No se pudo cargar la lista de errores']);
        }
    }

    function crear()
    { //Funcion que solamene se usa para enviarnos al formulario para crear cusos
        $this->render('cursos/crear', ['antiguos' => ['nombre' => '', 'horas' => '']]);
    }

    function guardar()
    { //Funcion para guardar cursos
        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {

            header("Location: index.php?accion=listar");
            exit;   
        }
        $nombre = trim($_POST['nombre']) ?? '';
        $horas = trim($_POST['horas']) ?? '';

        try {
            $this->validar($nombre, $horas);
            $curso = new Curso(
                null,
                $nombre,
                (int)$horas,
                date('Y-m-d H:i:s')
            );

            $this->repositorio->insertar($curso);
            header('Location: index.php?accion=listar');
            exit;
        } catch (Throwable $e) {
            $this->registarErrores('Guardar', $e);
            $this->render('cursos/listar', ['error' => $e->getMessage(), 'antiguos' => ['nombre' => $nombre, 'horas' => $horas]]);
            header('Location: index.php?accion=listar');
            exit;
        }
    }

    function validar($nombre, $horas) {
        if(strlen($nombre)<3){
            throw new Exception("El nombre debe tener una longitud minima de 3 letras");
        }
        if ($horas===''||!ctype_digit($horas)){
            throw new Exception("Las horas deben ser un numero");
        }
        $horas=(int)$horas;
        if($horas<1||$horas>1000){
            throw new Exception("Las horas deben ser entre 1  y 1000");
        }

    }

    function render($vista, $datos = [])
    {
        extract($datos);
        $archivoVista=__DIR__."/../vistas/".$vista.".php";
        if(!file_exists($archivoVista)){
            echo "Vista no encontrada";
            return;
        
        }
        $contenidoVista=$archivoVista;
        require __DIR__."/../vistas/layout.php";

        }

    function registarErrores($contexto, $e) {
    $log=__DIR__."/../../storage/error.log";
    $fecha=date('Y-m-d H:i:m');
    $errorMsg="[$fecha]|$contexto|".$e->getMessage()."|".$e->getFile()."|".$e->getLine(). PHP_EOL;
    file_put_contents($log,$errorMsg, FILE_APPEND);
    }
}
