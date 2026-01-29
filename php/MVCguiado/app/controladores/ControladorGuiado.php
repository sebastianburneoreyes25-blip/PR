<?php

require_once __DIR__ . "/../modelos/repositorioNotas.php";

class Controlador
{

    public $repositorio;

    function __construct()
    {
        $this->repositorio = new RepositorioNotas;
    }

    function render($vista, $datos=[])//renderizamos la ruta dada y le damos que dato debe extraer
    {
        extract($datos);
        $archivoVista = __DIR__ . "/../vistas/" . $vista . ".php";
        if (!file_exists($archivoVista)) {
            echo "Vista no encontrada: " . $vista;
            echo $archivoVista;
            return;
        }
        $contenidoVista = $archivoVista;
        require_once __DIR__ . "/../vistas/layout.php";
    }

    function registrarErrores($contexto, $e)
    {
        
        $log = __DIR__ . "/../../storage/error.log";
        echo $log;
        $fecha = date("Y-m-d H:i:s");
        $errorMsg = "[$fecha]|$contexto|" . $e->getMessage() . "|" . $e->getFile() . "|" . $e->getLine() . PHP_EOL;
        file_put_contents($log, $errorMsg, FILE_APPEND);
    }

    function listar(){
        try {
            $notas=$this->repositorio->obtenerTodas();//usamos el metodo obtener todas para guardar el valor de notas
            $this->render('notas/listar', ['notas'=>$notas]);//renderizamos listar junto con los datos de notas.

        } catch (Throwable $e) {
            $this->registrarErrores("Listar",$e);//registramos el contexto del error 
            $this->render('notas/listar',['notas'=>[], 'error'=>'No se pudieron cargar las notas']);//renderizamos listar con notas vacio y danto otro dato'error' para que imprima el mensaje.
            exit;       
            }
    }

    function crear(){
        $this->render('notas/crear',['Antiguos'=>['Texto','']]);
    }

    function guardar(){
        if($_SERVER['REQUEST_METHOD']=="POST"){

            try{
            $texto=$_POST["texto"]??'';
            $texto=str_replace(["\r\n", "\n", "\r"], " ", $texto);
            $this->validar($texto);
            $id=(string) time();
            $fecha=date("Y-m-s H:i:s");
            $nota=new Nota($id,$texto,$fecha);
            $this->repositorio->agregar($nota);
            header("Location: index.php?accion=listar");
            exit;
            }catch (Throwable $e){
                $this->registrarErrores("Guardar",$e);//registramos el contexto del error 
                header("Location: index.php?accion=listar");
                exit;

            }

        }

    }

    function validar($texto){
        if(strlen($texto)<3 || strlen($texto)>80){
            throw new Exception("El texto no cumple los requisitos");
            
        }
    }

}
