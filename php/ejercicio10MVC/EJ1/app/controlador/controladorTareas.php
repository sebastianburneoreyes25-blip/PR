<?php


require_once __DIR__ . "/../modelos/repositorioTarea.php"; //necesitamos importar el archivo repositorio para usar los metodos de la clase

class ControladorTareas
{

    public $repositorio;

    public function __construct()
    {
        $this->repositorio = new RepositorioTarea;
    }

    public function render($vista, $datos = [])
    {

        extract($datos); //extract creara una variable con el contenido de datos=[]. La clave será $datos y el valor [].
        $archivoVista = __DIR__ . "/../vistas/" . $vista . ".php";
        if (!file_exists($archivoVista)) {
            echo "No existe la vista " . $vista;
            echo $archivoVista;
            $contenidoVista="";
            exit;
        }
        $contenidoVista = $archivoVista; //contenido vista es requerido en el index.php
        require __DIR__ . "/../vistas/layout.php";
    }

    public function listar()
    {
        try {
            $tareas = $this->repositorio->obtenerTareas();
            $this->render("/tareas/listar", ['tarea' => $tareas]);
        } catch (Throwable $e) {
            $this->registrarErrores("Listar", $e);
            $this->render('/tareas/listar', ['notas' => [], 'error' => 'No se pudieron cargar las notas']); //renderizamos listar con notas vacio y danto otro dato'error' para que imprima el mensaje.
            exit;
        }
    }

    public function crear()
    {
        $this->render("/tareas/crear", ['Antiguos' => ['texto', '']]);
    }

    public function guardar()
    {
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            try {
                $titulo = $_POST["titulo"];
                $titulo=str_replace(["\n\r","\n","\r"], " ",$titulo);
                $this->validar($titulo);
                $id = (string)time();
                $estado = "Pendiente";
                $fechaCreacion = date("Y-m-d H:i:s");
                $tarea = new Tarea($id, $titulo, $estado, $fechaCreacion);
                $this->repositorio->agregar($tarea);
                header("Location: index.php?accion=listar");
                exit;
            } catch (Throwable $e) {
                $this->registrarErrores("Guardar", $e);
                header("Location: index.php?accion=listar");
                exit;
            }
        }
    }

    public function validar($titulo)
    {
        if (strlen($titulo) < 3 || strlen($titulo) > 60) {
            throw new Exception("Tarea con formato no valido");
        }
    }

    public function registrarErrores($contexto, $e)
    {
        $fecha = date("Y-m-s H:i:s");
        $msgError = "[$fecha] | Error: " . $contexto . "|" . $e->getMessage() . "|" . $e->getFile() . "|" . $e->getLine() . PHP_EOL;
        $log = __DIR__ . "/../../storage/error.log";
        file_put_contents($log, $msgError, FILE_APPEND);
    }
}
