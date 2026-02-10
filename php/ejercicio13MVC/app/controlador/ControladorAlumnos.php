<?php

require_once __DIR__ . "/../modelos/RepositorioAlumnos.php";

class Controlador//El controlador practicamente solo usa ducniones externas(quitando render y )
{

    private $repositorio;

    function __construct()
    {
        $this->repositorio = new RepositorioAlumnos;
    }

    function listar()
    {
        try {
            $alumnos = $this->repositorio->obtenerTodos();
            $this->render('alumnos/listar', ['alumnos' => $alumnos]);
        } catch (Throwable $e) {
            $this->registrarErrores('Listar', $e);
            $this->render('alumnos/listar', ['alumnos' => '', 'error' => 'No se pudo cargar los alumnos']);
        }
    }

    function render($vista, $datos = [])
    {
        extract($datos);
        $archivoVista = __DIR__ . "/../vistas/" . $vista . ".php";
        if (!file_exists($archivoVista)) {
            echo "Vista no encontrada";
        }
        $contenidoVista = $archivoVista;
        require __DIR__ . "/../vistas/layout.php";
    }

    function registrarErrores($contexto, $e)
    {
        $log = __DIR__ . "/../../storage/error.log";
        $fecha = date('Y-m-d H:i:s');
        $msgError = "[$fecha]|$contexto|" . $e->getMessage() . "|" . $e->getFile() . "|" . $e->getLine() . PHP_EOL;
        file_put_contents($log, $msgError, FILE_APPEND);
        
    }
}
?>