<?php

require_once __DIR__ . "/tarea.php";

class RepositorioTarea
{

    public $path;

    public function __construct()
    {
        $this->path = __DIR__ . "/../../storage/tareas.txt";
    }

    public function obtenerTareas()
    {
        if (!file_exists($this->path)) {
            return [];
        }
        $lineasTareas = fopen($this->path, "r");
        $arrayTareas = [];
        while (!feof($lineasTareas)) {
            $linea = fgets($lineasTareas);
            $tarea = Tarea::crearDesdeLinea($linea);
            if ($tarea !== null) {
                $arrayTareas[] = $tarea;
            }
        }
        return $arrayTareas;
    }

    public function agregar($tarea)
    {
        try {
            $linea = $tarea->convertirALinea();
            $resultado = file_put_contents($this->path, $linea, FILE_APPEND); //file_put_content devolvera false en caso que no se pudiera añadir la linea
            if ($resultado === false) {
                throw new Exception("No se pudo añadir la linea " . $linea . "al archivo $this->path \n");
            }
        } catch (Throwable $e) {
            $logPath = __DIR__ . "/../storage/error.log";
            $fecha = date("Y-m-d H:i:s");
            $errorMsg = "[$fecha]|Agregar|" . $e->getMessage() . "|" . $e->getFile() . PHP_EOL;
            file_put_contents($logPath, $errorMsg, FILE_APPEND);
        }
    }
}
