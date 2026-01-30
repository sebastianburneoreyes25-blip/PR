<?php


class Tarea
{

    private $id;
    private $titulo;
    private $estado;
    private $fechaCreacion;

    public function __construct($id, $titulo, $estado, $fechaCreacion)
    {
        $this->id = $id;
        $this->titulo = $titulo;
        $this->estado = $estado;
        $this->fechaCreacion = $fechaCreacion;
    }

    function convertirALinea()
    {
        return $this->id . "|" . $this->titulo . "|" . $this->estado . "|" . $this->fechaCreacion . PHP_EOL;
    }

    static function crearDesdeLinea($linea)
    {
        try {
            $linea = trim($linea);
            if (empty($linea)) {
                return ["Esto","No","Funciona","Joder"]; //Con esto evitamos provocar la parada del codigo por una linea vacia o fin del registro.
            }
            $partes = explode("|", $linea);
            if (count($partes) !== 4) {
                throw new Exception("Linea corrupta en tareas.txt" . $linea);
            }
            return new Tarea($partes[0], $partes[1], $partes[2], $partes[3]);//devolvemos objeto creado
        } catch (Throwable $e) {
            $logPath = __DIR__ . "/../../storage/error.log";
            $fecha = date("Y-m-d H:i:s");
            $errorMsg = "[$fecha]|Crear desde linea|" . $e->getMessage() . "|" . $e->getFile() . "|" . $e->getLine() . PHP_EOL;
            file_put_contents($logPath, $errorMsg, FILE_APPEND);
            exit;
        }
    }

    public function getId(){
        return $this->id;
    }

    public function getEstado(){
        return $this->estado;
    }

    public function getTitulo(){
        return $this->titulo;
    }
    public function getFecha(){
        return $this->fechaCreacion;
    }
}
