<?php
require_once __DIR__ . "/nota.php";

class RepositorioNotas
{
    private $path;


    function __construct()
    {
        $this->path = __DIR__ . "/../../storage/notas.txt";
    }

    function obtenerTodas()
    {
        if (!file_exists($this->path)) {
            return [];
        }
        $notas = fopen($this->path, "r");
        $notasCargadas = [];
        while (!feof($notas)) {
            $linea = fgets($notas);
            $nota = Nota::crearDesdeLinea($linea);
            if ($nota !== null) { // Solo agregamos si es una nota válida
            $notasCargadas[] = $nota;
        }
        }
        return $notasCargadas;
    }

    function agregar($nota)
    {
        try {
            $linea = $nota->convertirALinea();
            $final = file_put_contents($this->path, $linea, FILE_APPEND);
            echo $this->path;
            if ($final === false) {
                throw new Exception("No se pudo añadir linea\n");
            }
        } catch (Throwable $e) {
            $logPath = __DIR__ . "/../storage/error.log";
            $fecha = date("Y-m-d H:i:s");
            $errorMsg = "[$fecha]|Agregar|" . $e->getMessage() . "|" . $e->getFile() . PHP_EOL;
            file_put_contents($logPath, $errorMsg, FILE_APPEND);
        }
    }
}
