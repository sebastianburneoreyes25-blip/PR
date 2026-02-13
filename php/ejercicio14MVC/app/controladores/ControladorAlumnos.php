<?php

require_once __DIR__."/../modelos/RepositorioAlumnos.php";

class ControladorAlumnos{

    public $repositorio;

    public function __construct(){

       $this->repositorio=new RepositorioAlumnos;
    }

    public function crear(){
        $this->render('alumnos/crear',
        ['antiguos'=>['nombre'=>'','edad'=>'','email'=>'']]);
    }

    function guardar(){
        if($_SERVER['REQUEST_METHOD']!=='POST'){//Si no detecta el post, mandara el error de no detectado y redirije de nuevo a crear
            header('Location: index.php?accion=crear');
            throw new Exception('No se detecto "POST"');
        }
            $nombre=$_POST['nombre'];
            $edad=$_POST['edad'];
            $email=$_POST['email'];
            
            try{
            $this->validar($nombre,$email,$edad);

            $alumno=new Alumno(
                null,
                $nombre,
                $email,
                (int)$edad,
                date('Y-m-d H:i:s')
            );
            
            $this->repositorio->insertar($alumno);
            header('Location: index.php?accion=correcto');
            exit;

            }catch (Throwable $e){
            $this->registrarError('Guardar',$e);
            $this->render('alumnos/crear',['error'=>[//al tener 'error' en la pagina a renderizar detectara que existe y podra mostrarnos que hay un error sin romperse
                $e->getMessage(),
                'antiguos'=>['nombre'=>$nombre, 'email'=>$email, 'edad'=>$edad]
            ]]);
            header('Location: index.php?accion=crear');//nos redirige a crear
            exit;

            }            

    }

    function correcto(){//solo lleva a la vista correcto

        $this->render('alumnos/correcto',["alumno"=>'']);

    }

    function render($vista,$datos=[]){
        extract($datos);
        $archivoVista=__DIR__."/../vistas/".$vista.".php";
        if(!file_exists($archivoVista)){
            echo 'Vista no encontrada';
        }
        $contenidoVista=$archivoVista;//Luego se pedira Contenido vista 
        require __DIR__.'/../vistas/layout.php';//Asi cargamos la vista con el diseño del layout
        
    }    

    function registrarError($contexto,$e){
        $fecha=date('Y-m-d H:i:s');
        $log=__DIR__."/../../storage/error.log";
        $errorMSG="[$fecha]|$contexto|". $e->getMessage()."|". $e->getFile(). "|". $e->getLine(). PHP_EOL;
        file_put_contents($log,$errorMSG,FILE_APPEND);
    }

    function validar($nombre,$email,$edad){
        if(strlen($nombre)<3){
            throw new Exception('Nombre muy corto');
        }
        if($email=='' || !filter_var($email, FILTER_VALIDATE_EMAIL)){
            throw new Exception('Email con formato incorrecto: '.$email);
        }
        if($edad==''||!ctype_digit($edad)){
            throw new Exception("Edad vacia o con formato incorrecto: [$edad]");
        }
        $edadInt=(int)$edad;
        if($edadInt<0 || $edadInt>120){
            throw new Exception("Edad en rango incorrecto(<3 o >120): [$edadInt]");
        }
    }
}


?>