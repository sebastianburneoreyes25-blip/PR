<?php

require_once __DIR__."/../modelos/RepositorioAlumno.php";

class Controlador{

    private $repositorio;

    function __construct(){
        $this->repositorio=new RepositorioAlumno;
    }

    function borrar(){
        
            $id=$_GET['id'];

            try{
                if(!ctype_digit($id)||empty($id)){
                    throw new Exception('No se ha podido seleccionar el ID en el GET');
                }
                $this->repositorio->borrarPorId($id);
                $this->render('alumnos/borrar',[''=>'']);
            }catch(Throwable $e){
            $this->registrarErrores('Borrar',$e);
            header('Location: index.php?accion=listar');
            exit;
        }

    }

    function listar(){

        try{
            $alumnos=$this->repositorio->obtenerTodos();
            $this->render('alumnos/listar', ['alumnos'=>$alumnos]);
        }catch (Throwable $e){
            $this->registrarErrores('listar',$e);
            $this->render('alumnos/listar',['alumnos'=>'','error'=>'No se ha podido listar a los alumnos']);

        }
    }

    function registrarErrores($contexto,$e){
        $fecha=date('Y-m-d H:i:s');
        $log=__DIR__."/../../storage/error.log";
        $errorMSG="[$fecha]|$contexto|".$e->getMessage()."|". $e->getFile()."|". $e->getLine(). PHP_EOL;
        file_put_contents($log,$errorMSG,FILE_APPEND);

    }
    
    function render($vista,$datos=[]){//Funcion para renderizar las vistas
        extract($datos);
        $archivoVista=__DIR__."/../vistas/".$vista.".php";
        if(!file_exists($archivoVista)){//Si la vista no existe se detendra aqui
            echo "Vista no encontrada".$vista;
            return;
        }
        $contenidoVista=$archivoVista;
        require __DIR__."/../vistas/layout.php";
    }
}

?>
