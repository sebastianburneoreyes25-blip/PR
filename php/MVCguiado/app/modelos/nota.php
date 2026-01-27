<?php

class Nota
{
    private $id;
    private $texto;
    private $fecha;

    function __construct($id,$texto,$fecha){
        $this->id=$id;
        $this->texto=$texto;
        $this->fecha=$fecha;
    }

    function convertirALinea()
    {
        return $this->id . "|" . $this->texto . "|" . $this->fecha . PHP_EOL;
    }

    static function crearDesdeLinea($linea)
    {
        try {
            $partes = explode("|", trim($linea));
            if (count($partes) !== 3) {
                throw new Exception("Linea corrupta en notas.txt: " . $linea . PHP_EOL);
            }
            return $partes;
        } catch (Throwable $e) {
            $logPath = __DIR__ . "/../../storage/error.log";
            $fecha = date("Y-m-d H:i:s");
            $errorMsg = "[$fecha]|Crear desde linea|" . $e->getMessage() . "|" . $e->getFile() . "|" . $e->getLine() . PHP_EOL;
            file_put_contents($logPath, $errorMsg, FILE_APPEND);
        }
    }
}
